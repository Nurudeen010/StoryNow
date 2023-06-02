from django.db import models

class Detail(models.Model):
    title = models.CharField(max_length=256, blank=False)
    story = models.TextField(blank=False)

    def __str__(self):
        return self.title