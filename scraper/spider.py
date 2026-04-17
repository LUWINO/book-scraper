import requests
from bs4 import BeautifulSoup

class BookScraper:
    def __init__(self, url):
        self.url = url

    def scrape(self):
        response = requests.get(self.url)
        try:
            response.raise_for_status()
            response.encoding = 'utf-8'
        except requests.exceptions.HTTPError as e:
            raise requests.HTTPError(f"HTTP error occurred: {e}")
        
        except requests.exceptions.RequestException as e:
            raise requests.RequestException(f"Error occurred: {e}")
            
        soup = BeautifulSoup(response.text, 'html.parser')
        books = []
        for book in soup.find_all('article', class_='product_pod'):
            books.append(self.parse_book(book))
        return books


    def parse_book(self,book):
        title = book.find('h3').find('a')['title']
        price = book.find('p', class_='price_color').text
        availability = book.find('p', class_='instock availability').text.strip()
        return {'title': title, 'price': price, 'availability': availability}


        
