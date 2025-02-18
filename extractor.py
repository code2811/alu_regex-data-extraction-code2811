import re
from typing import List

class DataExtractor:
    """A utility class for extracting various data types using regular expressions."""
    
    def __init__(self):
        # Email pattern matches standard email formats including those with subdomains
        self.email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        
        # URL pattern matches http/https URLs with optional subdomains and paths
        self.url_pattern = r'https?://(?:www\.)?[a-zA-Z0-9-]+(?:\.[a-zA-Z]{2,})+(?:/[^\s]*)?'
        
        # Phone pattern matches common US/Canada phone number formats
        self.phone_pattern = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]\d{4}'
        
        # Currency pattern matches dollar amounts with optional thousands separators
        self.currency_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'

    def extract_emails(self, text: str) -> List[str]:
        """Extract email addresses from text."""
        return re.findall(self.email_pattern, text)
    
    def extract_urls(self, text: str) -> List[str]:
        """Extract URLs from text."""
        return re.findall(self.url_pattern, text)
    
    def extract_phone_numbers(self, text: str) -> List[str]:
        """Extract phone numbers from text."""
        return re.findall(self.phone_pattern, text)
    
    def extract_currency(self, text: str) -> List[str]:
        """Extract currency amounts from text."""
        return re.findall(self.currency_pattern, text)

if __name__ == "__main__":
    # Test the implementation
    sample_text = """
    Contact us at user@example.com or support.team@company.co.uk
    Visit our website at https://www.example.com or https://subdomain.example.org/page
    Call us at (123) 456-7890 or 987-654-3210
    Products starting from $19.99 to $1,234.56
    """
    
    extractor = DataExtractor()
    
    # Test and print results
    print("\nEmails found:", extractor.extract_emails(sample_text))
    print("\nURLs found:", extractor.extract_urls(sample_text))
    print("\nPhone numbers found:", extractor.extract_phone_numbers(sample_text))
    print("\nCurrency amounts found:", extractor.extract_currency(sample_text))
