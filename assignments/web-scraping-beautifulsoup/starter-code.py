from bs4 import BeautifulSoup
import requests
import csv
import json
import time

# Sample HTML for testing (you can also use the sample-page.html file)
SAMPLE_HTML = """
<html>
  <head><title>Online Store</title></head>
  <body>
    <h1>Featured Products</h1>
    <div class="product">
      <h2>Laptop</h2>
      <p class="price">$999.99</p>
      <p class="description">High-performance laptop for work and gaming</p>
    </div>
    <div class="product">
      <h2>Mouse</h2>
      <p class="price">$29.99</p>
      <p class="description">Ergonomic wireless mouse</p>
    </div>
    <div class="product">
      <h2>Keyboard</h2>
      <p class="price">$79.99</p>
      <p class="description">Mechanical keyboard with RGB lighting</p>
    </div>
  </body>
</html>
"""


# Task 1: Parse HTML and extract basic data
def extract_paragraphs(html_content):
    """Extract all paragraph text from HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    paragraphs = []
    
    # TODO: Find all <p> tags and extract their text
    
    return paragraphs


# Task 2: Extract structured data with CSS selectors
def extract_products(html_content):
    """Extract product data from HTML using CSS selectors"""
    soup = BeautifulSoup(html_content, 'html.parser')
    products = []
    
    # TODO: Find all elements with class="product"
    # TODO: For each product, extract name, price, and description
    # TODO: Store each product as a dictionary in the products list
    
    return products


# Task 3: Clean and save data
def save_products_to_file(products, filename="products.csv"):
    """Save product data to CSV or JSON file"""
    
    # TODO: Clean the data (strip whitespace, convert types)
    # TODO: Save to CSV or JSON file
    # TODO: Print summary of how many items were saved
    
    pass


# Task 4: Handle errors and make requests
def fetch_and_scrape(url):
    """Fetch a URL and scrape its content with error handling"""
    
    # TODO: Use try/except to handle request errors
    # TODO: Check if the response was successful
    # TODO: Parse the HTML and extract data
    # TODO: Return the extracted data or error message
    
    pass


# Example usage
if __name__ == "__main__":
    # Test with sample HTML
    print("Extracting paragraphs...")
    paragraphs = extract_paragraphs(SAMPLE_HTML)
    print(f"Found {len(paragraphs)} paragraphs")
    
    print("\nExtracting products...")
    products = extract_products(SAMPLE_HTML)
    print(f"Found {len(products)} products")
    for product in products:
        print(f"  - {product}")
