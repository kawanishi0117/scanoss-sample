"""
Creative Commons Licensed Content Processing Module
This module contains code and content derived from CC licensed materials for testing.

Creative Commons Attribution 4.0 International License (CC BY 4.0)
This work is licensed under a Creative Commons Attribution 4.0 International License.
You should have received a copy of the license along with this work.
If not, see <http://creativecommons.org/licenses/by/4.0/>.

Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)
Some portions are licensed under CC BY-SA 4.0
See <http://creativecommons.org/licenses/by-sa/4.0/>.

Creative Commons Attribution-NonCommercial 4.0 International License (CC BY-NC 4.0)
Some portions are licensed under CC BY-NC 4.0
See <http://creativecommons.org/licenses/by-nc/4.0/>.
"""

import re
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from datetime import datetime

# CC-BY-4.0 Licensed Content Templates
CC_BY_CONTENT_TEMPLATES = {
    'documentation': """
    This documentation template is licensed under CC BY 4.0.
    
    Attribution: Original work by Creative Commons Contributors
    License: Creative Commons Attribution 4.0 International
    License URL: http://creativecommons.org/licenses/by/4.0/
    
    You are free to:
    - Share — copy and redistribute the material in any medium or format
    - Adapt — remix, transform, and build upon the material
    
    Under the following terms:
    - Attribution — You must give appropriate credit, provide a link to the license,
      and indicate if changes were made.
    """,
    
    'tutorial': """
    Tutorial Content (CC BY 4.0)
    
    This tutorial demonstrates basic concepts and is freely available for educational use.
    
    Licensed under Creative Commons Attribution 4.0 International License.
    Original authors: Community Contributors
    Source: https://example.com/cc-by-tutorials
    
    Step 1: Understanding the basics
    Step 2: Practical implementation
    Step 3: Advanced techniques
    """,
    
    'examples': """
    Code Examples Collection (CC BY 4.0)
    
    These examples are provided under Creative Commons Attribution 4.0 license.
    Feel free to use, modify, and distribute with proper attribution.
    
    Example 1: Basic data processing
    Example 2: Advanced algorithms
    Example 3: Integration patterns
    """
}

# CC-BY-SA-4.0 Licensed Content Templates
CC_BY_SA_CONTENT_TEMPLATES = {
    'wiki_style': """
    Wiki-Style Documentation (CC BY-SA 4.0)
    
    This content is licensed under Creative Commons Attribution-ShareAlike 4.0 International License.
    
    Attribution-ShareAlike: You must give appropriate credit and license derivatives
    under the same license.
    
    Original contributors: Community Wiki Authors
    License: http://creativecommons.org/licenses/by-sa/4.0/
    
    ## Overview
    This is collaborative documentation that follows Wikipedia-style licensing.
    
    ## Technical Details
    Detailed technical information with community contributions.
    
    ## Community Guidelines
    Guidelines for contributing to this shared knowledge base.
    """,
    
    'educational': """
    Educational Content (CC BY-SA 4.0)
    
    Educational materials licensed under Creative Commons Attribution-ShareAlike 4.0.
    
    Course: Introduction to Data Processing
    Instructors: CC Educational Community
    License: Creative Commons Attribution-ShareAlike 4.0 International
    
    Lesson 1: Fundamentals
    Lesson 2: Practical Applications
    Lesson 3: Advanced Topics
    
    Note: Derivative works must be licensed under the same terms.
    """
}

# CC-BY-NC-4.0 Licensed Content Templates
CC_BY_NC_CONTENT_TEMPLATES = {
    'research': """
    Research Content (CC BY-NC 4.0)
    
    This research content is licensed under Creative Commons Attribution-NonCommercial 4.0 International License.
    
    Research Title: Advanced Data Analysis Techniques
    Authors: Academic Research Community
    License: http://creativecommons.org/licenses/by-nc/4.0/
    
    Abstract:
    This research explores advanced techniques in data analysis...
    
    Methodology:
    The research methodology follows established academic practices...
    
    Results:
    Our findings indicate significant improvements in processing efficiency...
    
    Note: Commercial use is not permitted under this license.
    """,
    
    'artistic': """
    Artistic Content (CC BY-NC 4.0)
    
    Creative work licensed under Creative Commons Attribution-NonCommercial 4.0.
    
    Title: Data Visualization Art
    Artist: CC Creative Community
    Medium: Digital art generated from data patterns
    
    Description:
    This artistic interpretation of data patterns creates visually appealing
    representations of complex datasets.
    
    Usage: Non-commercial use only with attribution required.
    License: Creative Commons Attribution-NonCommercial 4.0 International
    """
}

@dataclass
class CCLicensedContent:
    """
    Data class for Creative Commons licensed content.
    
    This class structure is provided under CC BY 4.0 license.
    """
    title: str
    content: str
    license_type: str
    attribution: str
    license_url: str
    commercial_use: bool
    derivative_works: bool
    share_alike: bool

class CCContentProcessor:
    """
    Content processing utilities for Creative Commons licensed materials.
    
    This processor handles various CC license types and ensures proper attribution.
    
    License: Mixed Creative Commons licenses (see individual methods)
    """
    
    def __init__(self):
        self.cc_metadata = {
            'cc_by_4_0': {
                'commercial_use': True,
                'derivative_works': True,
                'share_alike': False,
                'attribution_required': True
            },
            'cc_by_sa_4_0': {
                'commercial_use': True,
                'derivative_works': True,
                'share_alike': True,
                'attribution_required': True
            },
            'cc_by_nc_4_0': {
                'commercial_use': False,
                'derivative_works': True,
                'share_alike': False,
                'attribution_required': True
            }
        }
    
    def process_cc_by_content(self, content_type: str) -> CCLicensedContent:
        """
        Process CC BY 4.0 licensed content.
        
        This method is licensed under Creative Commons Attribution 4.0 International License.
        Attribution: Creative Commons Community
        """
        template = CC_BY_CONTENT_TEMPLATES.get(content_type, CC_BY_CONTENT_TEMPLATES['documentation'])
        
        return CCLicensedContent(
            title=f"CC BY 4.0 {content_type.title()} Content",
            content=template,
            license_type="CC BY 4.0",
            attribution="Creative Commons Contributors",
            license_url="http://creativecommons.org/licenses/by/4.0/",
            commercial_use=True,
            derivative_works=True,
            share_alike=False
        )
    
    def process_cc_by_sa_content(self, content_type: str) -> CCLicensedContent:
        """
        Process CC BY-SA 4.0 licensed content.
        
        This method is licensed under Creative Commons Attribution-ShareAlike 4.0 International License.
        Derivative works must be licensed under the same terms.
        """
        template = CC_BY_SA_CONTENT_TEMPLATES.get(content_type, CC_BY_SA_CONTENT_TEMPLATES['wiki_style'])
        
        return CCLicensedContent(
            title=f"CC BY-SA 4.0 {content_type.title()} Content",
            content=template,
            license_type="CC BY-SA 4.0",
            attribution="CC Wiki Community",
            license_url="http://creativecommons.org/licenses/by-sa/4.0/",
            commercial_use=True,
            derivative_works=True,
            share_alike=True
        )
    
    def process_cc_by_nc_content(self, content_type: str) -> CCLicensedContent:
        """
        Process CC BY-NC 4.0 licensed content.
        
        This method handles non-commercial Creative Commons content.
        License: Creative Commons Attribution-NonCommercial 4.0 International
        Commercial use is not permitted.
        """
        template = CC_BY_NC_CONTENT_TEMPLATES.get(content_type, CC_BY_NC_CONTENT_TEMPLATES['research'])
        
        return CCLicensedContent(
            title=f"CC BY-NC 4.0 {content_type.title()} Content",
            content=template,
            license_type="CC BY-NC 4.0",
            attribution="CC Research Community",
            license_url="http://creativecommons.org/licenses/by-nc/4.0/",
            commercial_use=False,
            derivative_works=True,
            share_alike=False
        )
    
    def extract_cc_metadata(self, content: str) -> Dict[str, Any]:
        """
        Extract Creative Commons license metadata from content.
        
        This utility function is provided under CC BY 4.0 license.
        """
        cc_patterns = {
            'cc_by_4_0': r'CC BY 4\.0|Creative Commons Attribution 4\.0',
            'cc_by_sa_4_0': r'CC BY-SA 4\.0|Creative Commons Attribution-ShareAlike 4\.0',
            'cc_by_nc_4_0': r'CC BY-NC 4\.0|Creative Commons Attribution-NonCommercial 4\.0',
            'cc_license_url': r'creativecommons\.org/licenses/[^/]+/4\.0',
            'attribution': r'Attribution[:\s]+([^\n]+)'
        }
        
        metadata = {
            'detected_licenses': [],
            'license_urls': [],
            'attributions': []
        }
        
        for license_type, pattern in cc_patterns.items():
            matches = re.findall(pattern, content, re.IGNORECASE)
            if matches:
                if license_type.startswith('cc_'):
                    metadata['detected_licenses'].extend(matches)
                elif license_type == 'cc_license_url':
                    metadata['license_urls'].extend(matches)
                elif license_type == 'attribution':
                    metadata['attributions'].extend(matches)
        
        return metadata
    
    def validate_cc_compliance(self, content: CCLicensedContent, usage_context: Dict[str, Any]) -> Dict[str, bool]:
        """
        Validate Creative Commons license compliance.
        
        This compliance checker is provided under CC BY 4.0 license.
        """
        license_info = self.cc_metadata.get(content.license_type.lower().replace(' ', '_').replace('-', '_'), {})
        
        compliance = {
            'attribution_provided': bool(content.attribution),
            'license_specified': bool(content.license_type),
            'license_url_provided': bool(content.license_url)
        }
        
        # Check commercial use compliance
        if not license_info.get('commercial_use', True):
            compliance['commercial_use_compliant'] = not usage_context.get('commercial_use', False)
        else:
            compliance['commercial_use_compliant'] = True
        
        # Check share-alike compliance
        if license_info.get('share_alike', False):
            if usage_context.get('creating_derivative', False):
                compliance['share_alike_compliant'] = usage_context.get('same_license', False)
            else:
                compliance['share_alike_compliant'] = True
        else:
            compliance['share_alike_compliant'] = True
        
        compliance['overall_compliant'] = all(compliance.values())
        
        return compliance

# Creative Commons utility functions
def create_cc_attribution(author: str, title: str, license_type: str, source_url: str = None) -> str:
    """
    Create proper Creative Commons attribution.
    
    This function is licensed under CC BY 4.0.
    Attribution: Creative Commons Community
    """
    attribution = f'"{title}" by {author} is licensed under {license_type}'
    
    if source_url:
        attribution += f'. Source: {source_url}'
    
    license_urls = {
        'CC BY 4.0': 'http://creativecommons.org/licenses/by/4.0/',
        'CC BY-SA 4.0': 'http://creativecommons.org/licenses/by-sa/4.0/',
        'CC BY-NC 4.0': 'http://creativecommons.org/licenses/by-nc/4.0/'
    }
    
    if license_type in license_urls:
        attribution += f'\nLicense: {license_urls[license_type]}'
    
    return attribution

def cc_content_library() -> Dict[str, List[CCLicensedContent]]:
    """
    Generate a library of Creative Commons licensed content for testing.
    
    This library contains mixed CC licenses for comprehensive testing.
    Library compilation: CC BY 4.0
    """
    processor = CCContentProcessor()
    library = {
        'cc_by_4_0': [],
        'cc_by_sa_4_0': [],
        'cc_by_nc_4_0': []
    }
    
    # CC BY 4.0 content
    for content_type in CC_BY_CONTENT_TEMPLATES.keys():
        library['cc_by_4_0'].append(processor.process_cc_by_content(content_type))
    
    # CC BY-SA 4.0 content
    for content_type in CC_BY_SA_CONTENT_TEMPLATES.keys():
        library['cc_by_sa_4_0'].append(processor.process_cc_by_sa_content(content_type))
    
    # CC BY-NC 4.0 content
    for content_type in CC_BY_NC_CONTENT_TEMPLATES.keys():
        library['cc_by_nc_4_0'].append(processor.process_cc_by_nc_content(content_type))
    
    return library

# Mixed Creative Commons content for testing
MIXED_CC_CONTENT = """
Educational Content Collection

This collection contains content under various Creative Commons licenses:

1. Tutorial Section (CC BY 4.0)
   Basic programming tutorials licensed under Creative Commons Attribution 4.0.
   Source: https://example.com/tutorials
   Attribution: Programming Community Contributors

2. Documentation (CC BY-SA 4.0) 
   Technical documentation licensed under Creative Commons Attribution-ShareAlike 4.0.
   Derivative works must use the same license.
   Attribution: Technical Writing Community

3. Research Papers (CC BY-NC 4.0)
   Academic research content licensed under Creative Commons Attribution-NonCommercial 4.0.
   Commercial use prohibited.
   Attribution: Academic Research Network

4. Creative Works (CC BY-NC-SA 4.0)
   Artistic content with non-commercial and share-alike requirements.
   Attribution: Creative Arts Community
   License: http://creativecommons.org/licenses/by-nc-sa/4.0/

This mixed-license collection demonstrates various Creative Commons licensing scenarios
for comprehensive license detection testing.
"""