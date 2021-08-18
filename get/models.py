from django.db import models


# Create your models here.


class app(models.Model):
    number = models.IntegerField()
    password = models.CharField(max_length=20)

    def __str_(self):
        return str(self.number)
