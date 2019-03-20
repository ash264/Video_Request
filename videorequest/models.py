from django.db import models
from datetime import date
from datetime import datetime

class Video(models.Model):
    title=models.CharField(max_length=20)
    text=models.TextField()
    date_added=models.DateTimeField(default=datetime.now(),blank=True)

    def __str__(self):
        return 'Title: {} Id: {}'.format(self.title,self.id)
