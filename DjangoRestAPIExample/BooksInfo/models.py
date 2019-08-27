from django.db import models

class books(models.Model):
    book_name = models.CharField(max_length=10)
    author_name = models.CharField(max_length=10)
    book_price = models.IntegerField()
    book_quantity = models.IntegerField()
 
# Create a string representation
    def __str__(self):
        return self.book_name
