import csv

def export_to_csv(books, filename='books.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['title', 'price', 'availability'])
        writer.writeheader()
        writer.writerows(books)