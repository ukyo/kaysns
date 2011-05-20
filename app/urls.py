# -*- coding: utf-8 -*-
# app.urls
# 

# Following few lines is an example urlmapping with an older interface.
"""
from werkzeug.routing import EndpointPrefix, Rule

def make_rules():
  return [
    EndpointPrefix('app/', [
      Rule('/', endpoint='index'),
    ]),
  ]

all_views = {
  'app/index': 'app.views.index',
}
"""

from kay.routing import (
  ViewGroup, Rule
)

view_groups = [
  ViewGroup(
    Rule('/', endpoint='index', view='app.views.index'),
    Rule('/manage-profile', endpoint='manage-profile', view='app.views.manage_profile'),
    Rule('/bbs', endpoint='bbs/index', view='app.views.bbs'),
    Rule('/bbs/<int:id>', endpoint='bbs/thread', view='app.views.bbs_thread'),
    Rule('/blog/manage', endpoint='blog/manage', view='app.views.blog_manage'),
    Rule('/blog/create', endpoint='blog/create', view='app.views.blog_create_entry'),
    Rule('/blog/update/<int:id>', endpoint='blog/update', view='app.views.blog_update_entry'),
    Rule('/blog/delete/check/<int:id>', endpoint='blog/delete/check', view='app.views.blog_check_delete_entry'),
    Rule('/blog/delete/<int:id>', endpoint='blog/delete', view='app.views.blog_delete_entry'),
    Rule('/<user_name>/blog', endpoint='blog/index', view='app.views.blog'),
    Rule('/<user_name>/blog/<int:id>', endpoint='blog/entry', view='app.views.blog_entry'),
    Rule('/setting/icon', endpoint='setting/icon', view='app.views.setting_icon'),
    Rule('/<user_name>/icon_<int:width>x<int:height>.png', endpoint='icon', view='app.views.icon'),
    Rule('/uploader', endpoint='uploader', view='app.views.uploader'),
    Rule('/uploader/download/<int:id>/<filename>', endpoint='uploader/download', view='app.views.uploader_download'),
    Rule('/uploader/delete/check/<int:id>', endpoint='uploader/delete/check', view='app.views.uploader_check_delete'),
    Rule('/uploader/delete/<int:id>', endpoint='uploader/delete', view='app.views.uploader_delete'),
  )
]

