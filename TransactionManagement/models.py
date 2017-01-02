from UserManagement.models import Customer, Admin, AdminBranch, Accountant

from django.db import models






class Branch(models.Model):
    number = models.IntegerField()
    admin = models.OneToOneField(AdminBranch, null=True)



class Account(models.Model):
    number = models.IntegerField()
    customer = models.ForeignKey(Customer, null=True, blank=True)













