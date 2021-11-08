from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.deletion import CASCADE

# Create your models here.

class CustomerCompany(models.Model):
    user = models.ManyToManyField(User)
    repo = models.URLField(max_length=100)
    services = models.CharField()
    alerts = models.CharField()
    post_mordem = models.CharField()
    cadence = models.CharField()
    documentation_url = models.URLField()
    grafana_url = models.URLField()


class CustomerUser(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    company = models.OneToOneField(CustomerCompany, on_delete=CASCADE)
    git_user = models.CharField(max_length=30)
    git_token = models.CharField(max_length=200)


class Services(models.Model):
    pass

class Alerts(models.Model):
    pass

class Postmoderm(models.Model):
    pass

class Cadence (models.Model):
    pass