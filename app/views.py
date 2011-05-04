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

from werkzeug import redirect

from kay.utils import (
    render_to_response, url_for
    )
from app.models import (
    MyUser, BbsThread, BbsComment
    )
from app.forms import (
    UserForm, BbsThreadForm, BbsCommentForm
    )
from kay.auth.decorators import login_required

# Create your views here.

def index(request):
    return render_to_response('app/index.html', {'request': request})

@login_required
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

@login_required
def bbs(request):
    form = BbsThreadForm()
    threads = BbsThread.all().order('-created')
    if request.method == 'POST':
        if form.validate(request.form):
            form.save()
            return redirect(url_for('app/bbs/index'))
    return render_to_response('app/bbs/index.html', {'form': form.as_widget(),
                                                     'threads': threads})
                                                     
@login_required
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
