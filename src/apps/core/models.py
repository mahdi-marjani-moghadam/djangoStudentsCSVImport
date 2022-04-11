from abc import abstractmethod
from django.db import models
from django.http import Http404
from django.urls import reverse



class baseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-id']
    
    @classmethod
    def get_by_pk(cls, pk, raise_exception=False):
        obj = cls.objects.filter(pk=pk).first()
        if raise_exception and not obj:
            raise Http404('The requested entity is not found')
        return obj

    def get_absolute_url(self):
        return reverse(self.__class__+"-detail", kwargs={"pk": self.pk})

class PaginationSearchable:
    @classmethod
    @abstractmethod
    def get_searchable_fields(cls):
        return []