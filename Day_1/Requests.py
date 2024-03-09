import requests
from bs4 import BeautifulSoup


def fetch_wikipedia_page(title=None):
    if not title:
        url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
    else:
        url = f"https://en.wikipedia.org/wiki/{title}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching Wikipedia page: {e}")
        return None


def extract_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    # Extract text from paragraph tags
    paragraphs = soup.find_all('p')
    text = "\n".join([p.get_text() for p in paragraphs])
    return text


def save_to_file(content, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Content saved to {filename}")


def main():
    title = input("Enter the title of the Wikipedia page or skip and get info about Python: ")
    content = fetch_wikipedia_page(title)
    if content:
        text_content = extract_text(content)
        if title:
            filename = f"{title.replace(' ', '_')}.txt"
        else:
            filename = "PaythonProgLang.txt"
        save_to_file(text_content, filename)


if __name__ == "__main__":
    main()
