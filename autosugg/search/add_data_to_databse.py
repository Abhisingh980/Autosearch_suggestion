from .models import BookSummary
import csv

def add_data_to_database():

    with open('/Users/abhisingh/Downloads/books_summary.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            book = BookSummary()
            book.book_name = row['book_name']
            book.summaries = row['summaries']
            book.categories = row['categories']
            book.save()
