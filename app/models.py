import uuid
from django.db import models

# Create your models here.

# Match between two users
class Match(models.Model):
    username1 = models.CharField(max_length=50)
    username2 = models.CharField(max_length=50)
    phone1 = models.IntegerField(unique=False)
    phone2 = models.IntegerField(unique=False)
    created_at = models.DateTimeField(auto_now_add=True)
    uid = models.CharField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        self.uid = uuid.uuid4().hex[:6].upper()
        super(Match, self).save(*args, **kwargs)


    def __str__(self):
        return self.username1 + ", " + self.username2 + " - " + self.uid