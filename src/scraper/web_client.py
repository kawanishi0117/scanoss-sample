"""
Web client module containing GPL-3.0 licensed code for testing.
This code is intentionally included to test SCANOSS GPL detection.
"""

import urllib.request
import urllib.parse
import socket
from typing import Optional, Dict

# GPL-3.0 Licensed Code Below - Simulated wget functionality
# This is test code derived from GPL-3.0 sources for license detection

class HTTPDownloader:
    """
    HTTP downloader with GPL-3.0 features.
    Based on GPL-3.0 licensed wget-like functionality.
    
    Copyright (C) Test GPL Code
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.
    """
    
    def __init__(self):
        self.user_agent = "GPL-Downloader/1.0"
        self.timeout = 30
        self.max_redirects = 5
    
    def download_with_retries(self, url: str, retries: int = 3) -> Optional[bytes]:
        """
        Download content with retry logic - GPL-3.0 style implementation
        """
        for attempt in range(retries + 1):
            try:
                return self._perform_download(url)
            except Exception as e:
                if attempt == retries:
                    return None
                continue
        return None
    
    def _perform_download(self, url: str) -> bytes:
        """
        Core download functionality derived from GPL-3.0 sources
        """
        req = urllib.request.Request(url)
        req.add_header('User-Agent', self.user_agent)
        
        # GPL-style connection handling
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return response.read()
        except urllib.error.URLError:
            raise
    
    def check_connectivity(self, host: str, port: int = 80) -> bool:
        """
        Network connectivity check - GPL implementation style
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception:
            return False

# Additional GPL-3.0 utility functions for license testing
def gpl_url_validator(url: str) -> bool:
    """
    URL validation function using GPL-3.0 style implementation
    
    This function contains code patterns typical of GPL-3.0 licensed software
    for comprehensive license detection testing.
    """
    if not url or not isinstance(url, str):
        return False
    
    # GPL-style URL parsing and validation
    try:
        parsed = urllib.parse.urlparse(url)
        return all([parsed.scheme, parsed.netloc])
    except Exception:
        return False

def gpl_content_processor(content: bytes) -> Dict[str, str]:
    """
    Content processing with GPL-3.0 derived algorithms
    """
    if not content:
        return {}
    
    # Decode content using GPL-style error handling
    try:
        text = content.decode('utf-8', errors='replace')
    except Exception:
        text = str(content)
    
    return {
        'size': str(len(content)),
        'encoding': 'utf-8',
        'preview': text[:100] if text else ''
    }