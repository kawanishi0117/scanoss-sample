"""
GPLv2 Licensed Network Tools Module
This module contains code derived from GPLv2 licensed projects for testing.

Copyright (C) 2023 Free Software Foundation, Inc.

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
"""

import socket
import time
import threading
import urllib.parse
from typing import List, Dict, Optional, Tuple
import subprocess
import os

# GPLv2 Licensed Network Scanner - Based on nmap-style scanning
class GPLv2NetworkScanner:
    """
    Network scanning utilities derived from GPLv2 licensed tools.
    This code is based on GPL-2.0 licensed network scanning utilities.
    
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License version 2.
    """
    
    def __init__(self):
        self.scan_results = []
        self.timeout = 5
        self.max_threads = 50
    
    def gpl2_port_scan(self, host: str, ports: List[int]) -> Dict[int, bool]:
        """
        Port scanning functionality derived from GPLv2 network tools.
        Based on GPL-2.0 licensed scanning algorithms.
        """
        results = {}
        threads = []
        
        def scan_port(host: str, port: int) -> None:
            """GPLv2-style port scanning function"""
            try:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(self.timeout)
                result = sock.connect_ex((host, port))
                results[port] = (result == 0)
                sock.close()
            except Exception:
                results[port] = False
        
        # GPL-style threaded scanning
        for port in ports:
            thread = threading.Thread(target=scan_port, args=(host, port))
            threads.append(thread)
            thread.start()
            
            # Limit concurrent threads (GPL-style resource management)
            if len(threads) >= self.max_threads:
                for t in threads:
                    t.join()
                threads = []
        
        # Wait for remaining threads
        for thread in threads:
            thread.join()
        
        return results
    
    def gpl2_host_discovery(self, network: str) -> List[str]:
        """
        Host discovery using GPLv2-style ping sweep.
        Implements GPL-2.0 licensed host enumeration techniques.
        """
        active_hosts = []
        
        # GPLv2-style network parsing
        try:
            # Simple subnet scanning (GPL implementation style)
            if '/' in network:
                base_ip = network.split('/')[0]
                ip_parts = base_ip.split('.')
                base = '.'.join(ip_parts[:3])
                
                # GPL-style host enumeration
                for i in range(1, 255):
                    host = f"{base}.{i}"
                    if self._gpl2_ping_host(host):
                        active_hosts.append(host)
            else:
                # Single host check
                if self._gpl2_ping_host(network):
                    active_hosts.append(network)
        
        except Exception:
            pass
        
        return active_hosts
    
    def _gpl2_ping_host(self, host: str) -> bool:
        """
        GPLv2-style ping implementation using system ping.
        Based on GPL-2.0 licensed ping utilities.
        """
        try:
            # GPL-style ping command
            ping_cmd = ['ping', '-c', '1', '-W', '1', host]
            result = subprocess.run(ping_cmd, capture_output=True, timeout=3)
            return result.returncode == 0
        except Exception:
            return False
    
    def gpl2_service_detection(self, host: str, port: int) -> Optional[str]:
        """
        Service detection based on GPLv2 licensed service fingerprinting.
        Uses GPL-2.0 style banner grabbing techniques.
        """
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(3)
            sock.connect((host, port))
            
            # GPL-style banner grabbing
            try:
                sock.send(b'GET / HTTP/1.0\r\n\r\n')
                banner = sock.recv(1024).decode('utf-8', errors='ignore')
                sock.close()
                
                # GPL-style service identification
                if 'HTTP' in banner:
                    return 'HTTP'
                elif 'SSH' in banner:
                    return 'SSH'
                elif 'FTP' in banner:
                    return 'FTP'
                else:
                    return 'Unknown'
            except:
                sock.close()
                return 'Filtered'
                
        except Exception:
            return None

# GPLv2 Licensed Protocol Handler
class GPLv2ProtocolHandler:
    """
    Protocol handling utilities derived from GPLv2 network libraries.
    
    This program is distributed under the GNU General Public License v2.0
    See COPYING file for full license text.
    """
    
    def __init__(self):
        self.protocols = {
            'http': 80,
            'https': 443,
            'ftp': 21,
            'ssh': 22,
            'telnet': 23,
            'smtp': 25,
            'dns': 53
        }
    
    def gpl2_parse_url(self, url: str) -> Dict[str, str]:
        """
        URL parsing using GPLv2-style parsing algorithms.
        Based on GPL-2.0 licensed URL handling libraries.
        """
        try:
            parsed = urllib.parse.urlparse(url)
            
            # GPL-style URL component extraction
            return {
                'scheme': parsed.scheme or 'http',
                'hostname': parsed.hostname or '',
                'port': str(parsed.port or self.protocols.get(parsed.scheme, 80)),
                'path': parsed.path or '/',
                'query': parsed.query or '',
                'fragment': parsed.fragment or ''
            }
        except Exception:
            return {}
    
    def gpl2_build_url(self, components: Dict[str, str]) -> str:
        """
        URL construction using GPLv2-style URL building.
        Implements GPL-2.0 licensed URL composition algorithms.
        """
        scheme = components.get('scheme', 'http')
        hostname = components.get('hostname', 'localhost')
        port = components.get('port', '')
        path = components.get('path', '/')
        query = components.get('query', '')
        fragment = components.get('fragment', '')
        
        # GPL-style URL assembly
        url = f"{scheme}://{hostname}"
        
        if port and port != str(self.protocols.get(scheme, 80)):
            url += f":{port}"
        
        url += path
        
        if query:
            url += f"?{query}"
        
        if fragment:
            url += f"#{fragment}"
        
        return url
    
    def gpl2_validate_protocol(self, protocol: str) -> bool:
        """GPLv2-style protocol validation"""
        return protocol.lower() in self.protocols

# GPLv2 utility functions for comprehensive testing
def gpl2_network_utils(host: str, timeout: int = 5) -> Dict[str, any]:
    """
    Network utility functions derived from GPLv2 licensed networking tools.
    
    This function is part of GPL-2.0 licensed software.
    You should have received a copy of the GNU General Public License
    along with this program; if not, see <http://www.gnu.org/licenses/>.
    """
    results = {
        'host': host,
        'reachable': False,
        'response_time': None,
        'resolved_ip': None
    }
    
    try:
        # GPL-style hostname resolution
        start_time = time.time()
        resolved_ip = socket.gethostbyname(host)
        resolution_time = time.time() - start_time
        
        results['resolved_ip'] = resolved_ip
        results['resolution_time'] = resolution_time
        
        # GPL-style connectivity test
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        
        start_time = time.time()
        connect_result = sock.connect_ex((resolved_ip, 80))
        response_time = time.time() - start_time
        
        sock.close()
        
        results['reachable'] = (connect_result == 0)
        results['response_time'] = response_time
        
    except Exception as e:
        results['error'] = str(e)
    
    return results

def gpl2_security_scan(target: str, scan_type: str = 'basic') -> Dict[str, any]:
    """
    Security scanning functionality based on GPLv2 licensed security tools.
    Implements GPL-2.0 style vulnerability assessment patterns.
    """
    scan_results = {
        'target': target,
        'scan_type': scan_type,
        'vulnerabilities': [],
        'open_ports': [],
        'services': {}
    }
    
    scanner = GPLv2NetworkScanner()
    
    # GPL-style basic port scan
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995]
    port_results = scanner.gpl2_port_scan(target, common_ports)
    
    for port, is_open in port_results.items():
        if is_open:
            scan_results['open_ports'].append(port)
            service = scanner.gpl2_service_detection(target, port)
            if service:
                scan_results['services'][port] = service
    
    # GPL-style vulnerability checks
    if 21 in scan_results['open_ports']:
        scan_results['vulnerabilities'].append('FTP service detected')
    
    if 23 in scan_results['open_ports']:
        scan_results['vulnerabilities'].append('Telnet service detected (insecure)')
    
    return scan_results