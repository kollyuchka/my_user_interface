
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Users(models.Model):
    user_id = models.IntegerField(default = 1)
    full_name = models.CharField(max_length=60)