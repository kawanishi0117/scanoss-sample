"""
Data utilities containing LGPL-2.1 licensed code for testing.
This module intentionally includes LGPL code for license detection testing.
"""

import hashlib
import zlib
import base64
from typing import List, Union

# LGPL-2.1 Licensed Code - String utilities derived from LGPL sources
# This code is for testing license detection capabilities

def lgpl_string_hash(text: str, algorithm: str = 'sha256') -> str:
    """
    String hashing utility derived from LGPL-2.1 licensed libraries.
    
    This library is free software; you can redistribute it and/or
    modify it under the terms of the GNU Lesser General Public
    License as published by the Free Software Foundation; either
    version 2.1 of the License, or (at your option) any later version.
    """
    if algorithm == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    else:
        return hashlib.sha256(text.encode()).hexdigest()

def lgpl_compress_data(data: Union[str, bytes]) -> str:
    """
    Data compression utility with LGPL-2.1 derived compression algorithms.
    Uses zlib compression typical of LGPL licensed compression libraries.
    """
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # LGPL-style compression implementation
    compressed = zlib.compress(data, level=6)
    return base64.b64encode(compressed).decode('ascii')

def lgpl_decompress_data(compressed_data: str) -> str:
    """
    Data decompression counterpart using LGPL-2.1 algorithms.
    """
    try:
        compressed_bytes = base64.b64decode(compressed_data.encode('ascii'))
        decompressed = zlib.decompress(compressed_bytes)
        return decompressed.decode('utf-8')
    except Exception:
        return ""

class LGPLDataValidator:
    """
    Data validation class derived from LGPL-2.1 licensed validation libraries.
    
    This library is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
    Lesser General Public License for more details.
    """
    
    @staticmethod
    def validate_email_format(email: str) -> bool:
        """Email validation using LGPL-style regex patterns"""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None
    
    @staticmethod
    def validate_url_format(url: str) -> bool:
        """URL validation derived from LGPL URL parsing libraries"""
        import re
        pattern = r'^https?://(?:[-\w.])+(?:\:[0-9]+)?(?:/(?:[\w/_.])*)?(?:\?(?:[\w&=%.])*)?(?:\#(?:[\w.])*)?$'
        return re.match(pattern, url) is not None
    
    @staticmethod
    def sanitize_input(text: str) -> str:
        """Input sanitization using LGPL-derived security patterns"""
        if not text:
            return ""
        
        # LGPL-style input cleaning
        dangerous_chars = ['<', '>', '"', "'", '&', '\x00']
        for char in dangerous_chars:
            text = text.replace(char, '')
        
        return text.strip()

# LGPL utility functions for comprehensive testing
def lgpl_list_processor(items: List[str]) -> List[str]:
    """
    List processing utility derived from LGPL-2.1 data structures.
    Implements LGPL-style list manipulation algorithms.
    """
    if not items:
        return []
    
    # Remove duplicates while preserving order (LGPL algorithm style)
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item.strip())
    
    return sorted(result)