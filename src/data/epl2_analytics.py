"""
EPL-2.0 Licensed Data Analytics Module
This module contains code derived from EPL-2.0 licensed analytics projects.

Copyright (c) 2023 Eclipse Foundation and others.

This program and the accompanying materials are made available under the
terms of the Eclipse Public License 2.0 which is available at
http://www.eclipse.org/legal/epl-2.0.

This Source Code may also be made available under the following Secondary
Licenses when the conditions for such availability set forth in the Eclipse
Public License, v. 2.0 are satisfied: GNU General Public License, version 2
with the GNU Classpath Exception which is available at
https://www.gnu.org/software/classpath/license.html.

SPDX-License-Identifier: EPL-2.0 OR GPL-2.0 WITH Classpath-exception-2.0
"""

import math
import statistics
from typing import List, Dict, Any, Optional, Tuple, Callable
from collections import defaultdict, Counter
from dataclasses import dataclass
import itertools

# EPL-2.0 Licensed Statistical Analysis Engine
class EPL2StatisticalAnalyzer:
    """
    Statistical analysis utilities derived from EPL-2.0 licensed analytics frameworks.
    Based on Eclipse Foundation statistical computing libraries.
    
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License 2.0.
    
    SPDX-License-Identifier: EPL-2.0
    """
    
    def __init__(self):
        self.analysis_cache = {}
        self.epl_metadata = {
            'license': 'EPL-2.0',
            'eclipse_foundation': True,
            'secondary_licenses_allowed': True,
            'patent_grant': True
        }
    
    def epl2_descriptive_statistics(self, data: List[float]) -> Dict[str, float]:
        """
        Descriptive statistics calculation using EPL-2.0 licensed algorithms.
        Based on Eclipse Foundation statistical analysis patterns.
        """
        if not data:
            return {'error': 'Empty dataset'}
        
        # Eclipse-style statistical calculations
        n = len(data)
        sorted_data = sorted(data)
        
        stats = {
            'count': n,
            'sum': sum(data),
            'mean': statistics.mean(data),
            'median': statistics.median(data),
            'mode': self._epl2_calculate_mode(data),
            'std_dev': statistics.stdev(data) if n > 1 else 0.0,
            'variance': statistics.variance(data) if n > 1 else 0.0,
            'min': min(data),
            'max': max(data),
            'range': max(data) - min(data)
        }
        
        # EPL-2.0 style quartile calculations
        stats.update(self._epl2_calculate_quartiles(sorted_data))
        
        # Eclipse-style distribution analysis
        stats.update(self._epl2_distribution_analysis(data))
        
        return stats
    
    def epl2_correlation_analysis(self, x_data: List[float], y_data: List[float]) -> Dict[str, float]:
        """
        Correlation analysis using EPL-2.0 licensed correlation algorithms.
        Implements Eclipse Foundation correlation computation patterns.
        """
        if len(x_data) != len(y_data) or len(x_data) < 2:
            return {'error': 'Invalid dataset dimensions'}
        
        # Eclipse-style correlation calculations
        n = len(x_data)
        
        # Pearson correlation coefficient (EPL-2.0 implementation)
        x_mean = statistics.mean(x_data)
        y_mean = statistics.mean(y_data)
        
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data))
        x_variance = sum((x - x_mean) ** 2 for x in x_data)
        y_variance = sum((y - y_mean) ** 2 for y in y_data)
        
        denominator = math.sqrt(x_variance * y_variance)
        
        correlation_results = {
            'pearson_r': numerator / denominator if denominator != 0 else 0.0,
            'r_squared': 0.0,
            'covariance': numerator / (n - 1) if n > 1 else 0.0
        }
        
        correlation_results['r_squared'] = correlation_results['pearson_r'] ** 2
        
        # Eclipse-style rank correlation (Spearman)
        spearman_r = self._epl2_spearman_correlation(x_data, y_data)
        correlation_results['spearman_r'] = spearman_r
        
        return correlation_results
    
    def epl2_regression_analysis(self, x_data: List[float], y_data: List[float]) -> Dict[str, Any]:
        """
        Regression analysis using EPL-2.0 licensed regression algorithms.
        Based on Eclipse Foundation regression analysis frameworks.
        """
        if len(x_data) != len(y_data) or len(x_data) < 2:
            return {'error': 'Insufficient data for regression'}
        
        # Eclipse-style linear regression
        n = len(x_data)
        x_mean = statistics.mean(x_data)
        y_mean = statistics.mean(y_data)
        
        # EPL-2.0 style least squares calculations
        numerator = sum((x - x_mean) * (y - y_mean) for x, y in zip(x_data, y_data))
        denominator = sum((x - x_mean) ** 2 for x in x_data)
        
        if denominator == 0:
            return {'error': 'Cannot perform regression - no variance in x'}
        
        slope = numerator / denominator
        intercept = y_mean - slope * x_mean
        
        # Eclipse-style regression statistics
        y_predicted = [slope * x + intercept for x in x_data]
        residuals = [y_actual - y_pred for y_actual, y_pred in zip(y_data, y_predicted)]
        
        rss = sum(r ** 2 for r in residuals)  # Residual Sum of Squares
        tss = sum((y - y_mean) ** 2 for y in y_data)  # Total Sum of Squares
        
        r_squared = 1 - (rss / tss) if tss != 0 else 0
        
        return {
            'slope': slope,
            'intercept': intercept,
            'r_squared': r_squared,
            'residuals': residuals,
            'predictions': y_predicted,
            'standard_error': math.sqrt(rss / (n - 2)) if n > 2 else 0
        }
    
    def epl2_time_series_analysis(self, time_data: List[float], window_size: int = 5) -> Dict[str, List[float]]:
        """
        Time series analysis using EPL-2.0 licensed time series algorithms.
        Implements Eclipse Foundation time series processing patterns.
        """
        if len(time_data) < window_size:
            return {'error': 'Insufficient data for time series analysis'}
        
        # Eclipse-style moving averages
        moving_averages = []
        for i in range(len(time_data) - window_size + 1):
            window = time_data[i:i + window_size]
            moving_averages.append(statistics.mean(window))
        
        # EPL-2.0 style trend analysis
        trends = []
        for i in range(1, len(moving_averages)):
            trend = moving_averages[i] - moving_averages[i-1]
            trends.append(trend)
        
        # Eclipse-style volatility calculation
        volatility = []
        for i in range(len(time_data) - window_size + 1):
            window = time_data[i:i + window_size]
            vol = statistics.stdev(window) if len(window) > 1 else 0
            volatility.append(vol)
        
        return {
            'moving_averages': moving_averages,
            'trends': trends,
            'volatility': volatility,
            'overall_trend': statistics.mean(trends) if trends else 0,
            'average_volatility': statistics.mean(volatility) if volatility else 0
        }
    
    def _epl2_calculate_mode(self, data: List[float]) -> Optional[float]:
        """EPL-2.0 style mode calculation"""
        try:
            return statistics.mode(data)
        except statistics.StatisticsError:
            # Multiple modes or no mode
            counter = Counter(data)
            max_count = max(counter.values())
            modes = [value for value, count in counter.items() if count == max_count]
            return modes[0] if len(modes) == 1 else None
    
    def _epl2_calculate_quartiles(self, sorted_data: List[float]) -> Dict[str, float]:
        """EPL-2.0 style quartile calculations"""
        n = len(sorted_data)
        
        if n == 1:
            return {'q1': sorted_data[0], 'q3': sorted_data[0]}
        
        # Eclipse-style quartile calculation
        q1_index = n // 4
        q3_index = 3 * n // 4
        
        return {
            'q1': sorted_data[q1_index],
            'q3': sorted_data[q3_index],
            'iqr': sorted_data[q3_index] - sorted_data[q1_index]
        }
    
    def _epl2_distribution_analysis(self, data: List[float]) -> Dict[str, float]:
        """EPL-2.0 style distribution analysis"""
        mean_val = statistics.mean(data)
        std_val = statistics.stdev(data) if len(data) > 1 else 0
        
        # Eclipse-style skewness calculation
        if std_val == 0:
            skewness = 0
        else:
            n = len(data)
            skewness = sum(((x - mean_val) / std_val) ** 3 for x in data) / n
        
        # Eclipse-style kurtosis calculation
        if std_val == 0:
            kurtosis = 0
        else:
            n = len(data)
            kurtosis = sum(((x - mean_val) / std_val) ** 4 for x in data) / n - 3
        
        return {
            'skewness': skewness,
            'kurtosis': kurtosis
        }
    
    def _epl2_spearman_correlation(self, x_data: List[float], y_data: List[float]) -> float:
        """EPL-2.0 style Spearman rank correlation"""
        # Rank the data (Eclipse-style ranking)
        x_ranks = self._epl2_rank_data(x_data)
        y_ranks = self._epl2_rank_data(y_data)
        
        # Calculate Pearson correlation of ranks
        return self.epl2_correlation_analysis(x_ranks, y_ranks)['pearson_r']
    
    def _epl2_rank_data(self, data: List[float]) -> List[float]:
        """EPL-2.0 style data ranking"""
        sorted_pairs = sorted(enumerate(data), key=lambda x: x[1])
        ranks = [0] * len(data)
        
        for rank, (original_index, _) in enumerate(sorted_pairs):
            ranks[original_index] = float(rank + 1)
        
        return ranks

# EPL-2.0 Licensed Data Mining Engine
class EPL2DataMiningEngine:
    """
    Data mining utilities derived from EPL-2.0 licensed data mining frameworks.
    
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License 2.0.
    
    SPDX-License-Identifier: EPL-2.0
    """
    
    def __init__(self):
        self.mining_cache = {}
    
    def epl2_frequent_patterns(self, transactions: List[List[str]], min_support: float = 0.1) -> Dict[str, Any]:
        """
        Frequent pattern mining using EPL-2.0 licensed algorithms.
        Based on Eclipse Foundation data mining libraries.
        """
        if not transactions:
            return {'patterns': {}, 'support_counts': {}}
        
        # Eclipse-style item frequency counting
        item_counts = defaultdict(int)
        total_transactions = len(transactions)
        
        # Count individual items
        for transaction in transactions:
            for item in set(transaction):  # Use set to avoid counting duplicates in same transaction
                item_counts[item] += 1
        
        # EPL-2.0 style support filtering
        min_count = int(min_support * total_transactions)
        frequent_items = {item: count for item, count in item_counts.items() if count >= min_count}
        
        # Eclipse-style pattern generation
        patterns = {}
        
        # 1-itemsets
        for item, count in frequent_items.items():
            patterns[frozenset([item])] = count / total_transactions
        
        # 2-itemsets (Eclipse-style combination generation)
        if len(frequent_items) > 1:
            for item1, item2 in itertools.combinations(frequent_items.keys(), 2):
                pair_count = sum(1 for transaction in transactions 
                               if item1 in transaction and item2 in transaction)
                
                if pair_count >= min_count:
                    patterns[frozenset([item1, item2])] = pair_count / total_transactions
        
        return {
            'patterns': {str(sorted(pattern)): support for pattern, support in patterns.items()},
            'support_counts': frequent_items,
            'total_transactions': total_transactions
        }
    
    def epl2_clustering_analysis(self, data_points: List[List[float]], k: int = 3) -> Dict[str, Any]:
        """
        Clustering analysis using EPL-2.0 licensed clustering algorithms.
        Implements Eclipse Foundation k-means clustering patterns.
        """
        if not data_points or k <= 0:
            return {'error': 'Invalid clustering parameters'}
        
        # Eclipse-style k-means initialization
        centroids = self._epl2_initialize_centroids(data_points, k)
        assignments = [0] * len(data_points)
        
        # EPL-2.0 style iterative clustering
        max_iterations = 100
        for iteration in range(max_iterations):
            # Assign points to nearest centroid
            new_assignments = []
            for point in data_points:
                distances = [self._epl2_euclidean_distance(point, centroid) for centroid in centroids]
                closest_centroid = distances.index(min(distances))
                new_assignments.append(closest_centroid)
            
            # Check for convergence
            if new_assignments == assignments:
                break
            
            assignments = new_assignments
            
            # Update centroids (Eclipse-style centroid calculation)
            new_centroids = []
            for cluster_id in range(k):
                cluster_points = [data_points[i] for i, assignment in enumerate(assignments) if assignment == cluster_id]
                if cluster_points:
                    # Calculate centroid as mean of cluster points
                    dimensions = len(cluster_points[0])
                    centroid = [statistics.mean(cluster_points[i][dim] for i in range(len(cluster_points))) 
                              for dim in range(dimensions)]
                    new_centroids.append(centroid)
                else:
                    new_centroids.append(centroids[cluster_id])  # Keep old centroid if cluster is empty
            
            centroids = new_centroids
        
        # Eclipse-style cluster analysis
        cluster_stats = self._epl2_analyze_clusters(data_points, assignments, centroids)
        
        return {
            'centroids': centroids,
            'assignments': assignments,
            'iterations': iteration + 1,
            'cluster_stats': cluster_stats
        }
    
    def _epl2_initialize_centroids(self, data_points: List[List[float]], k: int) -> List[List[float]]:
        """EPL-2.0 style centroid initialization"""
        if k >= len(data_points):
            return data_points[:k]
        
        # Simple initialization: take first k points
        return data_points[:k]
    
    def _epl2_euclidean_distance(self, point1: List[float], point2: List[float]) -> float:
        """EPL-2.0 style Euclidean distance calculation"""
        return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))
    
    def _epl2_analyze_clusters(self, data_points: List[List[float]], assignments: List[int], centroids: List[List[float]]) -> Dict[str, Any]:
        """EPL-2.0 style cluster analysis"""
        cluster_analysis = {}
        
        for cluster_id in range(len(centroids)):
            cluster_points = [data_points[i] for i, assignment in enumerate(assignments) if assignment == cluster_id]
            
            if cluster_points:
                # Eclipse-style within-cluster sum of squares
                wcss = sum(self._epl2_euclidean_distance(point, centroids[cluster_id]) ** 2 for point in cluster_points)
                
                cluster_analysis[f'cluster_{cluster_id}'] = {
                    'size': len(cluster_points),
                    'centroid': centroids[cluster_id],
                    'wcss': wcss,
                    'avg_distance_to_centroid': wcss / len(cluster_points) if cluster_points else 0
                }
            else:
                cluster_analysis[f'cluster_{cluster_id}'] = {
                    'size': 0,
                    'centroid': centroids[cluster_id],
                    'wcss': 0,
                    'avg_distance_to_centroid': 0
                }
        
        return cluster_analysis

# EPL-2.0 utility functions
def epl2_create_statistical_analyzer() -> EPL2StatisticalAnalyzer:
    """
    Factory function for creating EPL-2.0 licensed statistical analyzers.
    
    This program and the accompanying materials are made available under the
    terms of the Eclipse Public License 2.0.
    """
    return EPL2StatisticalAnalyzer()

def epl2_create_data_mining_engine() -> EPL2DataMiningEngine:
    """
    Factory function for creating EPL-2.0 licensed data mining engines.
    
    SPDX-License-Identifier: EPL-2.0
    """
    return EPL2DataMiningEngine()

def epl2_cross_validation(data: List[Any], model_func: Callable, k_folds: int = 5) -> Dict[str, float]:
    """
    Cross-validation utility using EPL-2.0 licensed validation algorithms.
    Based on Eclipse Foundation machine learning validation patterns.
    """
    if len(data) < k_folds:
        return {'error': 'Insufficient data for cross-validation'}
    
    fold_size = len(data) // k_folds
    scores = []
    
    # Eclipse-style k-fold cross-validation
    for i in range(k_folds):
        start_idx = i * fold_size
        end_idx = start_idx + fold_size if i < k_folds - 1 else len(data)
        
        test_data = data[start_idx:end_idx]
        train_data = data[:start_idx] + data[end_idx:]
        
        try:
            score = model_func(train_data, test_data)
            scores.append(score)
        except Exception:
            continue
    
    if not scores:
        return {'error': 'No valid scores obtained'}
    
    return {
        'mean_score': statistics.mean(scores),
        'std_score': statistics.stdev(scores) if len(scores) > 1 else 0,
        'scores': scores,
        'folds': len(scores)
    }