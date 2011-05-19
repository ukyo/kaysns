# -*- coding: utf-8 -*-

from kay.utils.forms.modelform import ModelForm
from app.models import (
    MyUser, BbsThread, BbsComment,
    BlogEntry, BlogComment, Icon
)

class UserForm(ModelForm):
    class Meta:
        model = MyUser
        exclude = ('is_admin', 'activated', 'user_name', 'password')

        
class BbsThreadForm(ModelForm):
    class Meta:
        model = BbsThread
        exclude = ('user', )


class BbsCommentForm(ModelForm):
    class Meta:
        model = BbsComment
        exclude = ('user', 'thread')
        
        
class BlogEntryForm(ModelForm):
    class Meta:
        model = BlogEntry
        exclude = ('user', )
        

class BlogCommentForm(ModelForm):
    class Meta:
        model = BlogComment
        exclude = ('user', 'entry')
        
        
class IconForm(ModelForm):
    class Meta:
        model = Icon
        exclude = ('user', )