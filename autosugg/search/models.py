from django.db import models

#create a book summary model

class BookSummary(models.Model):
    book_name = models.CharField(max_length=255)
    summaries = models.TextField()
    categories = models.CharField(max_length=100)

    def __str__(self):
        return str(self.book_name)
