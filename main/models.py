from django.db import models
from django.contrib.auth.models import User

PARENT = 1
CREW = 2
DIRECTOR = 3
USER_TYPE = (
    (PARENT, 'rodzic'),
    (CREW, 'opiekun'),
    (DIRECTOR, 'dyrektor')
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE)
    institution = models.ForeignKey('Institution', on_delete=models.SET_NULL, null=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class Institution(models.Model):
    name = models.CharField(max_length=256)
    street = models.CharField(max_length=256)
    town = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)


class ChildrenGroup(models.Model):
    name = models.CharField(max_length=256)


class Address(models.Model):
    street = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=10)
    town = models.CharField(max_length=64)


class Children(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    mother = models.ForeignKey(User, related_name='mother', on_delete=models.CASCADE)
    father = models.ForeignKey(User, related_name='father', on_delete=models.CASCADE)

    groups = models.ForeignKey(ChildrenGroup, on_delete=models.SET_NULL, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    presence = models.ManyToManyField('Presences')


class Presences(models.Model):
    date = models.DateTimeField()
    presence = models.BooleanField
