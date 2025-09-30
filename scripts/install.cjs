const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

console.log('📦 Setting up docxtpl-mcp...');

const projectRoot = path.join(__dirname, '..');
const requirementsPath = path.join(projectRoot, 'requirements.txt');

// Check Python availability
function getPythonCommand() {
  const commands = ['python3.12', 'python3.11', 'python3.10', 'python3', 'python'];
  for (const cmd of commands) {
    try {
      const result = execSync(`${cmd} --version`, { stdio: 'pipe' });
      console.log(`Found ${cmd}: ${result.toString().trim()}`);
      return cmd;
    } catch (e) {
      // Continue to next command
    }
  }
  console.log('⚠️  Python not found. Python 3.10+ is required.');
  console.log('   Please install Python from https://www.python.org/');
  console.log('   After installing Python, run: pip install -r requirements.txt');
  return null;
}

const pythonCmd = getPythonCommand();

if (pythonCmd) {
  try {
    // Check if pip is available
    execSync(`${pythonCmd} -m pip --version`, { stdio: 'pipe' });

    // Install Python packages
    console.log('📥 Installing Python dependencies...');
    console.log('   This may take a minute on first install...');

    // Use --user flag for user installation, --quiet for less output
    const pipCmd = `${pythonCmd} -m pip install --user --quiet -r "${requirementsPath}"`;

    try {
      execSync(pipCmd, { stdio: 'inherit' });
      console.log('✅ Python dependencies installed successfully!');
    } catch (pipError) {
      // Try without --user flag if user installation fails
      console.log('   Retrying without --user flag...');
      execSync(`${pythonCmd} -m pip install --quiet -r "${requirementsPath}"`, { stdio: 'inherit' });
      console.log('✅ Python dependencies installed successfully!');
    }

    // Create example templates if they don't exist
    const templatesDir = path.join(projectRoot, 'templates');
    const docxFiles = fs.existsSync(templatesDir)
      ? fs.readdirSync(templatesDir).filter(f => f.endsWith('.docx'))
      : [];

    if (docxFiles.length === 0) {
      console.log('📄 Creating example templates...');
      try {
        execSync(`${pythonCmd} "${path.join(projectRoot, 'create_templates.py')}"`, {
          cwd: projectRoot,
          stdio: 'inherit'
        });
        console.log('✅ Templates created successfully!');
      } catch (templateError) {
        console.log('⚠️  Could not create templates automatically.');
        console.log('   You can create them manually by running:');
        console.log(`   ${pythonCmd} create_templates.py`);
      }
    } else {
      console.log(`✅ Found ${docxFiles.length} existing templates`);
    }

    console.log('\n🎉 Setup complete! You can now use docxtpl-mcp');
    console.log('   Run: npx docxtpl-mcp');

  } catch (error) {
    console.error('⚠️  Some dependencies may not be installed:', error.message);
    console.log('\nPlease manually install Python dependencies:');
    console.log(`  ${pythonCmd} -m pip install -r requirements.txt`);
    console.log('\nThen create templates:');
    console.log(`  ${pythonCmd} create_templates.py`);
  }
} else {
  console.log('\n📌 Manual setup required:');
  console.log('   1. Install Python 3.10+ from https://www.python.org/');
  console.log('   2. Install dependencies: pip install -r requirements.txt');
  console.log('   3. Create templates: python create_templates.py');
  console.log('\nAfter setup, you can use: npx docxtpl-mcp');
}