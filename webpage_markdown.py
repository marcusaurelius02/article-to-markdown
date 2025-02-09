import requests
from bs4 import BeautifulSoup
import markdownify

def create_markdown_from_webpage(url, output_filename="output.md"):
    """
    Reads a webpage, extracts the main text content, and saves it as a Markdown file.

    Args:
        url (str): The URL of the webpage to process.
        output_filename (str, optional): The name of the Markdown file to create. Defaults to "output.md".
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return

    soup = BeautifulSoup(response.content, 'html.parser')

    # --- Specific to brittonbroderick.com ---
    # Find the main article element.  We'll use the 'article' tag.
    article_content = soup.find('article')  # This is the important change
    if not article_content:
        print("Could not find article content. Check your selectors!")
        return

    # Convert HTML to Markdown
    markdown_text = markdownify.markdownify(str(article_content))

    # Save to a Markdown file
    try:
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(markdown_text)
        print(f"Markdown file created: {output_filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Example usage:
# Used https://www.linkedin.com/posts/kachchani_this-is-your-shortcut-to-better-tech-leadership-activity-7278035916646932480-HnWq/?utm_source=share&utm_medium=member_ios
#url = "https://brittonbroderick.com/2024/08/18/building-aggressively-helpful-teams/"
#url ="https://stackoverflow.blog/2024/12/31/generative-ai-is-not-going-to-build-your-engineering-team-for-you/"
url ="https://newsletter.getdx.com/p/developer-use-case-with-ai-tools"
url = "https://lauratacho.com/blog/dumb-leadership-mistakes-ive-made"
url = "https://sdtimes.com/softwaredev/dirty-code-still-runs-but-thats-not-a-good-thing/"
create_markdown_from_webpage(url, "dirty-code-not-good-thing.md")