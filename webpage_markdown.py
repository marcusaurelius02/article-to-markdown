import requests
from bs4 import BeautifulSoup
import markdownify  # pip install markdownify

def create_markdown_from_webpage(url, output_filename="output.md"):
    """
    Reads a webpage, extracts the main text content, and saves it as a Markdown file.

    Args:
        url (str): The URL of the webpage to process.
        output_filename (str, optional): The name of the Markdown file to create. Defaults to "output.md".
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # --- Specific to Medium.com (inspect the page source for best selectors) ---
    # This is the most crucial part:  Finding the right HTML elements
    # Medium articles are typically within a <div class="e eJ"> or similar structure. Inspect the page!
    article_content = soup.find('div', class_='e eJ')  # Or a more specific class if you find one

    if not article_content:
        print("Could not find article content.  Check your selectors!")
        return

    # Convert HTML to Markdown
    markdown_text = markdownify.markdownify(str(article_content))

    # Save to a Markdown file
    try:
        with open(output_filename, "w", encoding="utf-8") as f:  # Specify encoding!
            f.write(markdown_text)
        print(f"Markdown file created: {output_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Example usage:
url = "https://medium.com/@rrpinc/priorities-of-a-great-engineering-leader-9bba11bd005d"
create_markdown_from_webpage(url, "engineering_leadership.md")