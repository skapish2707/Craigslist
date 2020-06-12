from django.db import models


class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    #to show text of data in admin interface
    def __str__(self):
        return '{}'.format(self.search)

    #To make correct plural
    class Meta:
        verbose_name_plural = 'Searches'