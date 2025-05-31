from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        managed = False
        db_table = 'students'


