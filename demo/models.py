from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=255, db_index=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    contents = models.ManyToManyField(Content)

    def __str__(self):
        return self.name
