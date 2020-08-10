"""
References:
    - https://docs.djangoproject.com/en/3.0/topics/db/managers/

:keyword: Managers, models.QuerySet, and so on.
"""

from django.db import models


class BookQuerySet(models.QuerySet):
    """ several kinds of queryset. """
    def get_all(self):
        """
        get all book.
        :return:
        """
        return self.all()

    def get_book_for_less_100_pages(self):
        """
        get book for less 100 pages.
        :return:
        """
        return self.filter(page__lte=100)


class Book(models.Model):
    """ Table: the db schema definition of Book. """
    name = models.CharField(max_length=100)
    page = models.IntegerField(default=0)
    price = models.IntegerField(default=0)

    objects = BookQuerySet.as_manager()

    class Meta:
        db_table = 'book'
        app_label = 'app'
        managed = True

    def __str__(self):
        return self.name
