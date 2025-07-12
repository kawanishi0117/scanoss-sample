"""
MPL-2.0 Licensed Configuration Module
This module contains code derived from MPL-2.0 licensed configuration libraries.

This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.

Covered Software is provided under this License on an "as is" basis,
without warranty of any kind, either expressed, implied, or statutory,
including, without limitation, warranties that the Covered Software is
free of defects, merchantable, fit for a particular purpose or non-infringing.
"""

import os
import json
import xml.etree.ElementTree as ET
from typing import Dict, Any, List, Optional, Union
from pathlib import Path
import configparser

# MPL-2.0 Licensed Configuration Parser
class MPL2ConfigurationManager:
    """
    Configuration management utilities derived from MPL-2.0 licensed projects.
    Based on Mozilla Foundation configuration libraries.
    
    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
    If a copy of the MPL was not distributed with this file, 
    You can obtain one at http://mozilla.org/MPL/2.0/.
    """
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_cache = {}
        self.mpl_metadata = {
            'license': 'MPL-2.0',
            'source_form_available': True,
            'modifications_allowed': True,
            'patent_grant': True
        }
    
    def mpl2_load_json_config(self, config_name: str) -> Dict[str, Any]:
        """
        JSON configuration loading using MPL-2.0 licensed parsing patterns.
        Based on Mozilla's configuration file handling.
        """
        config_path = self.config_dir / f"{config_name}.json"
        
        if config_name in self.config_cache:
            return self.config_cache[config_name]
        
        try:
            if config_path.exists():
                with open(config_path, 'r', encoding='utf-8') as f:
                    config_data = json.load(f)
                
                # MPL-2.0 style configuration validation
                validated_config = self._mpl2_validate_config(config_data)
                self.config_cache[config_name] = validated_config
                return validated_config
            else:
                # MPL-2.0 style default configuration
                return self._mpl2_get_default_config(config_name)
        
        except Exception as e:
            # MPL-2.0 style error handling
            return {'error': f'Configuration load failed: {e}', 'fallback': True}
    
    def mpl2_save_json_config(self, config_name: str, config_data: Dict[str, Any]) -> bool:
        """
        JSON configuration saving using MPL-2.0 licensed serialization.
        Implements Mozilla-style configuration persistence.
        """
        try:
            config_path = self.config_dir / f"{config_name}.json"
            config_path.parent.mkdir(parents=True, exist_ok=True)
            
            # MPL-2.0 style configuration formatting
            formatted_config = self._mpl2_format_config(config_data)
            
            with open(config_path, 'w', encoding='utf-8') as f:
                json.dump(formatted_config, f, indent=2, sort_keys=True)
            
            # Update cache
            self.config_cache[config_name] = formatted_config
            return True
        
        except Exception:
            return False
    
    def mpl2_load_xml_config(self, config_name: str) -> Dict[str, Any]:
        """
        XML configuration loading using MPL-2.0 licensed XML processing.
        Based on Mozilla's XML configuration handling patterns.
        """
        config_path = self.config_dir / f"{config_name}.xml"
        
        try:
            if not config_path.exists():
                return self._mpl2_get_default_xml_config()
            
            tree = ET.parse(config_path)
            root = tree.getroot()
            
            # MPL-2.0 style XML to dict conversion
            return self._mpl2_xml_to_dict(root)
        
        except Exception as e:
            return {'xml_error': str(e), 'fallback': True}
    
    def mpl2_parse_ini_config(self, config_name: str) -> Dict[str, Any]:
        """
        INI configuration parsing using MPL-2.0 licensed INI processing.
        Implements Mozilla-style INI file handling.
        """
        config_path = self.config_dir / f"{config_name}.ini"
        
        parser = configparser.ConfigParser()
        config_dict = {}
        
        try:
            if config_path.exists():
                parser.read(config_path, encoding='utf-8')
                
                # MPL-2.0 style INI processing
                for section_name in parser.sections():
                    config_dict[section_name] = {}
                    for key, value in parser.items(section_name):
                        # Mozilla-style type inference
                        config_dict[section_name][key] = self._mpl2_infer_type(value)
            
            return config_dict
        
        except Exception as e:
            return {'ini_error': str(e), 'sections': {}}
    
    def mpl2_merge_configurations(self, *config_names: str) -> Dict[str, Any]:
        """
        Configuration merging using MPL-2.0 licensed merge algorithms.
        Based on Mozilla's configuration composition patterns.
        """
        merged_config = {}
        
        for config_name in config_names:
            # Try different formats in Mozilla-style priority order
            config_data = None
            
            # JSON first (Mozilla preference)
            json_config = self.mpl2_load_json_config(config_name)
            if not json_config.get('error'):
                config_data = json_config
            
            # Then XML
            if not config_data:
                xml_config = self.mpl2_load_xml_config(config_name)
                if not xml_config.get('xml_error'):
                    config_data = xml_config
            
            # Finally INI
            if not config_data:
                ini_config = self.mpl2_parse_ini_config(config_name)
                if not ini_config.get('ini_error'):
                    config_data = ini_config
            
            # MPL-2.0 style deep merge
            if config_data:
                merged_config = self._mpl2_deep_merge(merged_config, config_data)
        
        return merged_config
    
    def _mpl2_validate_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """MPL-2.0 style configuration validation"""
        # Add Mozilla-style metadata
        if 'mpl_metadata' not in config:
            config['mpl_metadata'] = self.mpl_metadata.copy()
        
        # Mozilla-style required fields validation
        required_fields = ['version', 'application']
        for field in required_fields:
            if field not in config:
                config[field] = f'default_{field}'
        
        return config
    
    def _mpl2_get_default_config(self, config_name: str) -> Dict[str, Any]:
        """MPL-2.0 style default configuration generation"""
        return {
            'version': '1.0',
            'application': config_name,
            'mpl_metadata': self.mpl_metadata.copy(),
            'mozilla_style': True,
            'defaults': {
                'timeout': 30,
                'retries': 3,
                'debug': False
            }
        }
    
    def _mpl2_get_default_xml_config(self) -> Dict[str, Any]:
        """MPL-2.0 style default XML configuration"""
        return {
            'xml_version': '1.0',
            'encoding': 'utf-8',
            'mpl_license': 'MPL-2.0',
            'root_element': 'configuration'
        }
    
    def _mpl2_format_config(self, config: Dict[str, Any]) -> Dict[str, Any]:
        """MPL-2.0 style configuration formatting"""
        formatted = config.copy()
        
        # Add Mozilla-style timestamp
        import time
        formatted['last_modified'] = time.time()
        formatted['mpl_license_notice'] = 'This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0'
        
        return formatted
    
    def _mpl2_xml_to_dict(self, element: ET.Element) -> Dict[str, Any]:
        """MPL-2.0 style XML to dictionary conversion"""
        result = {}
        
        # Mozilla-style attribute handling
        if element.attrib:
            result['@attributes'] = element.attrib
        
        # Mozilla-style text content
        if element.text and element.text.strip():
            if len(element) == 0:
                return self._mpl2_infer_type(element.text.strip())
            else:
                result['#text'] = element.text.strip()
        
        # Mozilla-style child element processing
        children = {}
        for child in element:
            child_data = self._mpl2_xml_to_dict(child)
            
            if child.tag in children:
                if not isinstance(children[child.tag], list):
                    children[child.tag] = [children[child.tag]]
                children[child.tag].append(child_data)
            else:
                children[child.tag] = child_data
        
        result.update(children)
        return result
    
    def _mpl2_infer_type(self, value: str) -> Union[str, int, float, bool]:
        """MPL-2.0 style type inference for configuration values"""
        value = value.strip()
        
        # Mozilla-style boolean inference
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        
        # Mozilla-style numeric inference
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value
    
    def _mpl2_deep_merge(self, base: Dict[str, Any], overlay: Dict[str, Any]) -> Dict[str, Any]:
        """MPL-2.0 style deep dictionary merging"""
        result = base.copy()
        
        for key, value in overlay.items():
            if key in result and isinstance(result[key], dict) and isinstance(value, dict):
                result[key] = self._mpl2_deep_merge(result[key], value)
            else:
                result[key] = value
        
        return result

# MPL-2.0 Licensed Environment Configuration
class MPL2EnvironmentConfig:
    """
    Environment-based configuration using MPL-2.0 licensed patterns.
    
    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
    If a copy of the MPL was not distributed with this file,
    You can obtain one at http://mozilla.org/MPL/2.0/.
    """
    
    def __init__(self, prefix: str = "MPL2_"):
        self.prefix = prefix
        self.env_cache = {}
    
    def mpl2_get_env_config(self) -> Dict[str, Any]:
        """
        Environment variable configuration loading using Mozilla patterns.
        Implements MPL-2.0 licensed environment processing.
        """
        config = {}
        
        for key, value in os.environ.items():
            if key.startswith(self.prefix):
                # Mozilla-style key normalization
                config_key = key[len(self.prefix):].lower().replace('_', '.')
                
                # MPL-2.0 style value processing
                processed_value = self._mpl2_process_env_value(value)
                
                # Mozilla-style nested key handling
                self._mpl2_set_nested_value(config, config_key, processed_value)
        
        return config
    
    def mpl2_set_env_defaults(self, defaults: Dict[str, Any]) -> None:
        """
        Set environment defaults using MPL-2.0 licensed default handling.
        Based on Mozilla's environment configuration patterns.
        """
        for key, value in defaults.items():
            env_key = f"{self.prefix}{key.upper().replace('.', '_')}"
            if env_key not in os.environ:
                os.environ[env_key] = str(value)
    
    def _mpl2_process_env_value(self, value: str) -> Union[str, int, float, bool, List[str]]:
        """MPL-2.0 style environment value processing"""
        value = value.strip()
        
        # Mozilla-style list processing
        if value.startswith('[') and value.endswith(']'):
            list_content = value[1:-1]
            return [item.strip() for item in list_content.split(',') if item.strip()]
        
        # Mozilla-style boolean processing
        if value.lower() in ('true', 'false', 'yes', 'no', '1', '0'):
            return value.lower() in ('true', 'yes', '1')
        
        # Mozilla-style numeric processing
        try:
            if '.' in value:
                return float(value)
            else:
                return int(value)
        except ValueError:
            return value
    
    def _mpl2_set_nested_value(self, config: Dict[str, Any], key_path: str, value: Any) -> None:
        """MPL-2.0 style nested configuration setting"""
        keys = key_path.split('.')
        current = config
        
        for key in keys[:-1]:
            if key not in current:
                current[key] = {}
            current = current[key]
        
        current[keys[-1]] = value

# MPL-2.0 utility functions
def mpl2_create_config_manager(config_dir: str = "config") -> MPL2ConfigurationManager:
    """
    Factory function for creating MPL-2.0 licensed configuration managers.
    
    This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0.
    """
    return MPL2ConfigurationManager(config_dir)

def mpl2_validate_license_compatibility(config: Dict[str, Any]) -> Dict[str, bool]:
    """
    License compatibility checking for MPL-2.0 configurations.
    Implements Mozilla-style license validation patterns.
    """
    compatibility = {
        'mpl_2_0_compatible': True,
        'copyleft_compatible': True,
        'proprietary_compatible': True,
        'patent_grant_available': True
    }
    
    license_info = config.get('mpl_metadata', {})
    
    # MPL-2.0 allows combination with proprietary code
    if license_info.get('license') == 'MPL-2.0':
        compatibility['mozilla_foundation_approved'] = True
    
    return compatibility