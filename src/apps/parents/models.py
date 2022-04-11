from django.db import models

from apps.core.models import PaginationSearchable, baseModel


class parents(baseModel, PaginationSearchable):

    @classmethod
    def get_searchable_fields(cls):
        return [
            'name',
            'age'
        ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return "{}".format(self.name)
