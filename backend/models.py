# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Account(models.Model):
    account_id = models.CharField(max_length=8)
    account_pass = models.CharField(max_length=16)
    account_email = models.CharField(max_length=25, default='')


class Photo(models.Model):
    photo_type = models.IntegerField(default=67)
    photo_photo = models.CharField(max_length=1024, default='')
    photo_account_id = models.CharField(max_length=8)

from django.db import models

# Create your models here.
