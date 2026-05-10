import os
import csv
from scraper.exporter import export_to_csv

def test_export_to_csv():
    books = [
        {'title': 'A Light in the Attic', 'price': '£51.77', 'availability': 'In stock'},
        {'title': 'Tipping the Velvet', 'price': '£53.74', 'availability': 'In stock'}
    ]

    export_to_csv(books, filename='test_books.csv')
    assert os.path.exists('test_books.csv')
    with open('test_books.csv', 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert rows[0]['title'] == 'A Light in the Attic'
        assert rows[0]['price'] == '£51.77'
        assert rows[0]['availability'] == 'In stock'
        assert rows[1]['title'] == 'Tipping the Velvet'
        assert rows[1]['price'] == '£53.74'
        assert rows[1]['availability'] == 'In stock'
    os.remove('test_books.csv')

