# DecureDOM - DOM Simplification for Language Models

This project simplifies the Document Object Model (DOM) of a web page to enhance its understanding by Language Models (LMs). The simplified DOM retains essential elements and attributes related to user intent while removing unnecessary elements. This README provides an overview of the choices made during the development of this project.

## Language and Framework

- **Language**: Python
- **Framework**: BeautifulSoup

**Why Python?**

Python is a versatile and widely-adopted programming language known for its simplicity, readability, and extensive libraries. It offers excellent support for web scraping and DOM manipulation, making it a suitable choice for this project.

**Why BeautifulSoup?**

Beautiful Soup is a Python library that specializes in parsing and manipulating HTML and XML documents. It simplifies complex HTML parsing tasks and allows for easy navigation and modification of the DOM structure. This library was chosen due to its simplicity and effectiveness in web scraping tasks.

## DOM Reduction Process

The core functionality of this project involves reducing the complexity of the DOM structure. Here's an overview of the steps taken to achieve this:

### 1. Fetching HTML Content

- We use the `requests` library to send an HTTP GET request to the specified URL, obtaining the HTML content of the webpage.

### 2. HTML Parsing

- BeautifulSoup is employed to parse the fetched HTML content, creating a parse tree that simplifies traversal and manipulation of the DOM.

### 3. Removing Unwanted Tags

- Various tags that are considered non-essential for understanding user intent are removed. These tags include 'script,' 'meta,' 'link,' 'style,' 'noscript,' 'base,' 'source,' 'track,' 'path,' and 'svg.'

### 4. Mapping Elements by Role

- Specific HTML elements are mapped to more generic ones based on their roles. For instance:
    - 'textarea' and 'input' elements are transformed into 'i' (input) elements.
    - Structural elements such as 'div,' 'section,' 'article,' 'main,' 'nav,' 'header,' and 'footer' are represented as 'c' (containers).
    - Textual elements such as 'h1,' 'h2,' 'h3,' 'h4,' 'h5,' 'h6,' 'p,' and 'span' are denoted as 't' (text).
    - Hyperlinks ('a' elements) are tagged as 'l' (links).
    - Buttons ('button' elements) are identified as 'b' (buttons).
    - Media elements like 'img' and 'video' are simplified to 'm' (media).

### 5. Retaining Useful Attributes

- A predefined list of attributes that are generally useful for understanding content is maintained. These attributes include 'href,' 'src,' 'alt,' 'title,' 'role,' and attributes starting with 'aria-'.

### 6. Removing Non-Useful Attributes

- Attributes that do not fall within the list of useful attributes are removed from the remaining elements in the DOM. This step helps in streamlining the DOM while retaining essential information.

### 7. Saving the Simplified DOM

- The simplified DOM, which is now represented as a BeautifulSoup object, is converted back into a string format. This simplified HTML is then appended to an 'output.txt' file for further analysis and use.

## Usage

To use this script:

1. Modify the `URL` variable in the code to specify the target URL.
2. Run the script, and it will simplify the DOM structure of the specified webpage and save it to 'output.txt'.

## Conclusion

This project demonstrates how to simplify a webpage's DOM to improve its understanding by Language Models. The choice of Python and BeautifulSoup was made based on their effectiveness and simplicity in web scraping and DOM manipulation tasks.
