"""
複雑な依存関係とライセンス継承のテストモジュール

このモジュールは意図的に複雑な依存関係チェーンとライセンス継承パターンを作成し、
SCANOSS等のライセンス検出ツールの高度な分析機能をテストします。

警告: これはテスト専用のモジュールです。実際のプロジェクトでは使用しないでください。
"""

# ============================================================================
# 多層依存関係チェーン
# ============================================================================

"""
依存関係ツリー構造:

Root Project (MIT)
├── Module A (Apache-2.0)
│   ├── Module A1 (BSD-3-Clause)
│   │   ├── Module A1a (GPL-3.0) ← コピーレフト感染
│   │   └── Module A1b (MIT)
│   └── Module A2 (LGPL-2.1)
│       └── Module A2a (Proprietary) ← ライセンス競合
├── Module B (GPL-2.0) ← 別のコピーレフト
│   ├── Module B1 (GPL-2.0+)
│   └── Module B2 (AGPL-3.0) ← ネットワークコピーレフト
└── Module C (Commercial License)
    ├── Module C1 (WTFPL)
    └── Module C2 (CC-BY-SA-4.0) ← ShareAlike要求
"""

import sys
import os
import hashlib
import json
from typing import Dict, List, Any, Optional, Union
from dataclasses import dataclass
from enum import Enum
import logging

# 各レイヤーのライセンスシミュレーション
class LicenseType(Enum):
    """ライセンス種別列挙"""
    MIT = "MIT"
    APACHE_2_0 = "Apache-2.0"
    BSD_3_CLAUSE = "BSD-3-Clause"
    GPL_2_0 = "GPL-2.0"
    GPL_3_0 = "GPL-3.0"
    LGPL_2_1 = "LGPL-2.1"
    AGPL_3_0 = "AGPL-3.0"
    MPL_2_0 = "MPL-2.0"
    EPL_2_0 = "EPL-2.0"
    PROPRIETARY = "Proprietary"
    COMMERCIAL = "Commercial"
    WTFPL = "WTFPL"
    CC_BY_SA_4_0 = "CC-BY-SA-4.0"
    UNLICENSE = "Unlicense"

@dataclass
class LicenseInfo:
    """ライセンス情報データクラス"""
    license_type: LicenseType
    copyleft: bool
    commercial_use: bool
    patent_grant: bool
    network_copyleft: bool = False
    share_alike: bool = False
    attribution_required: bool = True

class DependencyNode:
    """
    依存関係ノードクラス
    
    各モジュールの依存関係とライセンス情報を管理します。
    """
    
    def __init__(self, name: str, license_info: LicenseInfo, version: str = "1.0.0"):
        self.name = name
        self.license_info = license_info
        self.version = version
        self.dependencies: List['DependencyNode'] = []
        self.license_conflicts: List[str] = []
        self.inherited_licenses: List[LicenseType] = []
    
    def add_dependency(self, dependency: 'DependencyNode') -> None:
        """依存関係を追加"""
        self.dependencies.append(dependency)
        self._analyze_license_inheritance()
    
    def _analyze_license_inheritance(self) -> None:
        """ライセンス継承を分析"""
        self.inherited_licenses = [self.license_info.license_type]
        
        for dep in self.dependencies:
            # コピーレフトライセンスの感染チェック
            if dep.license_info.copyleft:
                if dep.license_info.license_type == LicenseType.GPL_3_0:
                    self.inherited_licenses.append(LicenseType.GPL_3_0)
                    self._add_conflict(f"GPL-3.0感染: {dep.name}")
                
                elif dep.license_info.license_type == LicenseType.GPL_2_0:
                    self.inherited_licenses.append(LicenseType.GPL_2_0)
                    self._add_conflict(f"GPL-2.0感染: {dep.name}")
                
                elif dep.license_info.license_type == LicenseType.AGPL_3_0:
                    self.inherited_licenses.append(LicenseType.AGPL_3_0)
                    self._add_conflict(f"AGPL-3.0ネットワークコピーレフト感染: {dep.name}")
            
            # ライセンス競合チェック
            if (self.license_info.license_type == LicenseType.PROPRIETARY and 
                dep.license_info.copyleft):
                self._add_conflict(f"プロプライエタリ vs コピーレフト競合: {dep.name}")
            
            # ShareAlike要求チェック
            if dep.license_info.share_alike:
                self._add_conflict(f"ShareAlike要求: {dep.name}")
    
    def _add_conflict(self, conflict: str) -> None:
        """ライセンス競合を追加"""
        if conflict not in self.license_conflicts:
            self.license_conflicts.append(conflict)
    
    def get_dependency_tree(self, depth: int = 0) -> Dict[str, Any]:
        """依存関係ツリーを取得"""
        return {
            'name': self.name,
            'license': self.license_info.license_type.value,
            'version': self.version,
            'depth': depth,
            'conflicts': self.license_conflicts,
            'inherited_licenses': [lic.value for lic in self.inherited_licenses],
            'dependencies': [dep.get_dependency_tree(depth + 1) for dep in self.dependencies]
        }

# ============================================================================
# 複雑な依存関係シナリオ構築
# ============================================================================

def create_complex_dependency_scenario() -> DependencyNode:
    """
    複雑な依存関係シナリオを構築
    
    多層構造と相互競合するライセンスの組み合わせを作成します。
    """
    
    # ライセンス情報の定義
    licenses = {
        'MIT': LicenseInfo(LicenseType.MIT, False, True, False),
        'Apache-2.0': LicenseInfo(LicenseType.APACHE_2_0, False, True, True),
        'BSD-3-Clause': LicenseInfo(LicenseType.BSD_3_CLAUSE, False, True, False),
        'GPL-3.0': LicenseInfo(LicenseType.GPL_3_0, True, True, True),
        'GPL-2.0': LicenseInfo(LicenseType.GPL_2_0, True, True, False),
        'LGPL-2.1': LicenseInfo(LicenseType.LGPL_2_1, True, True, False),
        'AGPL-3.0': LicenseInfo(LicenseType.AGPL_3_0, True, True, True, True),
        'Proprietary': LicenseInfo(LicenseType.PROPRIETARY, False, False, False),
        'Commercial': LicenseInfo(LicenseType.COMMERCIAL, False, False, False),
        'WTFPL': LicenseInfo(LicenseType.WTFPL, False, True, False),
        'CC-BY-SA-4.0': LicenseInfo(LicenseType.CC_BY_SA_4_0, False, True, False, False, True)
    }
    
    # 依存関係ツリーの構築
    
    # 最下層ノード
    module_a1a = DependencyNode("module-a1a", licenses['GPL-3.0'], "2.1.0")
    module_a1b = DependencyNode("module-a1b", licenses['MIT'], "1.5.2")
    module_a2a = DependencyNode("module-a2a", licenses['Proprietary'], "3.0.1")
    module_b1 = DependencyNode("module-b1", licenses['GPL-2.0'], "1.8.4")
    module_b2 = DependencyNode("module-b2", licenses['AGPL-3.0'], "0.9.7")
    module_c1 = DependencyNode("module-c1", licenses['WTFPL'], "42.0")
    module_c2 = DependencyNode("module-c2", licenses['CC-BY-SA-4.0'], "4.0.0")
    
    # 中間層ノード
    module_a1 = DependencyNode("module-a1", licenses['BSD-3-Clause'], "2.3.1")
    module_a1.add_dependency(module_a1a)  # GPL-3.0感染
    module_a1.add_dependency(module_a1b)
    
    module_a2 = DependencyNode("module-a2", licenses['LGPL-2.1'], "1.2.8")
    module_a2.add_dependency(module_a2a)  # プロプライエタリ競合
    
    module_b = DependencyNode("module-b", licenses['GPL-2.0'], "3.1.4")
    module_b.add_dependency(module_b1)
    module_b.add_dependency(module_b2)  # AGPL追加感染
    
    module_c = DependencyNode("module-c", licenses['Commercial'], "5.2.0")
    module_c.add_dependency(module_c1)
    module_c.add_dependency(module_c2)  # ShareAlike競合
    
    # トップレベルノード
    module_a = DependencyNode("module-a", licenses['Apache-2.0'], "4.1.2")
    module_a.add_dependency(module_a1)
    module_a.add_dependency(module_a2)
    
    # ルートプロジェクト
    root_project = DependencyNode("root-project", licenses['MIT'], "1.0.0")
    root_project.add_dependency(module_a)
    root_project.add_dependency(module_b)
    root_project.add_dependency(module_c)
    
    return root_project

# ============================================================================
# ライセンス互換性マトリックス
# ============================================================================

class LicenseCompatibilityMatrix:
    """
    ライセンス互換性マトリックス
    
    各ライセンス間の互換性を評価します。
    """
    
    def __init__(self):
        # 互換性マトリックス (ライセンス1 -> ライセンス2 の互換性)
        self.compatibility_matrix = {
            LicenseType.MIT: {
                LicenseType.MIT: 'COMPATIBLE',
                LicenseType.APACHE_2_0: 'COMPATIBLE',
                LicenseType.BSD_3_CLAUSE: 'COMPATIBLE',
                LicenseType.GPL_3_0: 'COMPATIBLE',
                LicenseType.GPL_2_0: 'COMPATIBLE',
                LicenseType.LGPL_2_1: 'COMPATIBLE',
                LicenseType.AGPL_3_0: 'COMPATIBLE',
                LicenseType.PROPRIETARY: 'COMPATIBLE',
                LicenseType.COMMERCIAL: 'COMPATIBLE'
            },
            LicenseType.GPL_3_0: {
                LicenseType.MIT: 'INCOMPATIBLE_COPYLEFT',
                LicenseType.APACHE_2_0: 'COMPATIBLE',
                LicenseType.BSD_3_CLAUSE: 'COMPATIBLE', 
                LicenseType.GPL_3_0: 'COMPATIBLE',
                LicenseType.GPL_2_0: 'INCOMPATIBLE_VERSION',
                LicenseType.LGPL_2_1: 'COMPATIBLE',
                LicenseType.AGPL_3_0: 'COMPATIBLE',
                LicenseType.PROPRIETARY: 'INCOMPATIBLE_COPYLEFT',
                LicenseType.COMMERCIAL: 'INCOMPATIBLE_COPYLEFT'
            },
            LicenseType.PROPRIETARY: {
                LicenseType.MIT: 'COMPATIBLE',
                LicenseType.APACHE_2_0: 'COMPATIBLE',
                LicenseType.BSD_3_CLAUSE: 'COMPATIBLE',
                LicenseType.GPL_3_0: 'INCOMPATIBLE_COPYLEFT',
                LicenseType.GPL_2_0: 'INCOMPATIBLE_COPYLEFT',
                LicenseType.LGPL_2_1: 'CONDITIONAL',
                LicenseType.AGPL_3_0: 'INCOMPATIBLE_COPYLEFT',
                LicenseType.PROPRIETARY: 'CONDITIONAL'
            }
        }
    
    def check_compatibility(self, license1: LicenseType, license2: LicenseType) -> str:
        """2つのライセンス間の互換性をチェック"""
        if license1 in self.compatibility_matrix:
            if license2 in self.compatibility_matrix[license1]:
                return self.compatibility_matrix[license1][license2]
        
        return 'UNKNOWN'
    
    def analyze_dependency_compatibility(self, root_node: DependencyNode) -> Dict[str, Any]:
        """依存関係全体の互換性を分析"""
        all_licenses = self._collect_all_licenses(root_node)
        conflicts = []
        warnings = []
        
        # すべてのライセンスペア間の互換性をチェック
        for i, lic1 in enumerate(all_licenses):
            for lic2 in all_licenses[i+1:]:
                compatibility = self.check_compatibility(lic1, lic2)
                
                if compatibility == 'INCOMPATIBLE_COPYLEFT':
                    conflicts.append(f"{lic1.value} vs {lic2.value}: コピーレフト競合")
                elif compatibility == 'INCOMPATIBLE_VERSION':
                    conflicts.append(f"{lic1.value} vs {lic2.value}: バージョン非互換")
                elif compatibility == 'CONDITIONAL':
                    warnings.append(f"{lic1.value} vs {lic2.value}: 条件付き互換")
                elif compatibility == 'UNKNOWN':
                    warnings.append(f"{lic1.value} vs {lic2.value}: 互換性不明")
        
        return {
            'total_licenses': len(set(all_licenses)),
            'unique_licenses': list(set(lic.value for lic in all_licenses)),
            'conflicts': conflicts,
            'warnings': warnings,
            'compatibility_status': 'INCOMPATIBLE' if conflicts else ('WARNING' if warnings else 'COMPATIBLE'),
            'risk_level': self._calculate_risk_level(conflicts, warnings)
        }
    
    def _collect_all_licenses(self, node: DependencyNode) -> List[LicenseType]:
        """依存関係ツリーからすべてのライセンスを収集"""
        licenses = [node.license_info.license_type]
        
        for dep in node.dependencies:
            licenses.extend(self._collect_all_licenses(dep))
        
        return licenses
    
    def _calculate_risk_level(self, conflicts: List[str], warnings: List[str]) -> str:
        """リスクレベルを計算"""
        if len(conflicts) >= 3:
            return 'CRITICAL'
        elif len(conflicts) >= 1:
            return 'HIGH'
        elif len(warnings) >= 3:
            return 'MEDIUM'
        elif len(warnings) >= 1:
            return 'LOW'
        else:
            return 'MINIMAL'

# ============================================================================
# ライセンス継承シミュレーター
# ============================================================================

class LicenseInheritanceSimulator:
    """
    ライセンス継承シミュレーター
    
    複雑な依存関係チェーンでのライセンス継承をシミュレートします。
    """
    
    def __init__(self):
        self.inheritance_rules = {
            # 強いコピーレフト
            LicenseType.GPL_3_0: {
                'infects_all': True,
                'network_effect': False,
                'dynamic_link_ok': False,
                'static_link_infects': True
            },
            LicenseType.GPL_2_0: {
                'infects_all': True,
                'network_effect': False,
                'dynamic_link_ok': False,
                'static_link_infects': True
            },
            # ネットワークコピーレフト
            LicenseType.AGPL_3_0: {
                'infects_all': True,
                'network_effect': True,
                'dynamic_link_ok': False,
                'static_link_infects': True
            },
            # 弱いコピーレフト
            LicenseType.LGPL_2_1: {
                'infects_all': False,
                'network_effect': False,
                'dynamic_link_ok': True,
                'static_link_infects': False
            },
            LicenseType.MPL_2_0: {
                'infects_all': False,
                'network_effect': False,
                'dynamic_link_ok': True,
                'static_link_infects': False
            }
        }
    
    def simulate_inheritance(self, root_node: DependencyNode) -> Dict[str, Any]:
        """ライセンス継承をシミュレート"""
        result = {
            'root_license': root_node.license_info.license_type.value,
            'effective_licenses': [],
            'inheritance_path': [],
            'obligations': [],
            'restrictions': [],
            'compliance_requirements': []
        }
        
        # 最も制限的なライセンスを特定
        strongest_license = self._find_strongest_license(root_node)
        result['effective_licenses'] = [strongest_license.value]
        
        # 継承パスを追跡
        inheritance_path = self._trace_inheritance_path(root_node, strongest_license)
        result['inheritance_path'] = inheritance_path
        
        # 義務と制限を計算
        obligations = self._calculate_obligations(strongest_license)
        result['obligations'] = obligations
        
        restrictions = self._calculate_restrictions(strongest_license)
        result['restrictions'] = restrictions
        
        # コンプライアンス要件
        compliance = self._generate_compliance_requirements(strongest_license, root_node)
        result['compliance_requirements'] = compliance
        
        return result
    
    def _find_strongest_license(self, node: DependencyNode) -> LicenseType:
        """最も制限的なライセンスを特定"""
        all_licenses = self._collect_all_licenses_deep(node)
        
        # 優先順位: AGPL > GPL > LGPL > その他
        if LicenseType.AGPL_3_0 in all_licenses:
            return LicenseType.AGPL_3_0
        elif LicenseType.GPL_3_0 in all_licenses:
            return LicenseType.GPL_3_0
        elif LicenseType.GPL_2_0 in all_licenses:
            return LicenseType.GPL_2_0
        elif LicenseType.LGPL_2_1 in all_licenses:
            return LicenseType.LGPL_2_1
        elif LicenseType.MPL_2_0 in all_licenses:
            return LicenseType.MPL_2_0
        else:
            return node.license_info.license_type
    
    def _collect_all_licenses_deep(self, node: DependencyNode) -> List[LicenseType]:
        """深い階層まですべてのライセンスを収集"""
        licenses = [node.license_info.license_type]
        
        for dep in node.dependencies:
            licenses.extend(self._collect_all_licenses_deep(dep))
        
        return licenses
    
    def _trace_inheritance_path(self, node: DependencyNode, target_license: LicenseType) -> List[str]:
        """ライセンス継承のパスを追跡"""
        path = []
        
        def find_path(current_node: DependencyNode, current_path: List[str]) -> bool:
            current_path.append(f"{current_node.name}({current_node.license_info.license_type.value})")
            
            if current_node.license_info.license_type == target_license:
                path.extend(current_path)
                return True
            
            for dep in current_node.dependencies:
                if find_path(dep, current_path.copy()):
                    return True
            
            return False
        
        find_path(node, [])
        return path
    
    def _calculate_obligations(self, license_type: LicenseType) -> List[str]:
        """ライセンスによる義務を計算"""
        obligations = []
        
        if license_type in [LicenseType.GPL_2_0, LicenseType.GPL_3_0]:
            obligations.extend([
                "ソースコード提供義務",
                "GPLライセンステキスト同梱義務",
                "著作権表示保持義務",
                "修正内容の明示義務"
            ])
        
        if license_type == LicenseType.AGPL_3_0:
            obligations.extend([
                "ネットワーク利用時のソースコード提供義務",
                "修正版サーバーコードの公開義務"
            ])
        
        if license_type in [LicenseType.APACHE_2_0]:
            obligations.extend([
                "NOTICEファイル提供義務",
                "著作権表示義務",
                "ライセンステキスト同梱義務"
            ])
        
        return obligations
    
    def _calculate_restrictions(self, license_type: LicenseType) -> List[str]:
        """ライセンスによる制限を計算"""
        restrictions = []
        
        if license_type in [LicenseType.GPL_2_0, LicenseType.GPL_3_0, LicenseType.AGPL_3_0]:
            restrictions.extend([
                "プロプライエタリライセンス併用不可",
                "DRMによる制限禁止",
                "特許訴訟による自動失効"
            ])
        
        if license_type == LicenseType.PROPRIETARY:
            restrictions.extend([
                "ソースコード開示禁止",
                "再配布制限",
                "商用利用要ライセンス"
            ])
        
        return restrictions
    
    def _generate_compliance_requirements(self, license_type: LicenseType, root_node: DependencyNode) -> List[str]:
        """コンプライアンス要件を生成"""
        requirements = []
        
        if license_type in [LicenseType.GPL_2_0, LicenseType.GPL_3_0, LicenseType.AGPL_3_0]:
            requirements.extend([
                f"プロジェクト全体を{license_type.value}でライセンス",
                "ソースコード配布メカニズムの確立",
                "ビルドスクリプトと依存関係の文書化",
                "法務レビューの実施"
            ])
        
        requirements.append("第三者ライセンス一覧の作成")
        requirements.append("ライセンス互換性監査の実施")
        
        return requirements

# ============================================================================
# 統合テストスイート
# ============================================================================

def run_comprehensive_license_analysis():
    """包括的なライセンス分析を実行"""
    print("=== 複雑な依存関係とライセンス継承の分析開始 ===")
    
    # 複雑な依存関係シナリオを作成
    root_project = create_complex_dependency_scenario()
    
    # 依存関係ツリーの表示
    dependency_tree = root_project.get_dependency_tree()
    print(f"\n依存関係ツリー:")
    print(json.dumps(dependency_tree, indent=2, ensure_ascii=False))
    
    # ライセンス互換性分析
    compatibility_analyzer = LicenseCompatibilityMatrix()
    compatibility_result = compatibility_analyzer.analyze_dependency_compatibility(root_project)
    
    print(f"\n=== ライセンス互換性分析 ===")
    print(f"総ライセンス数: {compatibility_result['total_licenses']}")
    print(f"ユニークライセンス: {compatibility_result['unique_licenses']}")
    print(f"互換性ステータス: {compatibility_result['compatibility_status']}")
    print(f"リスクレベル: {compatibility_result['risk_level']}")
    
    if compatibility_result['conflicts']:
        print(f"\n競合:")
        for conflict in compatibility_result['conflicts']:
            print(f"  - {conflict}")
    
    if compatibility_result['warnings']:
        print(f"\n警告:")
        for warning in compatibility_result['warnings']:
            print(f"  - {warning}")
    
    # ライセンス継承シミュレーション
    inheritance_simulator = LicenseInheritanceSimulator()
    inheritance_result = inheritance_simulator.simulate_inheritance(root_project)
    
    print(f"\n=== ライセンス継承分析 ===")
    print(f"ルートライセンス: {inheritance_result['root_license']}")
    print(f"有効ライセンス: {inheritance_result['effective_licenses']}")
    print(f"継承パス: {' -> '.join(inheritance_result['inheritance_path'])}")
    
    print(f"\n義務:")
    for obligation in inheritance_result['obligations']:
        print(f"  - {obligation}")
    
    print(f"\n制限:")
    for restriction in inheritance_result['restrictions']:
        print(f"  - {restriction}")
    
    print(f"\nコンプライアンス要件:")
    for requirement in inheritance_result['compliance_requirements']:
        print(f"  - {requirement}")
    
    # 総合リスク評価
    overall_risk = _calculate_overall_risk(compatibility_result, inheritance_result)
    print(f"\n=== 総合リスク評価 ===")
    print(f"総合リスクレベル: {overall_risk['level']}")
    print(f"リスク要因: {overall_risk['factors']}")
    print(f"推奨アクション: {overall_risk['recommendations']}")
    
    return {
        'dependency_tree': dependency_tree,
        'compatibility_analysis': compatibility_result,
        'inheritance_analysis': inheritance_result,
        'overall_risk': overall_risk
    }

def _calculate_overall_risk(compatibility_result: Dict, inheritance_result: Dict) -> Dict[str, Any]:
    """総合リスクを計算"""
    risk_factors = []
    recommendations = []
    
    # 互換性リスクの評価
    if compatibility_result['compatibility_status'] == 'INCOMPATIBLE':
        risk_factors.append("重大なライセンス競合")
        recommendations.append("非互換ライセンスの除去または置換")
    
    # 継承リスクの評価
    if 'AGPL' in str(inheritance_result['effective_licenses']):
        risk_factors.append("AGPLネットワークコピーレフト感染")
        recommendations.append("ネットワークサービス利用時のソースコード公開準備")
    
    if 'GPL' in str(inheritance_result['effective_licenses']):
        risk_factors.append("GPLコピーレフト感染")
        recommendations.append("プロジェクト全体のGPLライセンス採用検討")
    
    # リスクレベルの決定
    if len(risk_factors) >= 3:
        level = "CRITICAL"
    elif len(risk_factors) >= 2:
        level = "HIGH"
    elif len(risk_factors) >= 1:
        level = "MEDIUM"
    else:
        level = "LOW"
    
    if not recommendations:
        recommendations.append("現在の構成は概ね問題ありません")
    
    return {
        'level': level,
        'factors': risk_factors,
        'recommendations': recommendations
    }

if __name__ == "__main__":
    # 包括的分析の実行
    analysis_result = run_comprehensive_license_analysis()
    
    print("\n=== 分析完了 ===")
    print("複雑な依存関係とライセンス継承の分析が完了しました。")
    print("この分析結果はSCANOSSライセンス検出の精度向上に役立ちます。")