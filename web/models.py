from django.db import models

class Record(models.Model):
    cze = models.CharField("Word in CZech", max_length=200)
    eng = models.CharField("Word in ENglish", max_length=200)
    notes_cze = models.CharField("Notes about translation",
                             max_length=200, blank=True, null=True)
    notes_eng = models.CharField("Notes about translation",
                                 max_length=200, blank=True, null=True)
    special_cze = models.CharField(
        "Special notes", max_length=200, blank=True, null=True)
    special_eng = models.CharField(
        "Special notes", max_length=200, blank=True, null=True)
    translator = models.CharField(
        "Name of translator", max_length=200, blank=True, null=True)
    time_added = models.DateTimeField("Date of addition", blank=True, null=True)
    time_changed = models.DateTimeField(
        "Date of change", blank=True, null=True)

    def __str__(self):
        return f'{self.cz} - {self.en}' 
