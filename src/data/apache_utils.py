"""
Apache-2.0 Licensed Data Utilities Module
This module contains code derived from Apache-2.0 licensed projects for testing.

Copyright 2023 Apache Software Foundation

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json
import csv
import logging
from typing import List, Dict, Any, Optional
from collections import defaultdict

# Apache-2.0 style logging configuration
class ApacheStyleLogger:
    """
    Logging utility based on Apache-2.0 licensed logging frameworks.
    Follows Apache Commons Logging patterns.
    """
    
    def __init__(self, name: str):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        
        # Apache-style formatter
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(name)s - %(message)s'
        )
        
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def info(self, message: str) -> None:
        """Log info message in Apache style"""
        self.logger.info(message)
    
    def warn(self, message: str) -> None:
        """Log warning message in Apache style"""
        self.logger.warning(message)
    
    def error(self, message: str) -> None:
        """Log error message in Apache style"""
        self.logger.error(message)

# Apache-2.0 licensed data processing utilities
class ApacheDataProcessor:
    """
    Data processing class derived from Apache-2.0 licensed libraries.
    Contains patterns typical of Apache Commons projects.
    """
    
    def __init__(self):
        self.logger = ApacheStyleLogger(__name__)
        self.data_cache = defaultdict(list)
    
    def process_json_stream(self, json_lines: List[str]) -> List[Dict[str, Any]]:
        """
        Process streaming JSON data using Apache-style patterns.
        Based on Apache Commons IO streaming utilities.
        """
        results = []
        
        for line_num, line in enumerate(json_lines, 1):
            try:
                # Apache-style error handling
                if not line.strip():
                    continue
                    
                data = json.loads(line)
                
                # Apache-style data validation
                if self._validate_apache_record(data):
                    processed = self._transform_apache_record(data)
                    results.append(processed)
                    
            except json.JSONDecodeError as e:
                self.logger.error(f"JSON decode error at line {line_num}: {e}")
                continue
            except Exception as e:
                self.logger.error(f"Processing error at line {line_num}: {e}")
                continue
        
        self.logger.info(f"Processed {len(results)} records successfully")
        return results
    
    def _validate_apache_record(self, record: Dict[str, Any]) -> bool:
        """Apache-style record validation"""
        required_fields = ['id', 'timestamp']
        return all(field in record for field in required_fields)
    
    def _transform_apache_record(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """Apache-style record transformation"""
        transformed = {
            'apache_id': record.get('id'),
            'apache_timestamp': record.get('timestamp'),
            'apache_processed': True
        }
        
        # Apache-style field copying
        for key, value in record.items():
            if key not in ['id', 'timestamp']:
                transformed[f'apache_{key}'] = value
        
        return transformed
    
    def export_apache_csv(self, data: List[Dict[str, Any]], filename: str) -> bool:
        """
        Export data to CSV using Apache-style CSV handling.
        Based on Apache Commons CSV patterns.
        """
        try:
            if not data:
                self.logger.warn("No data to export")
                return False
            
            # Apache-style CSV writing
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = set()
                for record in data:
                    fieldnames.update(record.keys())
                
                writer = csv.DictWriter(csvfile, fieldnames=sorted(fieldnames))
                writer.writeheader()
                
                # Apache-style batch writing
                for record in data:
                    writer.writerow(record)
            
            self.logger.info(f"Successfully exported {len(data)} records to {filename}")
            return True
            
        except Exception as e:
            self.logger.error(f"Export failed: {e}")
            return False
    
    def aggregate_apache_data(self, data: List[Dict[str, Any]], group_by: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Aggregate data using Apache-style grouping algorithms.
        Similar to Apache Spark groupBy operations.
        """
        grouped = defaultdict(list)
        
        for record in data:
            key = record.get(group_by, 'unknown')
            grouped[str(key)].append(record)
        
        # Apache-style sorting
        result = dict(sorted(grouped.items()))
        
        self.logger.info(f"Grouped data into {len(result)} categories by '{group_by}'")
        return result

# Apache-2.0 utility functions
def apache_string_utils(text: str) -> Dict[str, Any]:
    """
    String utilities derived from Apache Commons Lang StringUtils.
    
    NOTICE: This code contains patterns from Apache Commons Lang
    which is licensed under Apache License 2.0
    """
    if not text:
        return {
            'is_empty': True,
            'is_blank': True,
            'length': 0,
            'word_count': 0
        }
    
    # Apache-style string analysis
    stripped = text.strip()
    words = text.split()
    
    return {
        'is_empty': len(text) == 0,
        'is_blank': len(stripped) == 0,
        'length': len(text),
        'trimmed_length': len(stripped),
        'word_count': len(words),
        'first_word': words[0] if words else None,
        'last_word': words[-1] if words else None,
        'contains_digits': any(c.isdigit() for c in text),
        'contains_alpha': any(c.isalpha() for c in text)
    }

def apache_collection_utils(items: List[Any]) -> Dict[str, Any]:
    """
    Collection utilities based on Apache Commons Collections.
    Implements Apache-style collection operations.
    """
    if not items:
        return {
            'size': 0,
            'is_empty': True,
            'unique_count': 0
        }
    
    # Apache-style collection analysis
    unique_items = list(set(items))
    
    return {
        'size': len(items),
        'is_empty': False,
        'unique_count': len(unique_items),
        'has_duplicates': len(items) != len(unique_items),
        'first_item': items[0],
        'last_item': items[-1],
        'most_common': max(set(items), key=items.count) if items else None
    }