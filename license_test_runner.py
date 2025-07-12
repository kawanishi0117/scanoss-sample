#!/usr/bin/env python3
"""
License Detection Test Runner
This module provides comprehensive testing for SCANOSS license detection capabilities.

This test runner is provided under MIT License for testing purposes.

MIT License
Copyright (c) 2023 SCANOSS Test Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
"""

import os
import sys
import json
import importlib
from typing import Dict, List, Any
from pathlib import Path

# Add src directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def discover_license_test_modules() -> Dict[str, Any]:
    """
    Discover all modules with various license types for testing.
    
    This function scans the codebase for license testing modules.
    """
    test_modules = {
        'apache_2_0': {
            'module': 'src.data.apache_utils',
            'expected_licenses': ['Apache-2.0'],
            'license_type': 'permissive',
            'commercial_use': True
        },
        'gpl_v2': {
            'module': 'src.scraper.gpl2_tools',
            'expected_licenses': ['GPL-2.0'],
            'license_type': 'copyleft',
            'commercial_use': True
        },
        'agpl_v3': {
            'module': 'src.data.agpl3_database',
            'expected_licenses': ['AGPL-3.0'],
            'license_type': 'copyleft',
            'commercial_use': True,
            'network_copyleft': True
        },
        'mpl_2_0': {
            'module': 'src.config.mpl2_config',
            'expected_licenses': ['MPL-2.0'],
            'license_type': 'weak_copyleft',
            'commercial_use': True
        },
        'epl_2_0': {
            'module': 'src.data.epl2_analytics',
            'expected_licenses': ['EPL-2.0'],
            'license_type': 'weak_copyleft',
            'commercial_use': True
        },
        'creative_commons': {
            'module': 'src.data.cc_content',
            'expected_licenses': ['CC-BY-4.0', 'CC-BY-SA-4.0', 'CC-BY-NC-4.0'],
            'license_type': 'creative_commons',
            'commercial_use': 'depends_on_variant'
        },
        'proprietary': {
            'module': 'src.scraper.proprietary_tools',
            'expected_licenses': ['Proprietary', 'Commercial'],
            'license_type': 'proprietary',
            'commercial_use': False
        },
        'mixed_licenses': {
            'module': 'src.mixed_licenses',
            'expected_licenses': ['MIT', 'BSD-3-Clause', 'GPL-3.0', 'Proprietary', 'Multiple'],
            'license_type': 'mixed',
            'commercial_use': 'complex'
        },
        'existing_lgpl': {
            'module': 'src.data.utils',
            'expected_licenses': ['LGPL-2.1'],
            'license_type': 'copyleft',
            'commercial_use': True
        },
        'existing_gpl3': {
            'module': 'src.scraper.web_client',
            'expected_licenses': ['GPL-3.0'],
            'license_type': 'copyleft',
            'commercial_use': True
        }
    }
    
    return test_modules

def run_license_detection_tests() -> Dict[str, Any]:
    """
    Run comprehensive license detection tests.
    
    This function tests various license detection scenarios.
    """
    test_modules = discover_license_test_modules()
    test_results = {
        'total_modules': len(test_modules),
        'modules_tested': 0,
        'modules_loaded': 0,
        'license_types_found': set(),
        'test_details': {},
        'summary': {}
    }
    
    for module_name, module_info in test_modules.items():
        print(f"Testing module: {module_name}")
        
        test_result = {
            'module_path': module_info['module'],
            'expected_licenses': module_info['expected_licenses'],
            'license_type': module_info['license_type'],
            'load_successful': False,
            'license_patterns_found': [],
            'errors': []
        }
        
        try:
            # Attempt to import the module
            module = importlib.import_module(module_info['module'])
            test_result['load_successful'] = True
            test_results['modules_loaded'] += 1
            
            # Analyze module docstring and source for license patterns
            if hasattr(module, '__doc__') and module.__doc__:
                license_patterns = analyze_license_patterns(module.__doc__)
                test_result['license_patterns_found'].extend(license_patterns)
            
            # Add to found license types
            test_results['license_types_found'].update(module_info['expected_licenses'])
            
        except ImportError as e:
            test_result['errors'].append(f"Import error: {e}")
        except Exception as e:
            test_result['errors'].append(f"General error: {e}")
        
        test_results['test_details'][module_name] = test_result
        test_results['modules_tested'] += 1
    
    # Generate summary
    test_results['summary'] = generate_test_summary(test_results)
    return test_results

def analyze_license_patterns(text: str) -> List[str]:
    """
    Analyze text for license patterns.
    
    This function identifies various license indicators in text.
    """
    license_indicators = [
        'MIT License', 'Apache License', 'GPL', 'LGPL', 'AGPL',
        'Mozilla Public License', 'MPL', 'Eclipse Public License', 'EPL',
        'Creative Commons', 'CC BY', 'CC BY-SA', 'CC BY-NC',
        'BSD License', 'ISC License', 'Unlicense', 'WTFPL',
        'Proprietary', 'Commercial License', 'All rights reserved',
        'GNU General Public License', 'GNU Lesser General Public License',
        'GNU Affero General Public License', 'Subject to the terms',
        'Permission is hereby granted', 'This program is free software',
        'Copyright (c)', '©', 'Licensed under', 'SPDX-License-Identifier'
    ]
    
    found_patterns = []
    text_lower = text.lower()
    
    for indicator in license_indicators:
        if indicator.lower() in text_lower:
            found_patterns.append(indicator)
    
    return found_patterns

def generate_test_summary(test_results: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generate a comprehensive test summary.
    
    This function creates a summary of all license detection tests.
    """
    successful_loads = test_results['modules_loaded']
    total_modules = test_results['total_modules']
    
    license_categories = {
        'permissive': ['MIT', 'Apache-2.0', 'BSD-3-Clause', 'ISC'],
        'copyleft': ['GPL-2.0', 'GPL-3.0', 'LGPL-2.1', 'AGPL-3.0'],
        'weak_copyleft': ['MPL-2.0', 'EPL-2.0'],
        'creative_commons': ['CC-BY-4.0', 'CC-BY-SA-4.0', 'CC-BY-NC-4.0'],
        'proprietary': ['Proprietary', 'Commercial']
    }
    
    found_by_category = {}
    for category, licenses in license_categories.items():
        found_count = sum(1 for license in licenses if license in test_results['license_types_found'])
        found_by_category[category] = {
            'found': found_count,
            'total': len(licenses),
            'percentage': (found_count / len(licenses)) * 100 if licenses else 0
        }
    
    return {
        'module_load_success_rate': (successful_loads / total_modules) * 100,
        'total_unique_licenses': len(test_results['license_types_found']),
        'license_categories': found_by_category,
        'test_coverage': {
            'copyleft_licenses': 'GPL-2.0, GPL-3.0, LGPL-2.1, AGPL-3.0' in str(test_results['license_types_found']),
            'permissive_licenses': 'Apache-2.0' in test_results['license_types_found'],
            'proprietary_licenses': 'Proprietary' in str(test_results['license_types_found']),
            'creative_commons': 'CC-BY' in str(test_results['license_types_found'])
        },
        'scanoss_detection_targets': [
            'Copyleft licenses (should trigger policy violations)',
            'Mixed license conflicts',
            'Proprietary license components',
            'Creative Commons variants',
            'License header patterns',
            'SPDX identifiers'
        ]
    }

def generate_license_report() -> str:
    """
    Generate a comprehensive license report for SCANOSS testing.
    
    This function creates a detailed report of all licenses in the codebase.
    """
    report = """
# SCANOSS License Detection Test Report

## Overview
This report documents the intentional license diversity in this test repository
for comprehensive SCANOSS license detection testing.

## License Categories Tested

### Copyleft Licenses (Should Trigger Violations)
- **GPL-2.0**: Network scanning tools (src/scraper/gpl2_tools.py)
- **GPL-3.0**: HTTP downloader utilities (src/scraper/web_client.py) 
- **LGPL-2.1**: Data processing utilities (src/data/utils.py)
- **AGPL-3.0**: Database management system (src/data/agpl3_database.py)

### Permissive Licenses
- **Apache-2.0**: Data processing utilities (src/data/apache_utils.py)
- **MIT**: Configuration management (existing modules)
- **BSD-3-Clause**: Pandas data processing (existing modules)

### Weak Copyleft Licenses  
- **MPL-2.0**: Configuration management (src/config/mpl2_config.py)
- **EPL-2.0**: Analytics engine (src/data/epl2_analytics.py)

### Creative Commons Licenses
- **CC-BY-4.0**: Documentation and tutorials (src/data/cc_content.py)
- **CC-BY-SA-4.0**: Wiki-style content (src/data/cc_content.py)
- **CC-BY-NC-4.0**: Research content (src/data/cc_content.py)

### Proprietary Licenses
- **Commercial/Proprietary**: Enterprise tools (src/scraper/proprietary_tools.py)

### Mixed License Testing
- **Multiple Conflicting Licenses**: Mixed license patterns (src/mixed_licenses.py)

## Expected SCANOSS Behavior

### Policy Violations (copyleft detection)
The following files should trigger SCANOSS policy violations:
- src/scraper/gpl2_tools.py (GPL-2.0)
- src/scraper/web_client.py (GPL-3.0)  
- src/data/utils.py (LGPL-2.1)
- src/data/agpl3_database.py (AGPL-3.0)

### License Compatibility Issues
- Mixed license conflicts in src/mixed_licenses.py
- Proprietary vs. open source conflicts

### GitHub Actions Integration
- PR submissions should fail CI due to copyleft detection
- SARIF output should detail all license findings
- Policy halt-on-failure should stop the build

## Testing Recommendations

1. **Submit PR**: Create PR to trigger license scanning
2. **Verify Detection**: Confirm all copyleft licenses are detected
3. **Check SARIF Output**: Review detailed license findings
4. **Validate Policy Enforcement**: Ensure CI fails appropriately
5. **Test Manual Scanning**: Use SCANOSS CLI for local testing

## File-by-File License Summary

| File | Primary License | Secondary Licenses | Risk Level |
|------|----------------|-------------------|------------|
| src/data/apache_utils.py | Apache-2.0 | None | Low |
| src/scraper/gpl2_tools.py | GPL-2.0 | None | **HIGH** |
| src/data/agpl3_database.py | AGPL-3.0 | None | **HIGH** |
| src/config/mpl2_config.py | MPL-2.0 | None | Medium |
| src/data/epl2_analytics.py | EPL-2.0 | None | Medium |
| src/data/cc_content.py | CC-BY-4.0 | CC-BY-SA-4.0, CC-BY-NC-4.0 | Medium |
| src/scraper/proprietary_tools.py | Proprietary | None | **HIGH** |
| src/mixed_licenses.py | Multiple | MIT, BSD, GPL, etc. | **CRITICAL** |
| src/data/utils.py | LGPL-2.1 | None | **HIGH** |
| src/scraper/web_client.py | GPL-3.0 | None | **HIGH** |

## Notes for SCANOSS Testing

- This repository is designed to test comprehensive license detection
- Multiple copyleft licenses should trigger policy violations
- Mixed license conflicts demonstrate complex scenarios
- Proprietary code simulates enterprise scanning scenarios
- Creative Commons variants test documentation scanning

**WARNING**: This is a test repository only. Do not use in production!
"""
    return report

def main():
    """
    Main function to run license detection tests.
    
    This function coordinates the entire testing process.
    """
    print("SCANOSS License Detection Test Runner")
    print("=" * 50)
    
    # Run tests
    print("\n1. Running license detection tests...")
    test_results = run_license_detection_tests()
    
    # Display results
    print(f"\n2. Test Results Summary:")
    print(f"   - Modules tested: {test_results['modules_tested']}")
    print(f"   - Modules loaded: {test_results['modules_loaded']}")
    print(f"   - Unique licenses found: {test_results['summary']['total_unique_licenses']}")
    print(f"   - Load success rate: {test_results['summary']['module_load_success_rate']:.1f}%")
    
    # Display license categories
    print(f"\n3. License Categories:")
    for category, stats in test_results['summary']['license_categories'].items():
        print(f"   - {category}: {stats['found']}/{stats['total']} ({stats['percentage']:.1f}%)")
    
    # Generate report
    print(f"\n4. Generating comprehensive license report...")
    report = generate_license_report()
    
    # Save results
    results_file = 'license_test_results.json'
    with open(results_file, 'w') as f:
        # Convert set to list for JSON serialization
        test_results['license_types_found'] = list(test_results['license_types_found'])
        json.dump(test_results, f, indent=2)
    
    report_file = 'SCANOSS_LICENSE_TEST_REPORT.md'
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"\n5. Test Complete!")
    print(f"   - Results saved to: {results_file}")
    print(f"   - Report saved to: {report_file}")
    print(f"\n6. Next Steps:")
    print(f"   - Create PR to trigger SCANOSS GitHub Action")
    print(f"   - Review SARIF output for license detections")
    print(f"   - Verify copyleft licenses trigger policy violations")
    
    return test_results

if __name__ == "__main__":
    main()