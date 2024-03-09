import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching page: {e}")
        return None


def scrape_items(html_content):
    items = []
    soup = BeautifulSoup(html_content, 'html.parser')
    product_cards = soup.find_all('div', class_='thumbnail')
    for card in product_cards:
        name = card.find('a', class_='title').text.strip()
        price = card.find('h4', class_='pull-right').text.strip()
        description = card.find('p', class_='description').text.strip()
        items.append({'Name': name, 'Price': price, 'Description': description})
    return items


def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(f"Name: {item['Name']}\n")
            f.write(f"Price: {item['Price']}\n")
            f.write(f"Description: {item['Description']}\n\n")
    print(f"Scraped data saved to {filename}")


def main():
    url = "https://webscraper.io/test-sites/e-commerce/allinone"
    html_content = fetch_page(url)
    if html_content:
        items = scrape_items(html_content)
        save_to_file(items, "scraped_data.txt")


if __name__ == "__main__":
    main()
