from unittest.mock import patch, Mock
from scraper.spider import BookScraper

def test_scrape_returns_books():
    with patch('scraper.spider.requests.get') as mock_get:
        mock_get.return_value.status_code = 200
    
        FAKE_HTML = '''
    <html>
    <body>
        <article class="product_pod">
            <h3><a title="A Light in the Attic">A Light in the ...</a></h3>
            <p class="price_color">£51.77</p>
            <p class="instock availability">In stock</p>
        </article>
        <article class="product_pod">
            <h3><a title="Tipping the Velvet">Tipping the Velvet</a></h3>
            <p class="price_color">£53.74</p>
            <p class="instock availability">In stock</p>
        </article>
    </body>
    </html>
    '''
        mock_get.return_value.text = FAKE_HTML
        scraper = BookScraper('http://books.toscrape.com/')
        books = scraper.scrape()
        assert len(books) == 2
        assert books[0]['title'] == 'A Light in the Attic'
        assert books[0]['price'] == '£51.77'
        assert books[0]['availability'] == 'In stock'
        assert books[1]['title'] == 'Tipping the Velvet'
        assert books[1]['price'] == '£53.74'
        assert books[1]['availability'] == 'In stock'
        