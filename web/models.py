from django.db import models

class Record(models.Model):
    cz = models.CharField("Word in CZech", max_length=200)
    en = models.CharField("Word in ENglish", max_length=200)
    notes = models.CharField("Notes about translation", max_length=200)
    special = models.CharField("Special notes", max_length=200)
    translator = models.CharField("Name of translator", max_length=200)

    def __str__(self):
        return self.name
