# -*- coding: utf-8 -*-
"""
app.views
"""

"""
import logging

from google.appengine.api import users
from google.appengine.api import memcache
from werkzeug import (
  unescape, redirect, Response,
)
from werkzeug.exceptions import (
  NotFound, MethodNotAllowed, BadRequest
)

from kay.utils import (
  render_to_response, reverse,
  get_by_key_name_or_404, get_by_id_or_404,
  to_utc, to_local_timezone, url_for, raise_on_dev
)
from kay.i18n import gettext as _
from kay.auth.decorators import login_required

"""

from google.appengine.ext import db
from google.appengine.api import images

from werkzeug import redirect, Response

from kay.utils import (
    render_to_response, url_for, render_to_string
    )
from app.models import (
    MyUser, BbsThread, BbsComment, BlogEntry, Image
    )
from app.forms import (
    UserForm, BbsThreadForm, BbsCommentForm, BlogEntryForm,
    BlogCommentForm, ImageForm
    )
from kay.auth.decorators import login_required, admin_required
from kay.utils.paginator import Paginator, InvalidPage, EmptyPage
from kay.auth import create_new_user

# Create your views here.

def create_paginator_page(request, query, length=10):
    #show http://kay-docs-jp.shehas.net/pagination.html
    paginator = Paginator(query, length)
    
    try:
        page = int(request.args.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        return paginator.page(page)
    except (EmptyPage, InvalidPage):
        return paginator.page(paginator.num_page)
    
    
def render_paginator(paginator_page):
    return render_to_string('app/paginator.html', {'page': paginator_page})
    
    
def index(request):
    return render_to_response('app/index.html')


def manage_profile(request):
    form = UserForm(request.user)
    data = {}
    if request.method == 'POST':
        if form.validate(request.form):
            form.save()
            data['validate'] = u'成功しました。'
        else:
            data['validate'] = u'失敗しました。'
    data['form'] = form.as_widget()
    return render_to_response('app/manage-profile.html', data)


def bbs(request):
    form = BbsThreadForm()
    threads_all = BbsThread.all().order('-created')
    threads = create_paginator_page(request, threads_all)
    if request.method == 'POST':
        if form.validate(request.form):
            form.save()
            return redirect(url_for('app/bbs/index'))
    return render_to_response('app/bbs/index.html', {'form': form.as_widget(),
                                                     'threads': threads,
                                                     'paginator': render_paginator(threads)})
                                                     
                                                     
def bbs_thread(request, id):
    form = BbsCommentForm()
    thread = BbsThread.get_by_id(id)
    if request.method == 'POST':
        if form.validate(request.form):
            form.save(thread=thread)
            thread.put()
            return redirect('/bbs/%d' % id)
    return render_to_response('app/bbs/thread.html', {'form': form.as_widget(),
                                                      'thread': thread})
                                                      
                                                      
def blog(request, user_name):
    user = MyUser.all().filter('user_name', user_name).get()
    query = BlogEntry.all().filter('user', user).order('-created')
    entries = create_paginator_page(request, query)
    return render_to_response('app/blog/index.html', {'user_name': user_name,
                                                      'entries': entries,
                                                      'paginator': render_paginator(entries)})


def blog_entry(request, user_name, id):
    form = BlogCommentForm()
    entry = BlogEntry.get_by_id(id)
    if request.method == 'POST':
        if form.validate(request.form):
            form.save(entry=entry)
            return redirect('/%s/blog/%d' % (user_name, id))
    return render_to_response('app/blog/entry.html', {'user_name': user_name,
                                                      'entry': entry,
                                                      'form': form.as_widget()})


def blog_manage(request):
    query = BlogEntry.all().filter('user', request.user).order('-created')
    entries = create_paginator_page(request, query)
    return render_to_response('app/blog/manage.html', {'entries': entries,
                                                       'paginator': render_paginator(entries)})


def blog_create_entry_base(request, form, template):
    if request.method == 'POST':
        if form.validate(request.form):
            form.save()
            return redirect(url_for('app/blog/manage'))
    return render_to_response(template, {'form': form.as_widget()})


def blog_create_entry(request):
    return blog_create_entry_base(request, BlogEntryForm(), 'app/blog/create.html')


def blog_update_entry(request, id):
    return blog_create_entry_base(request, BlogEntryForm(BlogEntry.get_by_id(id)), 'app/blog/update.html')
    
    
def blog_check_delete_entry(request, id):
    return render_to_response('app/blog/delete.html', {'entry': BlogEntry.get_by_id(id)})
    
    
def blog_delete_entry(request, id):
    entry = BlogEntry.get_by_id(id)
    db.delete(entry.comments)
    db.delete(entry)
    return redirect(url_for('app/blog/manage'))
    
    
def setting_image(request):
    form = ImageForm()
    if request.method == 'POST':
        if form.validate(request.form, request.files):
            image = Image.all().filter('user', request.user).get()
            if image:
                icon = request.files['icon'] or image.icon
                background_image = request.files['background_image'] or image.background_image
            else:
                icon = None
                background_image = None
            form.save(icon=icon, background_image=background_image)
            return redirect(url_for('app/index'))
    return render_to_response('app/setting/image.html', {'form': form.as_widget()})
    
    
def icon(request, user_name, width, height):
    user = MyUser.all().filter('user_name', user_name).get()
    icon = Image.all().filter('user', user).get().icon
    return Response(mimetype='image/png', response=images.resize(icon, width, height))
    
    
def background_image(request, user_name):
    user = MyUser.all().filter('user_name', user_name).get()
    background_image = Image.all().filter('user', user).get().background_image
    return Response(mimetype='image/png', response=images.rotate(background_image, 0))
    
@admin_required
def admin_create_user(request, user_name, password, is_admin):
    create_new_user(user_name, password, is_admin=bool(is_admin))
    return Response(response='ok')