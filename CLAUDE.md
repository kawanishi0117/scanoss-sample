# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a SCANOSS license scanning test repository containing intentionally mixed-license Python code designed to test comprehensive license detection capabilities. The project includes:

- **Permissive licensed code** (MIT, BSD-3-Clause, Apache-2.0, ISC, Unlicense, WTFPL, Boost, zlib) 
- **Copyleft licensed code** (GPL-2.0, GPL-3.0, LGPL-2.1, AGPL-3.0) for testing detection
- **Weak copyleft licenses** (MPL-2.0, EPL-2.0) for compatibility testing
- **Creative Commons licenses** (CC-BY-4.0, CC-BY-SA-4.0, CC-BY-NC-4.0) for content licensing
- **Proprietary/Commercial licenses** for enterprise scanning scenarios
- **Mixed license conflicts** for complex detection testing
- **Web scraping and data processing utilities**
- **Automated license scanning via GitHub Actions**

## Commands and Development

### Running Tests
```bash
python test.py  # Basic test runner (currently empty)
python license_test_runner.py  # Comprehensive license detection test runner
```

### License Scanning
The repository uses SCANOSS for automated license detection:
```bash
# License scanning runs automatically on PRs via GitHub Actions
# Manual scanning can be done with SCANOSS CLI tools
```

### Python Environment
This is a pure Python project with standard library dependencies plus:
- `click` (MIT) - CLI configuration
- `pandas` (BSD-3-Clause) - Data processing  
- `beautifulsoup4` (MIT) - HTML parsing
- `requests` (Apache-2.0) - HTTP client
- `pyyaml` (MIT) - Configuration files

## Architecture

### Module Structure
```
src/
├── config/              # Configuration management
│   ├── settings.py      # CLI and YAML config using click (MIT)
│   └── mpl2_config.py   # Mozilla Public License 2.0 configuration
├── data/               # Data processing utilities
│   ├── processor.py    # Pandas-based data processing (BSD-3-Clause)
│   ├── utils.py        # LGPL-2.1 utilities (intentional for testing)
│   ├── apache_utils.py # Apache-2.0 licensed data utilities
│   ├── agpl3_database.py # AGPL-3.0 database management system
│   ├── epl2_analytics.py # Eclipse Public License 2.0 analytics
│   └── cc_content.py   # Creative Commons licensed content processing
├── scraper/            # Web scraping components
│   ├── parser.py       # BeautifulSoup HTML parsing (MIT)
│   ├── web_client.py   # GPL-3.0 HTTP client (intentional for testing)
│   ├── gpl2_tools.py   # GPL-2.0 network scanning tools
│   └── proprietary_tools.py # Proprietary/Commercial licensed tools
├── mixed_licenses.py   # Mixed license patterns for complex testing
└── license_test_runner.py # Comprehensive license detection test runner
```

### License Testing Design
The codebase intentionally contains diverse licenses to test comprehensive SCANOSS detection:

**Copyleft Licenses (Should Trigger Policy Violations):**
- **gpl2_tools.py**: GPL-2.0 network scanning utilities with full GPL headers
- **web_client.py**: GPL-3.0 HTTP client with wget-like functionality
- **utils.py**: LGPL-2.1 data utilities with explicit LGPL license headers
- **agpl3_database.py**: AGPL-3.0 database system with network copyleft requirements

**Permissive Licenses:**
- **apache_utils.py**: Apache-2.0 data processing with full Apache license headers
- **Other modules**: MIT, BSD-3-Clause licenses for baseline compatibility

**Weak Copyleft:**
- **mpl2_config.py**: Mozilla Public License 2.0 configuration management
- **epl2_analytics.py**: Eclipse Public License 2.0 analytics engine

**Creative Commons:**
- **cc_content.py**: Multiple CC variants (BY, BY-SA, BY-NC) for content licensing

**Proprietary/Commercial:**
- **proprietary_tools.py**: Simulated proprietary licenses for enterprise testing

**Mixed License Conflicts:**
- **mixed_licenses.py**: Multiple conflicting licenses in one file for complex scenarios

### Key Components

1. **Configuration Management**:
   - `src/config/settings.py`: Click-based CLI configuration (MIT)
   - `src/config/mpl2_config.py`: Mozilla-style configuration system (MPL-2.0)

2. **Data Processing Systems**:
   - `src/data/processor.py`: Pandas DataFrame operations (BSD-3-Clause)
   - `src/data/apache_utils.py`: Apache Commons-style utilities (Apache-2.0)
   - `src/data/agpl3_database.py`: MongoDB-style database system (AGPL-3.0)
   - `src/data/epl2_analytics.py`: Eclipse-style analytics engine (EPL-2.0)

3. **Web Scraping & Network Tools**:
   - `src/scraper/parser.py`: BeautifulSoup-based HTML parsing (MIT)
   - `src/scraper/web_client.py`: GPL wget-like downloader (GPL-3.0)
   - `src/scraper/gpl2_tools.py`: nmap-style network scanner (GPL-2.0)
   - `src/scraper/proprietary_tools.py`: Enterprise encryption tools (Proprietary)

4. **License Testing Framework**:
   - `license_test_runner.py`: Comprehensive license detection testing
   - `src/mixed_licenses.py`: Mixed license conflict scenarios

## GitHub Actions Integration

The repository includes automated license scanning:
- **Workflow**: `.github/workflows/license-scan.yml`
- **Trigger**: Pull requests only
- **Policy**: Detects copyleft licenses (GPL/LGPL/AGPL)
- **Action**: Uses `scanoss/gha-code-scan@v1` with `policies: copyleft`
- **Behavior**: Fails CI when copyleft licenses detected (`policies.halt_on_failure: true`)

## Important Notes

### License Compliance
- This is a **test repository** with intentionally diverse and conflicting licenses
- **Copyleft licenses** (GPL-2.0, GPL-3.0, LGPL-2.1, AGPL-3.0) should trigger SCANOSS policy violations
- **Mixed license conflicts** in `mixed_licenses.py` create complex detection scenarios
- **Proprietary code** simulates enterprise scanning challenges
- **Creative Commons variants** test documentation and content licensing
- Do not use this codebase in production without comprehensive license review
- All license headers are intentionally explicit for testing purposes

### Development Guidelines
- Maintain license header comments when modifying test files
- Keep the intentional license mix for testing purposes
- Use Python standard library when possible
- Follow existing code patterns for each module
- Test license detection after making changes

### SCANOSS Testing
- **PR submissions** will trigger comprehensive license scanning
- **Expected behavior**: CI should fail due to copyleft license detection (GPL/LGPL/AGPL)
- **SARIF output** saved to `scanoss.sarif` for detailed review
- **Test runner**: Use `python license_test_runner.py` for local testing
- **File targets**: Multiple files with different license types for comprehensive coverage
- **Policy testing**: Verify halt-on-failure behavior with copyleft detection
- **Mixed license scenarios**: Test complex license conflict detection in `mixed_licenses.py`

### Expected SCANOSS Detections
The following files should trigger license violations:
- `src/scraper/gpl2_tools.py` (GPL-2.0)
- `src/scraper/web_client.py` (GPL-3.0)
- `src/data/utils.py` (LGPL-2.1)
- `src/data/agpl3_database.py` (AGPL-3.0)
- `src/mixed_licenses.py` (Multiple conflicting licenses)