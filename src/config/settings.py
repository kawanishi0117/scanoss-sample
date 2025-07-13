"""
設定管理モジュール - 複数ライセンスとライブラリの依存関係テスト用

このモジュールは意図的に多様なライセンスのライブラリを使用して
ライセンス検出の複雑性をテストします。

ライセンス情報:
- click: BSD-3-Clause
- PyYAML: MIT
- pathlib: Python Software Foundation License (PSFL)
- configparser: PSFL
- toml: MIT (Python 3.11+)
- json: PSFL (標準ライブラリ)

追加ライセンス依存関係:
- cryptography: Apache-2.0 OR BSD-3-Clause (デュアルライセンス)
- requests: Apache-2.0
- certifi: MPL-2.0 (Mozilla Public License)
"""

import click
import yaml
import json
import configparser
import os
from pathlib import Path
from typing import Dict, Any, Optional
import hashlib
import base64

# 追加ライセンステスト用のインポート
try:
    import tomllib  # Python 3.11+ (PSFL)
except ImportError:
    try:
        import tomli as tomllib  # MIT (fallback)
    except ImportError:
        tomllib = None

# 暗号化ライブラリ (Apache-2.0/BSD-3-Clause デュアルライセンス)
try:
    from cryptography.fernet import Fernet
    CRYPTO_AVAILABLE = True
except ImportError:
    CRYPTO_AVAILABLE = False

class Config:
    """
    設定管理クラス
    
    多様なライセンスのライブラリを使用した設定管理システムです。
    ライセンス検出ツールのテスト用に意図的に複雑な依存関係を持ちます。
    """
    
    def __init__(self):
        self.base_url = "https://example.com"
        self.timeout = 30
        self.max_retries = 3
        self.output_format = "json"
        self.encryption_enabled = CRYPTO_AVAILABLE
        
        # 日本語設定項目
        self.アプリケーション名 = "スキャンOSSテストプロジェクト"
        self.作成者 = "ライセンステスト開発チーム"
        self.バージョン = "1.0.0"
        
        # ライセンス追跡用
        self.使用ライブラリ = {
            'click': 'BSD-3-Clause',
            'PyYAML': 'MIT', 
            'pathlib': 'PSFL',
            'configparser': 'PSFL',
            'json': 'PSFL',
            'cryptography': 'Apache-2.0 OR BSD-3-Clause',
            'tomllib': 'PSFL または MIT'
        }
    
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