from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MaxValueValidator


class Car(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    make = models.CharField(max_length=25)
    model = models.CharField(max_length=40)
    year = models.IntegerField(validators=[MaxValueValidator(2023)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
