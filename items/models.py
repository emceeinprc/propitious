from django.db import models

CATEGORY_CHOICES = (
    ('holiday', 'Holiday'),
    ('breaking_news', "Breaking News"),
)

class Item(models.Model):
    item_title = models.CharField(max_length=200)
    date = models.DateTimeField('date occuring')
    category = models.CharField(max_length = 200, choices = CATEGORY_CHOICES)
