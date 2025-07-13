"""
Data processing module using pandas (BSD-3-Clause license).
"""

import pandas as pd
import json
from typing import Dict, List, Any

class DataProcessor:
    def __init__(self):
        self.data = pd.DataFrame()
        
    def load_json_data(self, json_data: str) -> pd.DataFrame:
        """Load JSON data into pandas DataFrame"""
        try:
            data = json.loads(json_data)
            self.data = pd.DataFrame(data)
            return self.data
        except json.JSONDecodeError:
            return pd.DataFrame()
    
    def clean_data(self) -> pd.DataFrame:
        """Clean and normalize data using pandas operations"""
        if not self.data.empty:
            # Remove duplicates
            self.data = self.data.drop_duplicates()
            
            # Fill missing values
            self.data = self.data.fillna('')
            
            # Normalize text columns
            text_columns = self.data.select_dtypes(include=['object']).columns
            for col in text_columns:
                self.data[col] = self.data[col].str.strip().str.lower()
        
        return self.data
    
    def export_to_csv(self, filename: str) -> bool:
        """Export processed data to CSV using pandas"""
        try:
            self.data.to_csv(filename, index=False)
            return True
        except Exception:
            return False
    
    def get_summary_stats(self) -> Dict[str, Any]:
        """Generate summary statistics using pandas describe"""
        if not self.data.empty:
            return self.data.describe().to_dict()
        return {}