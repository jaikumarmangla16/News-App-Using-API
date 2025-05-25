
# News API Reader

This Python project fetches the latest news articles based on a user's query using the [NewsAPI](https://newsapi.org/) and saves the results to a text file.

## Features
- User inputs a search query.
- Retrieves recent news articles related to the query.
- Displays article details (title, description, URL, published date) in the console.
- Saves the same details to a `news.txt` file.

## Requirements
- Python 3.x
- `requests` library

Install required packages using pip:
```bash
pip install requests
```

## How to Use
1. Replace `your_Api_key_here` in the code with your actual NewsAPI key. You can get one by registering at [newsapi.org](https://newsapi.org/).
2. Run the script:
```bash
main.py
```
3. Enter a search query when prompted.
4. The script will print and save the latest articles.

## Output
- Console: Displays a numbered list of articles with their titles, descriptions, URLs, and published dates.
- File: A `news.txt` file is created with the same content, encoded in UTF-8.

## Example
```
Enter your query: technology
...
news.txt created with latest articles.
```

## Notes
- Make sure your API key is valid.
- The script filters news from 2025-04-25 onwards.
- If special characters are present, they are correctly handled using UTF-8 encoding.

---
Made with Python and NewsAPI 📄
