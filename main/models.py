import datetime
from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=256)
    owner = models.ForeignKey('kid_auth.User', on_delete=models.CASCADE)
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

    mother_inv = models.OneToOneField('kid_auth.ParentInvitation', related_name='mother_inv', null=True,
                                      on_delete=models.SET_NULL)
    father_inv = models.OneToOneField('kid_auth.ParentInvitation', related_name='father_inv', null=True,
                                      on_delete=models.SET_NULL)

    mother = models.OneToOneField('kid_auth.User', related_name='mother', on_delete=models.CASCADE, null=True)
    father = models.OneToOneField('kid_auth.User', related_name='father', on_delete=models.CASCADE, null=True)

    groups = models.ForeignKey(ChildrenGroup, on_delete=models.SET_NULL, null=True)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def presence_today(self):
        presence = self.presences_set.filter(date=datetime.date.today()).first()
        return presence.is_present if presence else None


class Presences(models.Model):
    children = models.ForeignKey(Children, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.NullBooleanField()
