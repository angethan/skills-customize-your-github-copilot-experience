# 📘 Assignment: Web Scraping with BeautifulSoup

## 🎯 Objective

Learn how to extract data from web pages using Python and the BeautifulSoup library. You will practice making HTTP requests, parsing HTML, and organizing scraped data into useful formats.

## 📝 Tasks

### 🛠️ Parse HTML and Extract Basic Data

#### Description
Use BeautifulSoup to read an HTML file and extract specific elements from it.

#### Requirements
Completed program should:

- Import BeautifulSoup and the `requests` library.
- Load the provided `sample-page.html` file or fetch content from a URL.
- Find all paragraph (`<p>`) tags in the HTML.
- Extract and print the text from each paragraph.


### 🛠️ Extract Structured Data with CSS Selectors

#### Description
Use CSS selectors to find and extract specific data from HTML elements.

#### Requirements
Completed program should:

- Find all elements with a specific class (e.g., `class="product"`).
- Extract attributes from HTML tags (e.g., `href` from links, `src` from images).
- Store the extracted data in a list of dictionaries (e.g., `[{"name": "...", "price": "..."}, ...]`).


### 🛠️ Clean and Organize Scraped Data

#### Description
Process and clean the extracted data, then save it to a file.

#### Requirements
Completed program should:

- Remove extra whitespace and formatting from extracted text (using `.strip()`).
- Convert data types if needed (e.g., prices from strings to floats).
- Save the cleaned data to a CSV or JSON file.
- Print a summary showing how many items were extracted.


### 🛠️ Handle Real-World Challenges

#### Description
Extend your scraper to handle edge cases and errors gracefully.

#### Requirements
Completed program should:

- Use try/except blocks to handle cases where elements don't exist.
- Add a delay between requests if scraping multiple pages (using `time.sleep()`).
- Provide informative error messages if a URL is unreachable or HTML parsing fails.
