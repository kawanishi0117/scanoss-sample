"""
Configuration settings for the web scraper.
Uses MIT licensed click library for CLI configuration.
"""

import click
import yaml
from pathlib import Path

class Config:
    def __init__(self):
        self.base_url = "https://example.com"
        self.timeout = 30
        self.max_retries = 3
        self.output_format = "json"
    
    @click.command()
    @click.option('--url', default='https://example.com', help='Base URL to scrape')
    @click.option('--timeout', default=30, help='Request timeout in seconds')
    @click.option('--output', default='json', help='Output format (json/csv)')
    def configure(self, url, timeout, output):
        self.base_url = url
        self.timeout = timeout
        self.output_format = output
        return self
    
    def load_from_yaml(self, config_path):
        """Load configuration from YAML file using PyYAML (MIT license)"""
        if Path(config_path).exists():
            with open(config_path, 'r') as f:
                config_data = yaml.safe_load(f)
                for key, value in config_data.items():
                    if hasattr(self, key):
                        setattr(self, key, value)
        return self

config = Config()