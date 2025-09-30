#!/usr/bin/env node
import { spawn, spawnSync } from 'child_process';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';
import fs from 'fs';
import os from 'os';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const projectRoot = join(__dirname, '..');

// Check if running with --version flag
if (process.argv.includes('--version')) {
  const packageJson = JSON.parse(fs.readFileSync(join(projectRoot, 'package.json'), 'utf8'));
  console.log(`docxtpl-mcp v${packageJson.version}`);
  process.exit(0);
}

// Check Python environment
function checkPython() {
  const commands = ['python3.12', 'python3.11', 'python3.10', 'python3', 'python'];
  for (const cmd of commands) {
    try {
      const result = spawnSync(cmd, ['--version'], { stdio: 'pipe' });
      if (result.status === 0) {
        const version = result.stdout.toString();
        // Only log to stderr if not in MCP mode (MCP uses stdout for communication)
        if (process.env.MCP_MODE !== 'true') {
          console.error(`Using ${cmd}: ${version.trim()}`);
        }
        return cmd;
      }
    } catch (e) {
      // Silently continue to next command
    }
  }
  console.error('Error: Python 3.10+ is required but not found.');
  console.error('Please install Python from https://www.python.org/');
  process.exit(1);
}

// Start MCP server
function startServer() {
  const pythonCmd = checkPython();

  // Set up environment variables
  const env = {
    ...process.env,
    TEMPLATE_DIR: join(projectRoot, 'templates'),
    OUTPUT_DIR: process.env.OUTPUT_DIR || join(process.cwd(), 'output'),
    MCP_MODE: 'true'
  };

  // Ensure output directory exists
  const outputDir = env.OUTPUT_DIR;
  if (!fs.existsSync(outputDir)) {
    try {
      fs.mkdirSync(outputDir, { recursive: true });
    } catch (e) {
      // Silently handle if directory creation fails
    }
  }

  // Start Python process with stdio protocol for MCP
  const serverProcess = spawn(pythonCmd, ['-m', 'src.server'], {
    cwd: projectRoot,
    env: env,
    stdio: 'inherit'  // Important: MCP uses stdio communication
  });

  // Handle graceful shutdown
  process.on('SIGINT', () => {
    serverProcess.kill('SIGINT');
    process.exit(0);
  });

  process.on('SIGTERM', () => {
    serverProcess.kill('SIGTERM');
    process.exit(0);
  });

  serverProcess.on('error', (err) => {
    console.error('Failed to start server:', err.message);
    process.exit(1);
  });

  serverProcess.on('exit', (code, signal) => {
    if (signal) {
      process.exit(0);
    } else {
      process.exit(code || 0);
    }
  });
}

// Main execution
try {
  startServer();
} catch (error) {
  console.error('Error starting docxtpl-mcp:', error.message);
  process.exit(1);
}