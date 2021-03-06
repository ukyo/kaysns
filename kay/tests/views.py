# -*- coding: utf-8 -*-

"""
Kay test views.

:Copyright: (c) 2009 Takashi Matsuo <tmatsuo@candit.jp> All rights reserved.
:license: BSD, see LICENSE for more details.
"""

from werkzeug import (
  unescape, redirect, Response,
)

from kay.utils import (
  local, render_to_response, url_for,
)
from kay.i18n import lazy_gettext as _
from kay.utils.decorators import maintenance_check, cron_only

@maintenance_check
def index(request):
  return Response("test")

@maintenance_check("tests/no_decorator")
def index2(request):
  return Response("test")

def no_decorator(request):
  return Response("test")

def oldpage(request):
  return Resposne("Old")

def newpage(request):
  return Response("New")
  
def countup(request):
  count = request.session.get('count', 0) + 1
  request.session['count'] = count
  return Response(str(count))

@cron_only
def cron(request):
    return Response("OK")
