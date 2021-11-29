from django.contrib.auth.models import User
from django.db import models


class Medic(models.Model):
    name = models.CharField(max_length=50)
    specialty = models.CharField(max_length=200)
    crm = models.CharField(max_length=20)
    photo = models.ImageField(blank=True, upload_to='photo/')

    def __str__(self):
        return self.name


class Consultation(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    medic = models.ForeignKey(Medic, on_delete=models.DO_NOTHING)
    date = models.DateField(blank=True, null=True)
    created = models.DateField(auto_now_add=True, blank=True, null=True)


    def __str__(self):
        return  f'{self.user.first_name}-{self.created}'
