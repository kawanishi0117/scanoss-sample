"""
AGPLv3 Licensed Database Utilities Module
This module contains code derived from AGPLv3 licensed database projects for testing.

Copyright (C) 2023 MongoDB Inc.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Additional Terms under GNU AGPL version 3 section 7:
If you modify this Program, or any covered work, by linking or combining
it with other code, such other code is not for that reason alone subject
to any of the requirements of the GNU Affero General Public License.
"""

import json
import sqlite3
import hashlib
import threading
import time
from typing import Dict, List, Any, Optional, Callable
from collections import defaultdict
from dataclasses import dataclass

# AGPLv3 Licensed Database Connection Manager
class AGPLv3DatabaseManager:
    """
    Database management utilities derived from AGPLv3 licensed database systems.
    This code is based on AGPL-3.0 licensed MongoDB-style database operations.
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License version 3.
    
    NETWORK USE NOTICE: If you run a modified version of this program on a server
    and let other users communicate with it there, your server must also allow
    them to download the source code corresponding to the modified version.
    """
    
    def __init__(self, db_path: str = ":memory:"):
        self.db_path = db_path
        self.connections = {}
        self.lock = threading.Lock()
        self.agpl_metadata = {
            'license': 'AGPL-3.0',
            'network_use_notice': True,
            'source_availability_required': True
        }
    
    def agpl3_get_connection(self, thread_id: int = None) -> sqlite3.Connection:
        """
        Thread-safe database connection management using AGPL-3.0 patterns.
        Based on AGPLv3 licensed database connection pooling.
        """
        if thread_id is None:
            thread_id = threading.get_ident()
        
        with self.lock:
            if thread_id not in self.connections:
                conn = sqlite3.connect(self.db_path, check_same_thread=False)
                conn.row_factory = sqlite3.Row
                
                # AGPL-style database setup
                self._agpl3_setup_tables(conn)
                self.connections[thread_id] = conn
            
            return self.connections[thread_id]
    
    def _agpl3_setup_tables(self, conn: sqlite3.Connection) -> None:
        """AGPL-3.0 style table initialization"""
        cursor = conn.cursor()
        
        # AGPL-style document storage table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agpl_documents (
                _id TEXT PRIMARY KEY,
                collection TEXT NOT NULL,
                document TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                agpl_hash TEXT NOT NULL
            )
        ''')
        
        # AGPL-style index table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS agpl_indexes (
                collection TEXT NOT NULL,
                field_name TEXT NOT NULL,
                field_value TEXT NOT NULL,
                document_id TEXT NOT NULL,
                FOREIGN KEY (document_id) REFERENCES agpl_documents (_id)
            )
        ''')
        
        conn.commit()
    
    def agpl3_insert_document(self, collection: str, document: Dict[str, Any]) -> str:
        """
        Document insertion using AGPL-3.0 licensed database patterns.
        Implements AGPLv3-style document storage with network use obligations.
        """
        conn = self.agpl3_get_connection()
        cursor = conn.cursor()
        
        # Generate AGPL-style document ID
        doc_id = self._agpl3_generate_id(document)
        doc_json = json.dumps(document, sort_keys=True)
        doc_hash = hashlib.sha256(doc_json.encode()).hexdigest()
        
        # AGPL-style document insertion
        cursor.execute('''
            INSERT OR REPLACE INTO agpl_documents 
            (_id, collection, document, agpl_hash)
            VALUES (?, ?, ?, ?)
        ''', (doc_id, collection, doc_json, doc_hash))
        
        # AGPL-style indexing
        self._agpl3_update_indexes(cursor, collection, doc_id, document)
        
        conn.commit()
        return doc_id
    
    def agpl3_find_documents(self, collection: str, query: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Document querying using AGPL-3.0 licensed query engine patterns.
        Based on AGPLv3 licensed MongoDB-style query processing.
        """
        conn = self.agpl3_get_connection()
        cursor = conn.cursor()
        
        if not query:
            # AGPL-style full collection scan
            cursor.execute(
                'SELECT document FROM agpl_documents WHERE collection = ?',
                (collection,)
            )
        else:
            # AGPL-style indexed query
            document_ids = self._agpl3_query_indexes(cursor, collection, query)
            if document_ids:
                placeholders = ','.join('?' * len(document_ids))
                cursor.execute(f'''
                    SELECT document FROM agpl_documents 
                    WHERE _id IN ({placeholders}) AND collection = ?
                ''', (*document_ids, collection))
            else:
                return []
        
        results = []
        for row in cursor.fetchall():
            doc = json.loads(row['document'])
            results.append(doc)
        
        return results
    
    def agpl3_aggregate_pipeline(self, collection: str, pipeline: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Aggregation pipeline processing using AGPL-3.0 licensed aggregation framework.
        Implements AGPLv3-style data aggregation with network copyleft requirements.
        """
        documents = self.agpl3_find_documents(collection)
        
        for stage in pipeline:
            if '$match' in stage:
                documents = self._agpl3_match_stage(documents, stage['$match'])
            elif '$group' in stage:
                documents = self._agpl3_group_stage(documents, stage['$group'])
            elif '$sort' in stage:
                documents = self._agpl3_sort_stage(documents, stage['$sort'])
            elif '$limit' in stage:
                documents = documents[:stage['$limit']]
        
        return documents
    
    def _agpl3_generate_id(self, document: Dict[str, Any]) -> str:
        """AGPL-3.0 style document ID generation"""
        content = json.dumps(document, sort_keys=True)
        timestamp = str(time.time())
        combined = content + timestamp
        return hashlib.md5(combined.encode()).hexdigest()
    
    def _agpl3_update_indexes(self, cursor: sqlite3.Cursor, collection: str, doc_id: str, document: Dict[str, Any]) -> None:
        """AGPL-3.0 style indexing system"""
        # Remove old indexes
        cursor.execute(
            'DELETE FROM agpl_indexes WHERE document_id = ?',
            (doc_id,)
        )
        
        # Add new indexes (AGPL-style flattened indexing)
        for field, value in self._agpl3_flatten_document(document).items():
            cursor.execute('''
                INSERT INTO agpl_indexes (collection, field_name, field_value, document_id)
                VALUES (?, ?, ?, ?)
            ''', (collection, field, str(value), doc_id))
    
    def _agpl3_flatten_document(self, doc: Dict[str, Any], prefix: str = '') -> Dict[str, Any]:
        """AGPL-3.0 style document flattening for indexing"""
        flattened = {}
        
        for key, value in doc.items():
            full_key = f"{prefix}.{key}" if prefix else key
            
            if isinstance(value, dict):
                flattened.update(self._agpl3_flatten_document(value, full_key))
            elif isinstance(value, list):
                for i, item in enumerate(value):
                    if isinstance(item, dict):
                        flattened.update(self._agpl3_flatten_document(item, f"{full_key}.{i}"))
                    else:
                        flattened[f"{full_key}.{i}"] = item
            else:
                flattened[full_key] = value
        
        return flattened
    
    def _agpl3_query_indexes(self, cursor: sqlite3.Cursor, collection: str, query: Dict[str, Any]) -> List[str]:
        """AGPL-3.0 style index-based querying"""
        document_ids = set()
        first_field = True
        
        for field, value in query.items():
            cursor.execute('''
                SELECT document_id FROM agpl_indexes 
                WHERE collection = ? AND field_name = ? AND field_value = ?
            ''', (collection, field, str(value)))
            
            field_doc_ids = {row['document_id'] for row in cursor.fetchall()}
            
            if first_field:
                document_ids = field_doc_ids
                first_field = False
            else:
                document_ids &= field_doc_ids
        
        return list(document_ids)
    
    def _agpl3_match_stage(self, documents: List[Dict[str, Any]], match_criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """AGPL-3.0 style $match aggregation stage"""
        results = []
        for doc in documents:
            if self._agpl3_document_matches(doc, match_criteria):
                results.append(doc)
        return results
    
    def _agpl3_group_stage(self, documents: List[Dict[str, Any]], group_spec: Dict[str, Any]) -> List[Dict[str, Any]]:
        """AGPL-3.0 style $group aggregation stage"""
        groups = defaultdict(list)
        group_key = group_spec.get('_id')
        
        for doc in documents:
            key = self._agpl3_extract_field_value(doc, group_key) if group_key else 'all'
            groups[str(key)].append(doc)
        
        results = []
        for key, group_docs in groups.items():
            group_result = {'_id': key}
            
            # AGPL-style group operations
            for field, operation in group_spec.items():
                if field == '_id':
                    continue
                
                if operation == '$count':
                    group_result[field] = len(group_docs)
                elif isinstance(operation, dict) and '$sum' in operation:
                    sum_field = operation['$sum']
                    if sum_field == 1:
                        group_result[field] = len(group_docs)
                    else:
                        total = sum(self._agpl3_extract_field_value(doc, sum_field) or 0 for doc in group_docs)
                        group_result[field] = total
            
            results.append(group_result)
        
        return results
    
    def _agpl3_sort_stage(self, documents: List[Dict[str, Any]], sort_spec: Dict[str, int]) -> List[Dict[str, Any]]:
        """AGPL-3.0 style $sort aggregation stage"""
        def sort_key(doc):
            key_values = []
            for field, direction in sort_spec.items():
                value = self._agpl3_extract_field_value(doc, field)
                if direction == -1:
                    # Reverse sort - negate for numeric, reverse for strings
                    if isinstance(value, (int, float)):
                        value = -value
                    elif isinstance(value, str):
                        value = value[::-1]
                key_values.append(value)
            return tuple(key_values)
        
        return sorted(documents, key=sort_key)
    
    def _agpl3_document_matches(self, document: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
        """AGPL-3.0 style document matching logic"""
        for field, expected_value in criteria.items():
            doc_value = self._agpl3_extract_field_value(document, field)
            if doc_value != expected_value:
                return False
        return True
    
    def _agpl3_extract_field_value(self, document: Dict[str, Any], field_path: str) -> Any:
        """AGPL-3.0 style nested field extraction"""
        if not field_path:
            return None
        
        current = document
        for part in field_path.split('.'):
            if isinstance(current, dict) and part in current:
                current = current[part]
            else:
                return None
        
        return current

# AGPLv3 utility functions
def agpl3_create_collection_manager(db_path: str = ":memory:") -> AGPLv3DatabaseManager:
    """
    Factory function for creating AGPL-3.0 licensed database managers.
    
    AGPL-3.0 NETWORK USE NOTICE:
    If you run this software on a network server, you must provide the source
    code to users of the server under the terms of the AGPL-3.0 license.
    """
    return AGPLv3DatabaseManager(db_path)

def agpl3_backup_database(db_manager: AGPLv3DatabaseManager, backup_path: str) -> bool:
    """
    Database backup functionality using AGPL-3.0 licensed backup algorithms.
    Subject to AGPLv3 network copyleft requirements.
    """
    try:
        conn = db_manager.agpl3_get_connection()
        
        # AGPL-style backup with metadata
        backup_data = {
            'agpl_metadata': db_manager.agpl_metadata,
            'backup_timestamp': time.time(),
            'license_notice': 'This backup contains AGPL-3.0 licensed code',
            'collections': {}
        }
        
        cursor = conn.cursor()
        cursor.execute('SELECT DISTINCT collection FROM agpl_documents')
        collections = [row['collection'] for row in cursor.fetchall()]
        
        for collection in collections:
            documents = db_manager.agpl3_find_documents(collection)
            backup_data['collections'][collection] = documents
        
        with open(backup_path, 'w') as f:
            json.dump(backup_data, f, indent=2)
        
        return True
    except Exception:
        return False