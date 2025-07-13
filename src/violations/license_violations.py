"""
ライセンス違反シミュレーションモジュール
このモジュールは意図的にライセンス違反パターンを含んでいます。

警告: これはライセンス検出テスト専用です。
実際のプロジェクトでは絶対に使用しないでください。
"""

# ============================================================================
# 故意のライセンス違反パターン #1: GPLコードの無許可商用利用
# ============================================================================

"""
Original GPL-3.0 Licensed Code (Violation Pattern)

This code is derived from GPL-3.0 licensed software but being used
in proprietary commercial software without GPL compliance.

VIOLATION: Using GPL code in proprietary software without:
1. Making source code available
2. Including GPL license text
3. Maintaining GPL license for derivative works

Original GPL Notice:
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License.

PROPRIETARY VIOLATION NOTICE:
Copyright (c) 2023 ProprietaryCorp. All rights reserved.
This code is proprietary and confidential.
Distribution is strictly prohibited.
"""

def stolen_gpl_algorithm(data: list) -> dict:
    """
    GPL-3.0ライセンスコードの無許可商用利用例
    
    このアルゴリズムはGPL-3.0ライセンスのコードから派生していますが、
    プロプライエタリソフトウェアで無許可使用されています。
    
    ライセンス違反内容:
    - GPLソースコードの開示義務違反
    - ライセンス表示の除去
    - 派生著作物のGPLライセンス継承違反
    """
    # GPL由来のソートアルゴリズム（無許可商用利用）
    if not data:
        return {'error': 'データなし'}
    
    # クイックソートアルゴリズム（GPL由来）
    def quicksort_gpl_violation(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort_gpl_violation(left) + middle + quicksort_gpl_violation(right)
    
    sorted_data = quicksort_gpl_violation(data)
    
    return {
        'sorted_data': sorted_data,
        'algorithm': 'QuickSort (GPL違反)',
        'original_license': 'GPL-3.0 (違反)',
        'current_claim': 'Proprietary (不正)',
        'violation_type': 'GPL商用利用ライセンス違反',
        'legal_risk': '極めて高い',
        'gpl_obligations_ignored': [
            'ソースコード開示義務',
            'GPLライセンステキスト同梱義務',
            '派生著作物のGPLライセンス継承義務'
        ]
    }

# ============================================================================
# 故意のライセンス違反パターン #2: 著作権表示の無断削除
# ============================================================================

"""
VIOLATION: Copyright Notice Removal

Original MIT License code with copyright notice removed.

ORIGINAL NOTICE (REMOVED ILLEGALLY):
Copyright (c) 2023 Original Author <original@example.com>

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

VIOLATION: The above copyright notice was illegally removed.
"""

def copyright_stripped_function(text: str) -> str:
    """
    著作権表示が不正に削除された関数
    
    元のMITライセンスコードから著作権表示とライセンス条項が
    不正に削除されています。
    
    違反内容:
    - 著作権表示の無断削除
    - ライセンス条項の除去
    - 帰属表示義務の無視
    """
    # 元のMITライセンスコードから著作権を削除
    processed = text.upper()
    processed = processed.replace(' ', '_')
    
    return processed  # 著作権表示なしで返却（違反）

# ============================================================================
# 故意のライセンス違反パターン #3: 非互換ライセンスの組み合わせ
# ============================================================================

class IncompatibleLicenseMixer:
    """
    非互換ライセンス混合クラス
    
    互換性のないライセンスを意図的に組み合わせて
    ライセンス違反を発生させています。
    """
    
    def __init__(self):
        # GPL-3.0 + Proprietary の非互換組み合わせ
        self.gpl_component = "GPL-3.0コンポーネント（コピーレフト要求）"
        self.proprietary_component = "プロプライエタリコンポーネント（ソース開示禁止）"
        
    def violate_license_compatibility(self):
        """
        ライセンス互換性違反メソッド
        
        GPLのコピーレフト要求とプロプライエタリライセンスの
        ソース開示禁止要求が直接競合しています。
        """
        # GPL-3.0ライセンス部分
        """
        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License version 3.
        
        GPL要求: すべての派生著作物もGPL-3.0でライセンスすること
        """
        gpl_code_result = "GPL処理完了（ソース開示必須）"
        
        # プロプライエタリライセンス部分
        """
        PROPRIETARY AND CONFIDENTIAL
        Source code disclosure is strictly prohibited.
        All rights reserved.
        
        プロプライエタリ要求: ソースコードの開示を一切禁止
        """
        proprietary_code_result = "プロプライエタリ処理完了（ソース開示禁止）"
        
        # 違反: 互換性のないライセンス要求を同時に満たそうとする
        return {
            'gpl_result': gpl_code_result,
            'proprietary_result': proprietary_code_result,
            'license_conflict': '重大な違反',
            'gpl_requirement': 'ソースコード開示必須',
            'proprietary_requirement': 'ソースコード開示禁止',
            'resolution': '不可能（互換性なし）',
            'legal_status': 'ライセンス違反',
            'risk_level': 'CRITICAL'
        }

# ============================================================================
# 故意のライセンス違反パターン #4: 商用ライセンス料金未払い
# ============================================================================

"""
Commercial License Payment Violation

This software requires a commercial license for commercial use.
License fee: $10,000 per deployment
Payment status: UNPAID (VIOLATION)

Commercial License Agreement Terms:
1. Annual license fee required for commercial use
2. Payment must be made before deployment
3. Audit rights reserved by licensor
4. Immediate termination for non-payment

VIOLATION NOTICE:
This software is being used commercially without payment of required license fees.
This constitutes a material breach of license terms.
"""

class UnpaidCommercialLicense:
    """
    商用ライセンス料金未払いクラス
    
    商用利用に必要なライセンス料金が支払われずに
    違法に使用されています。
    """
    
    def __init__(self):
        self.license_fee_required = 10000  # USD
        self.license_fee_paid = 0  # 未払い
        self.commercial_use = True  # 商用利用中
        self.payment_status = "OVERDUE"
        
    def commercial_feature_violation(self, data: any) -> dict:
        """
        商用機能の無許可使用
        
        ライセンス料金を支払わずに商用機能を使用しています。
        """
        if self.commercial_use and self.license_fee_paid < self.license_fee_required:
            # ライセンス料金未払いでの商用使用（違反）
            result = {
                'processed_data': f"商用処理: {data}",
                'license_status': 'VIOLATION',
                'fee_required': self.license_fee_required,
                'fee_paid': self.license_fee_paid,
                'outstanding_balance': self.license_fee_required - self.license_fee_paid,
                'days_overdue': 90,
                'penalty_fee': 5000,
                'total_amount_due': 15000,
                'legal_action_pending': True,
                'license_termination_notice': '即時効力停止予定'
            }
            
            return result
        
        return {'error': 'ライセンス料金を支払ってください'}

# ============================================================================
# 故意のライセンス違反パターン #5: 特許侵害
# ============================================================================

"""
Patent Infringement Violation

This code implements patented algorithms without proper licensing.

Patent Information:
- Patent No: US1234567 (fictional)
- Patent Holder: Patent Corp LLC
- Patent Title: "Advanced Data Processing Method"
- Status: Active, expires 2035
- License Required: Yes
- License Obtained: NO (VIOLATION)

PATENT VIOLATION NOTICE:
Use of this patented algorithm without license constitutes patent infringement.
Patent holder reserves all rights to pursue legal action.
"""

def patented_algorithm_infringement(data: list) -> dict:
    """
    特許侵害アルゴリズム
    
    特許保護されたアルゴリズムを無許可で実装・使用しています。
    
    特許違反内容:
    - US特許1234567の無許可実装
    - 特許ライセンス料の未払い
    - 特許権者への通知なし
    """
    # 特許侵害アルゴリズムの実装
    if not data:
        return {'error': '入力データなし'}
    
    # "高度なデータ処理手法"（特許侵害）
    enhanced_data = []
    for i, item in enumerate(data):
        # 特許アルゴリズム: 複雑な変換処理
        if isinstance(item, (int, float)):
            enhanced_value = (item * 1.618033988749) ** 0.5  # 黄金比を使用した特許手法
            enhanced_data.append(enhanced_value)
        else:
            enhanced_data.append(str(item)[::-1])  # 文字列反転（特許手法の一部）
    
    return {
        'enhanced_data': enhanced_data,
        'algorithm': 'Advanced Data Processing Method',
        'patent_number': 'US1234567 (fictional)',
        'patent_status': '有効（2035年まで）',
        'license_status': '未取得（違反）',
        'infringement_type': '特許無許可実装',
        'potential_damages': '$1,000,000+',
        'legal_risk': '極めて高い',
        'patent_holder': 'Patent Corp LLC',
        'injunction_risk': '使用差し止めの可能性'
    }

# ============================================================================
# 故意のライセンス違反パターン #6: オープンソース義務違反
# ============================================================================

"""
Open Source Obligation Violation

This code is derived from AGPL-3.0 licensed software but fails to comply
with network copyleft requirements.

AGPL-3.0 Network Copyleft Requirement:
If you run a modified version of AGPL software on a server and let users
interact with it over a network, you must provide the source code to those users.

VIOLATION:
- Modified AGPL-3.0 code is running on production servers
- Source code is not made available to network users
- No download link or source code offer provided
- AGPL license text not displayed to users
"""

class AGPLNetworkViolation:
    """
    AGPLネットワークコピーレフト違反クラス
    
    AGPL-3.0のネットワークコピーレフト義務に違反して
    サーバーサービスを提供しています。
    """
    
    def __init__(self):
        self.server_deployment = True
        self.network_service = True
        self.source_code_available = False  # 違反
        self.agpl_notice_displayed = False  # 違反
        self.modified_agpl_code = True
        
    def provide_network_service(self, user_request: str) -> dict:
        """
        ネットワークサービス提供（AGPL違反）
        
        AGPL-3.0コードを修正してネットワークサービスを提供していますが、
        ソースコード提供義務を果たしていません。
        """
        # AGPL由来の処理（修正版）
        service_response = f"処理完了: {user_request.upper()}"
        
        # AGPL違反: ソースコード提供義務を怠る
        return {
            'service_response': service_response,
            'server_deployment': self.server_deployment,
            'agpl_source_available': self.source_code_available,  # False (違反)
            'license_notice_shown': self.agpl_notice_displayed,   # False (違反)
            'agpl_compliance': False,
            'violation_type': 'AGPLネットワークコピーレフト違反',
            'required_actions': [
                'ソースコードのダウンロードリンク提供',
                'AGPLライセンステキストの表示',
                '修正版ソースコードの公開',
                'ユーザーへの適切な通知'
            ],
            'compliance_status': 'NON-COMPLIANT',
            'enforcement_risk': '高い'
        }

# ============================================================================
# 故意のライセンス違反パターン #7: 輸出規制違反
# ============================================================================

"""
Export Control Violation

This software contains encryption technology subject to U.S. Export Administration
Regulations (EAR) and may not be exported to certain countries.

RESTRICTED COUNTRIES (illustrative):
- Country A, Country B, Country C

VIOLATION:
Software containing controlled encryption has been distributed to restricted
jurisdictions without proper export licenses.

Export Classification: ECCN 5D002 (fictional)
License Required: Yes
License Obtained: NO (VIOLATION)
"""

def export_restricted_encryption(data: str, destination_country: str) -> dict:
    """
    輸出規制対象暗号化機能
    
    米国輸出管理規制（EAR）の対象となる暗号技術を
    許可なく制限国に提供しています。
    """
    # 輸出規制対象の暗号化実装
    import hashlib
    
    # 高度な暗号化処理（輸出規制対象）
    encrypted = hashlib.sha256(data.encode()).hexdigest()
    
    # 輸出規制チェック（違反状態）
    restricted_countries = ['Country A', 'Country B', 'Country C']
    export_violation = destination_country in restricted_countries
    
    return {
        'encrypted_data': encrypted,
        'encryption_strength': '256-bit SHA (輸出規制対象)',
        'destination_country': destination_country,
        'export_violation': export_violation,
        'eccn_classification': '5D002 (fictional)',
        'export_license_required': True,
        'export_license_obtained': False,  # 違反
        'violation_severity': 'CRITICAL' if export_violation else 'COMPLIANT',
        'potential_penalties': [
            '$1,000,000+ 罰金',
            '刑事訴追の可能性',
            '輸出特権の停止',
            '事業制限'
        ] if export_violation else [],
        'compliance_office': '米国商務省産業安全保障局（BIS）'
    }

# ============================================================================
# ライセンス違反検出シミュレーター
# ============================================================================

def simulate_license_violation_detection() -> dict:
    """
    ライセンス違反検出シミュレーション
    
    様々なライセンス違反パターンを検出し、分析結果を返します。
    """
    violations_detected = []
    
    # GPL違反検出
    gpl_violation = {
        'violation_type': 'GPL商用利用違反',
        'severity': 'CRITICAL',
        'description': 'GPL-3.0コードをプロプライエタリソフトウェアで無許可使用',
        'evidence': 'stolen_gpl_algorithm関数',
        'remediation': 'GPLライセンス採用またはコード除去'
    }
    violations_detected.append(gpl_violation)
    
    # 著作権違反検出
    copyright_violation = {
        'violation_type': '著作権表示削除違反',
        'severity': 'HIGH',
        'description': 'MITライセンスの著作権表示を無断削除',
        'evidence': 'copyright_stripped_function関数',
        'remediation': '著作権表示の復元'
    }
    violations_detected.append(copyright_violation)
    
    # ライセンス互換性違反検出
    compatibility_violation = {
        'violation_type': 'ライセンス互換性違反',
        'severity': 'CRITICAL',
        'description': 'GPL-3.0とプロプライエタリライセンスの非互換組み合わせ',
        'evidence': 'IncompatibleLicenseMixer クラス',
        'remediation': 'ライセンス統一またはコンポーネント分離'
    }
    violations_detected.append(compatibility_violation)
    
    # 商用ライセンス違反検出
    commercial_violation = {
        'violation_type': '商用ライセンス料金未払い',
        'severity': 'HIGH',
        'description': '商用ライセンス料金未払いでの商用利用',
        'evidence': 'UnpaidCommercialLicense クラス',
        'remediation': 'ライセンス料金支払いまたは使用停止'
    }
    violations_detected.append(commercial_violation)
    
    # 特許侵害検出
    patent_violation = {
        'violation_type': '特許侵害',
        'severity': 'CRITICAL',
        'description': '特許保護アルゴリズムの無許可実装',
        'evidence': 'patented_algorithm_infringement関数',
        'remediation': '特許ライセンス取得またはアルゴリズム変更'
    }
    violations_detected.append(patent_violation)
    
    # AGPL違反検出
    agpl_violation = {
        'violation_type': 'AGPLネットワークコピーレフト違反',
        'severity': 'HIGH',
        'description': 'AGPLコードのネットワークサービス利用でソース非公開',
        'evidence': 'AGPLNetworkViolation クラス',
        'remediation': 'ソースコード公開またはライセンス変更'
    }
    violations_detected.append(agpl_violation)
    
    # 輸出規制違反検出
    export_violation = {
        'violation_type': '輸出規制違反',
        'severity': 'CRITICAL',
        'description': '暗号技術の無許可輸出',
        'evidence': 'export_restricted_encryption関数',
        'remediation': '輸出ライセンス取得または配布停止'
    }
    violations_detected.append(export_violation)
    
    # 総合分析
    critical_count = sum(1 for v in violations_detected if v['severity'] == 'CRITICAL')
    high_count = sum(1 for v in violations_detected if v['severity'] == 'HIGH')
    
    return {
        'total_violations': len(violations_detected),
        'critical_violations': critical_count,
        'high_violations': high_count,
        'overall_risk': 'EXTREMELY HIGH',
        'violations_detail': violations_detected,
        'immediate_actions_required': [
            'すべての違反コードの使用停止',
            '法務部門への緊急相談',
            'ライセンス監査の実施',
            '影響範囲の調査',
            '修正計画の策定'
        ],
        'legal_exposure': '民事・刑事両面での訴訟リスク',
        'business_impact': '事業継続に重大な影響',
        'compliance_status': 'NON-COMPLIANT (重大違反)'
    }

# テスト実行
if __name__ == "__main__":
    print("=== ライセンス違反シミュレーション開始 ===")
    print("警告: このコードはテスト目的のみです")
    
    # 違反検出シミュレーション実行
    violation_report = simulate_license_violation_detection()
    print(f"検出された違反: {violation_report['total_violations']}件")
    print(f"重大違反: {violation_report['critical_violations']}件")
    print(f"リスクレベル: {violation_report['overall_risk']}")
    
    # 個別違反例の実行（デモンストレーション）
    print("\n=== 個別違反例 ===")
    
    # GPL違反例
    gpl_result = stolen_gpl_algorithm([3, 1, 4, 1, 5])
    print(f"GPL違反例: {gpl_result['violation_type']}")
    
    # 特許侵害例
    patent_result = patented_algorithm_infringement([1, 2, 3])
    print(f"特許侵害例: {patent_result['infringement_type']}")
    
    print("\n=== シミュレーション完了 ===")