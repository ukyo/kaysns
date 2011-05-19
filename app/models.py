# -*- coding: utf-8 -*-
# app.models

from google.appengine.ext import db
from kay.auth.models import DatastoreUser
import kay.db

# Create your models here.

class MyUser(DatastoreUser):
    tags = db.StringListProperty()
    description = db.TextProperty()
    
class ViewMixin(object):
    def view_text(self):
        if self.newline_to_br:
            return self.text.replace('\r\n', '\n').replace('\n', '<br/>')
        else:
            return self.text
    
    def view_datetime(self, attr_name):
        attr = getattr(self, attr_name)
        return attr.strftime('%Y/%m/%d %H:%M:%S')
        
        
class Thread(db.Model, ViewMixin):
    user = kay.db.OwnerProperty()
    title = db.StringProperty(required=True)
    tags = db.StringListProperty()
    text = db.TextProperty(required=True)
    newline_to_br = db.BooleanProperty(default=True)
    created = db.DateTimeProperty(auto_now_add=True)

class Comment(db.Model, ViewMixin):
    user = kay.db.OwnerProperty()
    title = db.StringProperty(required=True)
    text = db.TextProperty(required=True)
    newline_to_br = db.BooleanProperty()
    created = db.DateTimeProperty(auto_now_add=True)
    
class BbsThread(Thread):
    updated = db.DateTimeProperty(auto_now=True)
    
class BbsComment(Comment):
    thread = db.ReferenceProperty(BbsThread, collection_name='comments')
    
class BlogEntry(Thread):
    pass
    
class BlogComment(Comment):
    entry = db.ReferenceProperty(BlogEntry, collection_name='comments')
    
class Icon(db.Model):
    user = kay.db.OwnerProperty()
    image = db.BlobProperty(required=True)