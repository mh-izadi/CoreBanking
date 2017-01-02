from django.contrib.auth.models import User
from django.db import models


class Admin(models.Model):
    user = models.OneToOneField(User)

class AdminBranch(models.Model):
    user = models.OneToOneField(User)

class Accountant(models.Model):
    user = models.OneToOneField(User)

class Cashier(models.Model):
    user = models.OneToOneField(User)

class LegalExpert(models.Model):
    user = models.OneToOneField(User)

class Customer(models.Model):
    user = models.OneToOneField(User)
