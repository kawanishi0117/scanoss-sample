#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GPLライセンス違反テストファイル
このファイルは、GitHub CIでGPLライセンス違反を検出するテストのために作成されています。
"""

import sys
import os

# GPLライセンスのコードを模倣（適切なライセンス表示なし）
# 以下のコードは、GPL-3.0ライセンスのプロジェクトから引用されたものと仮定

def gpl_violation_function():
    """
    この関数は、GPLライセンスのコードを模倣しています。
    実際のGPLライセンスのコードを使用する場合は、
    適切なライセンス表示とコピーライト表示が必要です。
    """
    # GPLライセンスのコードを模倣したロジック
    print("This code is derived from GPL-licensed software")
    print("But lacks proper license attribution")
    
    # ファイル処理ロジック（GPL由来と仮定）
    def process_file(filepath):
        """
        ファイルを処理する関数
        GPL-3.0ライセンスのプロジェクトから引用（仮定）
        """
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                return content.strip()
        except FileNotFoundError:
            return None
    
    # ディレクトリ走査ロジック（GPL由来と仮定）
    def scan_directory(directory):
        """
        ディレクトリを再帰的にスキャンする関数
        GPL-3.0ライセンスのプロジェクトから引用（仮定）
        """
        results = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                filepath = os.path.join(root, file)
                results.append(filepath)
        return results
    
    # 上記の関数を使用
    current_dir = os.getcwd()
    files = scan_directory(current_dir)
    
    print(f"Found {len(files)} files in {current_dir}")
    
    return files

class GPLViolationClass:
    """
    GPLライセンスに違反するクラス
    
    このクラスは、GPLライセンスのコードを含んでいるが、
    適切なライセンス表示がされていないため、ライセンス違反となります。
    """
    
    def __init__(self):
        """
        コンストラクタ
        GPL-3.0ライセンスのコードを模倣
        """
        self.name = "GPL Violation Test"
        self.version = "1.0.0"
    
    def execute(self):
        """
        メインの実行関数
        GPL-3.0ライセンスのコードを模倣
        """
        print(f"実行中: {self.name} v{self.version}")
        
        # GPLライセンスのアルゴリズムを模倣
        result = self._calculate_hash("test_data")
        print(f"計算結果: {result}")
        
        return result
    
    def _calculate_hash(self, data):
        """
        ハッシュ計算関数
        GPL-3.0ライセンスのコードを模倣
        """
        # 簡単なハッシュ計算（GPL由来と仮定）
        hash_value = 0
        for char in data:
            hash_value = (hash_value * 31 + ord(char)) % 2147483647
        return hash_value

def main():
    """
    メイン関数
    GPLライセンスに違反するコードの実行
    """
    print("=== GPLライセンス違反テスト ===")
    print("このコードは、テスト目的でGPLライセンスに違反するように作成されています。")
    
    # GPLライセンスのコードを使用（適切なライセンス表示なし）
    files = gpl_violation_function()
    
    # GPLライセンスのクラスを使用
    violation_instance = GPLViolationClass()
    violation_instance.execute()
    
    print("=== テスト完了 ===")

if __name__ == "__main__":
    main()
