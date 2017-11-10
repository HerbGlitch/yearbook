# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1510345807.1599536
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/adminNav.htm'
_template_uri = 'adminNav.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['header', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        user = context.get('user', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <title>Timpview Yearbook</title>\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\r\n    <link href="https://gitcdn.github.io/bootstrap-toggle/2.2.2/css/bootstrap-toggle.min.css" rel="stylesheet">\r\n    <script src="https://gitcdn.github.io/bootstrap-toggle/2.2.2/js/bootstrap-toggle.min.js"></script>\r\n    <!-- Fonts from google -->\r\n    <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">\r\n    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">\r\n')
        __M_writer('    ')
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n  </head>\r\n  <body>\r\n')
        if user.is_superuser:
            __M_writer('      <nav class="navbar navbar-inverse" style="margin-bottom:0px;">\r\n        <div class="container-fluid">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="navbar-header">\r\n            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n              <span class="sr-only"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n              <span class="icon-bar"></span>\r\n            </button>\r\n            <a class="navbar-brand logo" href="/">\r\n              <span style="color: #337ab7;"></span>\r\n            </a>\r\n          </div>\r\n          <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n            <ul class=" FontChanges nav navbar-nav navbar-left">\r\n              <li><a href="/customerList">will add</a></li>\r\n              <li><a href="/userList">will add</a></li>\r\n            </ul>\r\n            <ul class=" FontChanges nav navbar-nav navbar-right">\r\n              <li class="dropdown">\r\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">')
            __M_writer(str(request.user))
            __M_writer(' <span class="caret"></span></a>\r\n                <ul class="dropdown-menu">\r\n                  <!-- <li><a href="/">Profile</a></li>\r\n                  <li><a href="/">Account</a></li> -->\r\n')
            if request.user.is_authenticated():
                __M_writer('                    <li><a href="/logout">Logout</a></li>\r\n')
            else:
                __M_writer('                    <li><a href="/index">Login</a></li>\r\n')
            __M_writer('                </ul>\r\n              </li>\r\n            </ul>\r\n          </div><!-- /.navbar-collapse -->\r\n        </div><!-- /.container-fluid -->\r\n      </nav>\r\n      ')
            if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
                context['self'].content(**pageargs)
            

            __M_writer('\r\n')
            __M_writer('      ')
            __M_writer(str( django_mako_plus.link_js(self) ))
            __M_writer('\r\n')
        __M_writer('  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/adminNav.htm", "uri": "adminNav.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "29": 2, "30": 8, "31": 19, "32": 19, "33": 19, "38": 21, "39": 24, "40": 25, "41": 46, "42": 46, "43": 50, "44": 51, "45": 52, "46": 53, "47": 55, "52": 63, "53": 65, "54": 65, "55": 65, "56": 67, "62": 20, "68": 20, "74": 61, "80": 61, "86": 80}}
__M_END_METADATA
"""
