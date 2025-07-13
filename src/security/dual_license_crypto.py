"""
デュアルライセンス暗号化モジュール
このモジュールは意図的に複数のライセンス選択肢を提供し、ライセンス検出の複雑性をテストします。

警告: これはテスト目的のモジュールで、意図的にライセンス競合を含んでいます。
本番環境では使用しないでください。
"""

# ============================================================================
# デュアルライセンス: GPL-3.0 OR Commercial
# ============================================================================

"""
Dual License Option 1: GPL-3.0

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

----

Dual License Option 2: Commercial License

For commercial use, this software is available under a separate commercial
license. Contact licensing@example.com for commercial licensing terms.

Commercial License Terms:
- Proprietary use permitted
- No source code disclosure required
- Commercial distribution allowed
- No GPL obligations
- License fee required
"""

import hashlib
import secrets
import os
from typing import Optional, Dict, Any
import base64

class DualLicenseCrypto:
    """
    デュアルライセンス暗号化クラス
    GPL-3.0または商用ライセンスで利用可能
    
    このクラスは意図的にライセンス検出の複雑性をテストするために
    複数のライセンス選択肢を持っています。
    """
    
    def __init__(self, commercial_license: bool = False):
        """
        初期化メソッド
        
        Args:
            commercial_license: 商用ライセンス使用フラグ
        """
        self.commercial_mode = commercial_license
        self.algorithm = "AES-256"
        
        if commercial_license:
            # 商用ライセンス機能
            self._initialize_commercial_features()
        else:
            # GPL機能のみ
            self._initialize_gpl_features()
    
    def _initialize_commercial_features(self):
        """商用ライセンス限定機能の初期化"""
        self.enhanced_encryption = True
        self.hardware_acceleration = True
        self.priority_support = True
        
        # 商用ライセンス通知
        print("商用ライセンス機能が有効化されました")
        print("拡張暗号化サポート、ハードウェアアクセラレーション利用可能")
    
    def _initialize_gpl_features(self):
        """GPL基本機能の初期化"""
        self.enhanced_encryption = False
        self.hardware_acceleration = False
        self.priority_support = False
        
        print("GPL-3.0基本機能で初期化されました")
        print("全ての機能はGPL-3.0ライセンス条件下で利用可能です")
    
    def encrypt_data(self, plaintext: str, key: Optional[str] = None) -> Dict[str, str]:
        """
        データ暗号化メソッド（両ライセンスで利用可能）
        
        GPL機能: 基本的なハッシュベース暗号化
        商用機能: 拡張暗号化アルゴリズム（商用ライセンスが必要）
        """
        if not key:
            key = secrets.token_hex(32)
        
        if self.commercial_mode and self.enhanced_encryption:
            # 商用ライセンス限定: 拡張暗号化
            return self._commercial_encrypt(plaintext, key)
        else:
            # GPL基本暗号化
            return self._gpl_encrypt(plaintext, key)
    
    def _gpl_encrypt(self, plaintext: str, key: str) -> Dict[str, str]:
        """
        GPL-3.0基本暗号化実装
        
        この機能はGPL-3.0ライセンス下で提供されます。
        ソースコード開示義務があります。
        """
        # 簡易的なXOR暗号化（GPL実装）
        plaintext_bytes = plaintext.encode('utf-8')
        key_bytes = key.encode('utf-8')
        
        # キーを平文の長さに拡張
        extended_key = (key_bytes * (len(plaintext_bytes) // len(key_bytes) + 1))[:len(plaintext_bytes)]
        
        # XOR演算
        encrypted = bytes(a ^ b for a, b in zip(plaintext_bytes, extended_key))
        
        result = {
            'encrypted_data': base64.b64encode(encrypted).decode('utf-8'),
            'algorithm': 'XOR-GPL',
            'license': 'GPL-3.0',
            'key_hint': key[:8] + '...',
            'note': 'GPL基本暗号化 - ソースコード開示必須'
        }
        
        return result
    
    def _commercial_encrypt(self, plaintext: str, key: str) -> Dict[str, str]:
        """
        商用ライセンス限定の拡張暗号化
        
        この機能は商用ライセンスが必要です。
        プロプライエタリアルゴリズムを使用します。
        """
        # より強力な暗号化（商用ライセンス限定）
        import hmac
        
        # ハッシュベース暗号化
        key_hash = hashlib.sha256(key.encode()).digest()
        plaintext_bytes = plaintext.encode('utf-8')
        
        # HMAC署名付き暗号化
        signature = hmac.new(key_hash, plaintext_bytes, hashlib.sha256).digest()
        
        # 複合的な暗号化処理
        encrypted = bytearray()
        for i, byte in enumerate(plaintext_bytes):
            encrypted.append(byte ^ key_hash[i % len(key_hash)] ^ signature[i % len(signature)])
        
        result = {
            'encrypted_data': base64.b64encode(encrypted).decode('utf-8'),
            'signature': base64.b64encode(signature).decode('utf-8'),
            'algorithm': 'HMAC-SHA256-COMMERCIAL',
            'license': 'Commercial',
            'key_hint': hashlib.md5(key.encode()).hexdigest()[:8],
            'note': '商用ライセンス拡張暗号化 - プロプライエタリ'
        }
        
        return result
    
    def get_license_info(self) -> Dict[str, Any]:
        """
        現在のライセンス情報を取得
        
        デュアルライセンスの状態と利用可能な機能を返します。
        """
        if self.commercial_mode:
            return {
                'active_license': 'Commercial',
                'gpl_obligations': False,
                'source_disclosure_required': False,
                'commercial_use_permitted': True,
                'enhanced_features': True,
                'support_level': 'Priority',
                'license_fee': 'Required',
                'patent_protection': True
            }
        else:
            return {
                'active_license': 'GPL-3.0',
                'gpl_obligations': True,
                'source_disclosure_required': True,
                'commercial_use_permitted': True,
                'enhanced_features': False,
                'support_level': 'Community',
                'license_fee': 'None',
                'patent_protection': False,
                'copyleft_requirements': True
            }

# ============================================================================
# トリプルライセンス暗号化ユーティリティ
# ============================================================================

"""
Triple License Choice: MIT OR Apache-2.0 OR BSD-3-Clause

Option 1 - MIT License:
Copyright (c) 2023 Triple License Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to deal in the Software without restriction.

Option 2 - Apache License 2.0:
Licensed under the Apache License, Version 2.0.
See http://www.apache.org/licenses/LICENSE-2.0

Option 3 - BSD 3-Clause License:
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that conditions are met.
"""

def triple_license_hash(data: str, license_choice: str = 'MIT') -> Dict[str, str]:
    """
    トリプルライセンスハッシュ関数
    
    MIT、Apache-2.0、またはBSD-3-Clauseライセンスから選択可能
    異なるライセンス選択により微妙に異なる実装を提供
    
    Args:
        data: ハッシュ化するデータ
        license_choice: ライセンス選択 ('MIT', 'Apache-2.0', 'BSD-3-Clause')
    """
    if license_choice == 'MIT':
        # MIT実装: シンプルなSHA256
        hash_value = hashlib.sha256(data.encode()).hexdigest()
        return {
            'hash': hash_value,
            'algorithm': 'SHA256-MIT',
            'license': 'MIT',
            'attribution_required': True,
            'patent_grant': False
        }
    
    elif license_choice == 'Apache-2.0':
        # Apache実装: ソルト付きハッシュ
        salt = hashlib.md5(data.encode()).hexdigest()[:16]
        salted_data = salt + data + salt
        hash_value = hashlib.sha256(salted_data.encode()).hexdigest()
        return {
            'hash': hash_value,
            'salt': salt,
            'algorithm': 'SHA256-SALTED-APACHE',
            'license': 'Apache-2.0',
            'attribution_required': True,
            'patent_grant': True,
            'notice_file_required': True
        }
    
    elif license_choice == 'BSD-3-Clause':
        # BSD実装: ダブルハッシュ
        first_hash = hashlib.sha256(data.encode()).hexdigest()
        second_hash = hashlib.sha256(first_hash.encode()).hexdigest()
        return {
            'hash': second_hash,
            'intermediate_hash': first_hash,
            'algorithm': 'SHA256-DOUBLE-BSD',
            'license': 'BSD-3-Clause',
            'attribution_required': True,
            'patent_grant': False,
            'endorsement_prohibited': True
        }
    
    else:
        raise ValueError(f"サポートされていないライセンス選択: {license_choice}")

# ============================================================================
# ライセンス競合シミュレーションクラス
# ============================================================================

class LicenseConflictSimulator:
    """
    ライセンス競合をシミュレートするクラス
    
    このクラスは意図的に互換性のないライセンスを組み合わせて
    ライセンス検出ツールのテストを行います。
    """
    
    def __init__(self):
        self.licenses_in_use = []
        self.conflicts_detected = []
    
    def add_gpl_component(self):
        """
        GPL-3.0コンポーネントを追加
        
        GPLコンポーネントはコピーレフト要求を持ちます。
        """
        # GPL-3.0 Licensed Code Fragment
        """
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License.
        """
        self.licenses_in_use.append('GPL-3.0')
        self._check_conflicts()
        return "GPL-3.0コンポーネントが追加されました（コピーレフト要求あり）"
    
    def add_proprietary_component(self):
        """
        プロプライエタリコンポーネントを追加
        
        プロプライエタリライセンスはソースコード開示を禁止します。
        """
        # Proprietary License Notice
        """
        PROPRIETARY AND CONFIDENTIAL
        This software is proprietary to Example Corp.
        Distribution or modification is strictly prohibited.
        All rights reserved.
        """
        self.licenses_in_use.append('Proprietary')
        self._check_conflicts()
        return "プロプライエタリコンポーネントが追加されました（ソース開示禁止）"
    
    def add_apache_component(self):
        """
        Apache-2.0コンポーネントを追加
        
        Apacheライセンスは特許保護を提供します。
        """
        # Apache License Notice
        """
        Licensed under the Apache License, Version 2.0 (the "License");
        you may not use this file except in compliance with the License.
        Grant of Patent License: Subject to terms, each Contributor grants
        a perpetual, worldwide, non-exclusive, no-charge, royalty-free,
        irrevocable patent license.
        """
        self.licenses_in_use.append('Apache-2.0')
        self._check_conflicts()
        return "Apache-2.0コンポーネントが追加されました（特許保護あり）"
    
    def _check_conflicts(self):
        """ライセンス競合をチェック"""
        # GPL vs Proprietary (重大な競合)
        if 'GPL-3.0' in self.licenses_in_use and 'Proprietary' in self.licenses_in_use:
            conflict = {
                'type': '重大な競合',
                'licenses': ['GPL-3.0', 'Proprietary'],
                'issue': 'GPLのコピーレフト要求とプロプライエタリの開示禁止が競合',
                'resolution': 'どちらか一方のライセンスを選択する必要があります'
            }
            if conflict not in self.conflicts_detected:
                self.conflicts_detected.append(conflict)
        
        # Apache vs GPL (特許条項の競合可能性)
        if 'Apache-2.0' in self.licenses_in_use and 'GPL-3.0' in self.licenses_in_use:
            conflict = {
                'type': '軽微な競合',
                'licenses': ['Apache-2.0', 'GPL-3.0'],
                'issue': 'Apache特許条項とGPL要求の相互作用',
                'resolution': 'GPL-3.0互換性確認が必要'
            }
            if conflict not in self.conflicts_detected:
                self.conflicts_detected.append(conflict)
    
    def get_conflict_report(self) -> Dict[str, Any]:
        """ライセンス競合レポートを生成"""
        return {
            'licenses_detected': self.licenses_in_use,
            'conflicts_found': len(self.conflicts_detected),
            'conflict_details': self.conflicts_detected,
            'risk_level': self._calculate_risk_level(),
            'recommendations': self._generate_recommendations()
        }
    
    def _calculate_risk_level(self) -> str:
        """リスクレベルを計算"""
        if not self.conflicts_detected:
            return 'LOW'
        
        serious_conflicts = sum(1 for c in self.conflicts_detected if c['type'] == '重大な競合')
        
        if serious_conflicts > 0:
            return 'CRITICAL'
        elif len(self.conflicts_detected) > 2:
            return 'HIGH'
        else:
            return 'MEDIUM'
    
    def _generate_recommendations(self) -> list:
        """推奨事項を生成"""
        recommendations = []
        
        if 'GPL-3.0' in self.licenses_in_use and 'Proprietary' in self.licenses_in_use:
            recommendations.append("GPLとプロプライエタリライセンスは共存できません")
            recommendations.append("デュアルライセンス戦略を検討してください")
        
        if len(set(self.licenses_in_use)) > 3:
            recommendations.append("ライセンス数が多すぎます - 統合を検討してください")
        
        if not recommendations:
            recommendations.append("現在のライセンス構成は概ね問題ありません")
        
        return recommendations

# ============================================================================
# ライセンス継承シミュレーション
# ============================================================================

def simulate_license_inheritance() -> Dict[str, Any]:
    """
    ライセンス継承の複雑なパターンをシミュレート
    
    複数レベルの依存関係とライセンス継承を模擬します。
    """
    
    # 依存関係ツリー
    dependency_tree = {
        'root_project': {
            'license': 'MIT',
            'dependencies': {
                'gpl_library': {
                    'license': 'GPL-3.0',
                    'dependencies': {
                        'lgpl_component': {'license': 'LGPL-2.1'},
                        'apache_utility': {'license': 'Apache-2.0'}
                    }
                },
                'proprietary_module': {
                    'license': 'Commercial-Proprietary',
                    'dependencies': {
                        'bsd_helper': {'license': 'BSD-3-Clause'}
                    }
                },
                'creative_commons_data': {
                    'license': 'CC-BY-SA-4.0',
                    'dependencies': {}
                }
            }
        }
    }
    
    # ライセンス継承ルール
    inheritance_rules = {
        'GPL-3.0': 'すべての派生作品にGPL-3.0を強制',
        'LGPL-2.1': '動的リンクは許可、静的リンクはLGPL継承',
        'MIT': 'ライセンス継承なし、互換性高',
        'Apache-2.0': '特許保護付き、GPL互換性注意',
        'Commercial-Proprietary': 'ライセンス継承禁止、商用のみ',
        'CC-BY-SA-4.0': 'ShareAlike要求、同じライセンス強制'
    }
    
    # 継承解析
    analysis_result = {
        'dependency_structure': dependency_tree,
        'inheritance_rules': inheritance_rules,
        'effective_license': 'GPL-3.0（最も制限的なライセンスが適用）',
        'license_conflicts': [
            'GPL-3.0 vs Commercial-Proprietary: 重大な競合',
            'CC-BY-SA-4.0 vs GPL-3.0: ShareAlike要求の競合',
            'Apache-2.0 vs GPL-3.0: 特許条項の相互作用'
        ],
        'compliance_requirements': [
            'GPLライセンステキストの同梱必須',
            'ソースコード提供義務',
            'プロプライエタリモジュールの除去が必要',
            'Creative Commons素材の適切な帰属表示'
        ],
        'risk_assessment': {
            'legal_risk': 'CRITICAL',
            'compliance_complexity': 'VERY HIGH',
            'commercial_viability': 'BLOCKED'
        }
    }
    
    return analysis_result

# テスト実行例
if __name__ == "__main__":
    print("=== デュアルライセンス暗号化テスト ===")
    
    # GPL版テスト
    gpl_crypto = DualLicenseCrypto(commercial_license=False)
    gpl_result = gpl_crypto.encrypt_data("テストデータ GPL版")
    print(f"GPL暗号化結果: {gpl_result}")
    
    # 商用版テスト
    commercial_crypto = DualLicenseCrypto(commercial_license=True)
    commercial_result = commercial_crypto.encrypt_data("テストデータ 商用版")
    print(f"商用暗号化結果: {commercial_result}")
    
    print("\n=== ライセンス競合シミュレーション ===")
    simulator = LicenseConflictSimulator()
    simulator.add_gpl_component()
    simulator.add_proprietary_component()
    simulator.add_apache_component()
    
    conflict_report = simulator.get_conflict_report()
    print(f"競合レポート: {conflict_report}")
    
    print("\n=== ライセンス継承シミュレーション ===")
    inheritance_analysis = simulate_license_inheritance()
    print(f"継承解析: {inheritance_analysis['effective_license']}")