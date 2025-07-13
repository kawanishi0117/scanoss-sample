# CLAUDE.md

このファイルは、このリポジトリのコードを扱う際にClaude Code (claude.ai/code) にガイダンスを提供します。

## プロジェクト概要

これは、包括的なライセンス検出機能をテストするために意図的に混合ライセンスのPythonコードを含むSCANOSSライセンススキャンテストリポジトリです。プロジェクトには以下が含まれます：

- **パーミッシブライセンスコード** (MIT, BSD-3-Clause, Apache-2.0, ISC, Unlicense, WTFPL, Boost, zlib) 
- **コピーレフトライセンスコード** (GPL-2.0, GPL-3.0, LGPL-2.1, AGPL-3.0) 検出テスト用
- **弱いコピーレフトライセンス** (MPL-2.0, EPL-2.0) 互換性テスト用
- **クリエイティブ・コモンズライセンス** (CC-BY-4.0, CC-BY-SA-4.0, CC-BY-NC-4.0) コンテンツライセンス用
- **プロプライエタリ/商用ライセンス** エンタープライズスキャンシナリオ用
- **混合ライセンス競合** 複雑な検出テスト用
- **Webスクレイピングとデータ処理ユーティリティ**
- **GitHub Actions経由の自動ライセンススキャン**

## コマンドと開発

### テストの実行
```bash
python test.py  # 基本テストランナー（現在は空）
python license_test_runner.py  # 包括的ライセンス検出テストランナー
```

### ライセンススキャン
リポジトリは自動ライセンス検出にSCANOSSを使用します：
```bash
# ライセンススキャンはGitHub Actions経由でPRで自動実行されます
# 手動スキャンはSCANOSS CLIツールで実行できます
```

### Python環境
これは標準ライブラリ依存関係を持つ純粋なPythonプロジェクトに加えて：
- `click` (MIT) - CLI設定
- `pandas` (BSD-3-Clause) - データ処理  
- `beautifulsoup4` (MIT) - HTML解析
- `requests` (Apache-2.0) - HTTPクライアント
- `pyyaml` (MIT) - 設定ファイル

## アーキテクチャ

### モジュール構造
```
src/
├── config/              # 設定管理
│   ├── settings.py      # clickを使用したCLIとYAML設定 (MIT)
│   └── mpl2_config.py   # Mozilla Public License 2.0設定
├── data/               # データ処理ユーティリティ
│   ├── processor.py    # Pandasベースのデータ処理 (BSD-3-Clause)
│   ├── utils.py        # LGPL-2.1ユーティリティ（テスト用意図的）
│   ├── apache_utils.py # Apache-2.0ライセンスデータユーティリティ
│   ├── agpl3_database.py # AGPL-3.0データベース管理システム
│   ├── epl2_analytics.py # Eclipse Public License 2.0アナリティクス
│   └── cc_content.py   # クリエイティブ・コモンズライセンスコンテンツ処理
├── scraper/            # Webスクレイピングコンポーネント
│   ├── parser.py       # BeautifulSoup HTML解析 (MIT)
│   ├── web_client.py   # GPL-3.0 HTTPクライアント（テスト用意図的）
│   ├── gpl2_tools.py   # GPL-2.0ネットワークスキャンツール
│   └── proprietary_tools.py # プロプライエタリ/商用ライセンスツール
├── mixed_licenses.py   # 複雑なテスト用混合ライセンスパターン
└── license_test_runner.py # 包括的ライセンス検出テストランナー
```

### ライセンステスト設計
コードベースは包括的なSCANOSS検出をテストするため意図的に多様なライセンスを含んでいます：

**コピーレフトライセンス（ポリシー違反を引き起こすべき）：**
- **gpl2_tools.py**: 完全なGPLヘッダー付きGPL-2.0ネットワークスキャンユーティリティ
- **web_client.py**: wget類似機能を持つGPL-3.0 HTTPクライアント
- **utils.py**: 明示的なLGPLライセンスヘッダー付きLGPL-2.1データユーティリティ
- **agpl3_database.py**: ネットワークコピーレフト要件を持つAGPL-3.0データベースシステム

**パーミッシブライセンス：**
- **apache_utils.py**: 完全なApacheライセンスヘッダー付きApache-2.0データ処理
- **その他のモジュール**: ベースライン互換性のためのMIT、BSD-3-Clauseライセンス

**弱いコピーレフト：**
- **mpl2_config.py**: Mozilla Public License 2.0設定管理
- **epl2_analytics.py**: Eclipse Public License 2.0アナリティクスエンジン

**クリエイティブ・コモンズ：**
- **cc_content.py**: コンテンツライセンシング用の複数CCバリエーション（BY、BY-SA、BY-NC）

**プロプライエタリ/商用：**
- **proprietary_tools.py**: エンタープライズテスト用のシミュレートされたプロプライエタリライセンス

**混合ライセンス競合：**
- **mixed_licenses.py**: 複雑なシナリオ用の単一ファイル内の複数競合ライセンス

### 主要コンポーネント

1. **設定管理**:
   - `src/config/settings.py`: ClickベースCLI設定 (MIT)
   - `src/config/mpl2_config.py`: Mozillaスタイル設定システム (MPL-2.0)

2. **データ処理システム**:
   - `src/data/processor.py`: Pandas DataFrame操作 (BSD-3-Clause)
   - `src/data/apache_utils.py`: Apache Commonsスタイルユーティリティ (Apache-2.0)
   - `src/data/agpl3_database.py`: MongoDBスタイルデータベースシステム (AGPL-3.0)
   - `src/data/epl2_analytics.py`: Eclipseスタイルアナリティクスエンジン (EPL-2.0)

3. **Webスクレイピング＆ネットワークツール**:
   - `src/scraper/parser.py`: BeautifulSoupベースHTML解析 (MIT)
   - `src/scraper/web_client.py`: GPL wget類似ダウンローダー (GPL-3.0)
   - `src/scraper/gpl2_tools.py`: nmapスタイルネットワークスキャナー (GPL-2.0)
   - `src/scraper/proprietary_tools.py`: エンタープライズ暗号化ツール (プロプライエタリ)

4. **ライセンステストフレームワーク**:
   - `license_test_runner.py`: 包括的ライセンス検出テスト
   - `src/mixed_licenses.py`: 混合ライセンス競合シナリオ

## GitHub Actions連携

リポジトリには自動ライセンススキャンが含まれています：
- **ワークフロー**: `.github/workflows/license-scan.yml`
- **トリガー**: プルリクエストのみ
- **ポリシー**: コピーレフトライセンスを検出 (GPL/LGPL/AGPL)
- **アクション**: `scanoss/gha-code-scan@v1`を`policies: copyleft`で使用
- **動作**: コピーレフトライセンス検出時にCIが失敗 (`policies.halt_on_failure: true`)

## 重要な注意事項

### ライセンスコンプライアンス
- これは意図的に多様で競合するライセンスを持つ**テストリポジトリ**です
- **コピーレフトライセンス** (GPL-2.0, GPL-3.0, LGPL-2.1, AGPL-3.0)はSCANOSSポリシー違反を引き起こすはずです
- `mixed_licenses.py`の**混合ライセンス競合**は複雑な検出シナリオを作成します
- **プロプライエタリコード**はエンタープライズスキャンチャレンジをシミュレートします
- **クリエイティブ・コモンズバリエーション**はドキュメントとコンテンツライセンシングをテストします
- 包括的なライセンスレビューなしにこのコードベースを本番環境で使用しないでください
- すべてのライセンスヘッダーはテスト目的で意図的に明示的です

### 開発ガイドライン
- テストファイルを修正する際はライセンスヘッダーコメントを維持してください
- テスト目的の意図的なライセンスミックスを保持してください
- 可能な限りPython標準ライブラリを使用してください
- 各モジュールの既存コードパターンに従ってください
- 変更後にライセンス検出をテストしてください

### SCANOSSテスト
- **PR提出**で包括的なライセンススキャンがトリガーされます
- **期待される動作**: コピーレフトライセンス検出 (GPL/LGPL/AGPL) によりCIが失敗するはずです
- **SARIF出力**が`scanoss.sarif`に保存され、詳細レビューが可能です
- **テストランナー**: ローカルテストには`python license_test_runner.py`を使用してください
- **ファイルターゲット**: 包括的カバレッジのため異なるライセンスタイプの複数ファイル
- **ポリシーテスト**: コピーレフト検出時のhalt-on-failure動作を検証
- **混合ライセンシナリオ**: `mixed_licenses.py`で複雑なライセンス競合検出をテスト

### 期待されるSCANOSS検出
以下のファイルがライセンス違反を引き起こすはずです：
- `src/scraper/gpl2_tools.py` (GPL-2.0)
- `src/scraper/web_client.py` (GPL-3.0)
- `src/data/utils.py` (LGPL-2.1)
- `src/data/agpl3_database.py` (AGPL-3.0)
- `src/mixed_licenses.py` (複数の競合ライセンス)