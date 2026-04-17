from scraper.spider import BookScraper
from scraper.exporter import export_to_csv

def main():
    try:
        url = 'http://books.toscrape.com/'
        scraper = BookScraper(url)
        books = scraper.scrape()
        export_to_csv(books)
        print("Books successfully scraped and exported to books.csv")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
