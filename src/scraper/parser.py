"""
HTML parsing module using BeautifulSoup (MIT license).
"""

from bs4 import BeautifulSoup
import requests
from typing import List, Dict, Optional

class WebParser:
    def __init__(self, user_agent: str = "SCANOSS-Test-Bot/1.0"):
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': user_agent})
    
    def fetch_page(self, url: str) -> Optional[str]:
        """Fetch webpage content using requests library (Apache-2.0)"""
        try:
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException:
            return None
    
    def parse_html(self, html_content: str) -> BeautifulSoup:
        """Parse HTML content using BeautifulSoup (MIT license)"""
        return BeautifulSoup(html_content, 'html.parser')
    
    def extract_links(self, soup: BeautifulSoup) -> List[Dict[str, str]]:
        """Extract all links from parsed HTML"""
        links = []
        for link in soup.find_all('a', href=True):
            links.append({
                'url': link['href'],
                'text': link.get_text(strip=True)
            })
        return links
    
    def extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract clean text content from HTML"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        # Get text and clean it up
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def extract_metadata(self, soup: BeautifulSoup) -> Dict[str, str]:
        """Extract metadata from HTML head section"""
        metadata = {}
        
        # Extract title
        title = soup.find('title')
        if title:
            metadata['title'] = title.get_text(strip=True)
        
        # Extract meta tags
        for meta in soup.find_all('meta'):
            name = meta.get('name') or meta.get('property')
            content = meta.get('content')
            if name and content:
                metadata[name] = content
        
        return metadata