# -*- coding: utf-8 -*-
# app.models

from google.appengine.ext import db
from kay.auth.models import DatastoreUser

# Create your models here.

class MyUser(DatastoreUser):
    tags = db.StringListProperty()
    description = db.TextProperty()