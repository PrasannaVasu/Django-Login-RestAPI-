# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Userdetails(models.Model):
  username = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  email = models.CharField(max_length=50)
  comments = models.CharField(max_length=50)
  publish = models.DateField(auto_now = False , auto_now_add = False)
  
  def __str__(self):
     return self.username