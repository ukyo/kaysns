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
    Rule('/setting/image', endpoint='setting/image', view='app.views.setting_image'),
    Rule('/<user_name>/icon_<int:width>x<int:height>.png', endpoint='icon', view='app.views.icon'),
    Rule('/<user_name>/background_image.png', endpoint='background_image', view='app.views.background_image'),
    Rule('/admin/create_user/<user_name>/<password>/<int:is_admin>', endpoint='admin/create_user', view='app.views.admin_create_user'),
  )
]

