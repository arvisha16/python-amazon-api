import requests
from bs4 import BeautifulSoup

def get_amazon_item_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Assume the price is contained within a span with a specific class
        price_element = soup.find('span', {'aria-hidden'})


        if price_element:
            price = price_element.get_text(strip=True)
            return price
        else:
            return 'Price not found on the page.'

    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    item_url = input("Enter the Amazon item URL: ")
    item_price = get_amazon_item_price(item_url)
    print(f"The price of the item is: {item_price}")
