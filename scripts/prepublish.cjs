const fs = require('fs');
const path = require('path');

console.log('🔍 Validating package before publishing...\n');

const projectRoot = path.join(__dirname, '..');

// Required files for npm package
const requiredFiles = [
  'bin/index.js',
  'scripts/install.cjs',
  'src/server.py',
  'src/__init__.py',
  'requirements.txt',
  'create_templates.py',
  'package.json',
  'README.md'
];

// Optional but recommended files
const optionalFiles = [
  'LICENSE',
  '.npmignore',
  'templates/invoice.docx',
  'templates/report.docx',
  'templates/contract.docx',
  'templates/letter.docx'
];

let hasError = false;
let warnings = [];

console.log('Checking required files:');
console.log('------------------------');

// Check required files
for (const file of requiredFiles) {
  const filePath = path.join(projectRoot, file);
  if (!fs.existsSync(filePath)) {
    console.error(`❌ Missing required file: ${file}`);
    hasError = true;
  } else {
    const stats = fs.statSync(filePath);
    const size = (stats.size / 1024).toFixed(1);
    console.log(`✅ Found: ${file} (${size} KB)`);
  }
}

console.log('\nChecking optional files:');
console.log('------------------------');

// Check optional files
for (const file of optionalFiles) {
  const filePath = path.join(projectRoot, file);
  if (!fs.existsSync(filePath)) {
    console.log(`⚠️  Missing optional file: ${file}`);
    warnings.push(`Missing ${file}`);
  } else {
    console.log(`✅ Found: ${file}`);
  }
}

// Check bin file shebang
console.log('\nChecking executable configuration:');
console.log('-----------------------------------');

const binFile = path.join(projectRoot, 'bin/index.js');
if (fs.existsSync(binFile)) {
  const binContent = fs.readFileSync(binFile, 'utf8');
  if (!binContent.startsWith('#!/usr/bin/env node')) {
    console.error('❌ bin/index.js must start with shebang: #!/usr/bin/env node');
    hasError = true;
  } else {
    console.log('✅ Shebang line present in bin/index.js');
  }

  // Check if file is executable (Unix-like systems)
  try {
    fs.accessSync(binFile, fs.constants.X_OK);
    console.log('✅ bin/index.js is executable');
  } catch (e) {
    console.log('⚠️  bin/index.js may not be executable (this is OK on Windows)');
  }
}

// Check package.json configuration
console.log('\nChecking package.json:');
console.log('----------------------');

const packageJsonPath = path.join(projectRoot, 'package.json');
if (fs.existsSync(packageJsonPath)) {
  const packageJson = JSON.parse(fs.readFileSync(packageJsonPath, 'utf8'));

  if (!packageJson.name) {
    console.error('❌ package.json missing "name" field');
    hasError = true;
  } else {
    console.log(`✅ Package name: ${packageJson.name}`);
  }

  if (!packageJson.version) {
    console.error('❌ package.json missing "version" field');
    hasError = true;
  } else {
    console.log(`✅ Package version: ${packageJson.version}`);
  }

  if (!packageJson.bin || !packageJson.bin['docxtpl-mcp']) {
    console.error('❌ package.json missing bin configuration');
    hasError = true;
  } else {
    console.log('✅ Bin entry configured');
  }

  if (!packageJson.type || packageJson.type !== 'module') {
    console.log('⚠️  package.json "type" should be "module" for ES6 imports');
    warnings.push('Consider setting "type": "module" in package.json');
  } else {
    console.log('✅ ES6 module type configured');
  }
}

// Check Python files
console.log('\nChecking Python components:');
console.log('---------------------------');

const serverPath = path.join(projectRoot, 'src/server.py');
if (fs.existsSync(serverPath)) {
  const serverContent = fs.readFileSync(serverPath, 'utf8');
  if (serverContent.includes('async def main()')) {
    console.log('✅ MCP server main function found');
  } else {
    console.log('⚠️  Could not verify MCP server main function');
  }
}

// Summary
console.log('\n' + '='.repeat(50));

if (hasError) {
  console.error('\n❌ VALIDATION FAILED');
  console.error('Please fix the errors above before publishing.\n');
  process.exit(1);
} else if (warnings.length > 0) {
  console.log('\n⚠️  VALIDATION PASSED WITH WARNINGS:');
  warnings.forEach(w => console.log(`   - ${w}`));
  console.log('\n✅ Package can be published, but consider addressing the warnings.\n');
} else {
  console.log('\n✅ VALIDATION SUCCESSFUL');
  console.log('Package is ready to publish!\n');
  console.log('Next steps:');
  console.log('  1. Test locally: npm link && npx docxtpl-mcp');
  console.log('  2. Login to npm: npm login');
  console.log('  3. Publish: npm publish');
  console.log('  4. Test published: npx docxtpl-mcp@latest\n');
}