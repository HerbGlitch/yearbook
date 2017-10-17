# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1508269548.4657564
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/navbar.htm'
_template_uri = 'navbar.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['header', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <title>Timpview Yearbook</title>\r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\r\n    <link href="https://gitcdn.github.io/bootstrap-toggle/2.2.2/css/bootstrap-toggle.min.css" rel="stylesheet">\r\n    <script src="https://gitcdn.github.io/bootstrap-toggle/2.2.2/js/bootstrap-toggle.min.js"></script>\r\n    <!-- Fonts from google -->\r\n    <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">\r\n    <link href="https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet" integrity="sha384-wvfXpqpZZVQGK6TAh5PVlGOfQNHSoD2xbE+QkPxCAFlNEevoEH3Sl0sibVcOQVnN" crossorigin="anonymous">\r\n')
        __M_writer('    ')
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n  </head>\r\n  <body>\r\n  \t\t<nav style="margin-bottom:0px;" id="mobilized_navbar_fix" class="navbar">\r\n\t\t<!-- <nav style="border-bottom:none; margin-bottom:0px; background-color: transparent; border-radius: 1px;" id="mobilized_navbar_fix" class="navbar"> -->\r\n\t\t    <div class="container-fluid">\r\n\t\t      <!-- Brand and toggle get grouped for better mobile display -->\r\n\t\t      <div class="navbar-header">\r\n\t\t        <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n\t\t          <span class="glyphicon glyphicon-menu-hamburger"></span>\r\n\t\t          <span class="sr-only">Toggle navigation</span>\r\n\t\t          <span class="icon-bar"></span>\r\n\t\t          <span class="icon-bar"></span>\r\n\t\t          <span class="icon-bar"></span>\r\n\t\t        </button>\r\n\r\n\t\t        <a class="navbar-brand" href="/index">\r\n\t\t          <!--<img style="height:50px; width:200px; margin-top:-15px;" src="http://placehold.it/150x50&text=Logo" alt="Nutrition For Wellness">-->\r\n\t\t          <h1 id="siteName" style="margin-left: 10px; margin-top: -5px; color: orange">Timpview<span style="color:#337AB7">Yearbook</span></h1>\r\n\t\t        </a>\r\n\t\t      </div>\r\n\r\n\t\t      <!-- Collect the nav links, forms, and other content for toggling -->\r\n\t\t      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\t\t        <ul class="nav navbar-nav navbar-right">\r\n\t\t          <li><a href="/student-life">Student Life</a></li>\r\n\t\t          <li><a href="/clubs">Clubs</a></li>\r\n\t\t          <li><a href="/staffers">Staffers</a></li>\r\n\t\t          <li><a href="/student-life">Student Life</a></li>\r\n\t              <li class="dropdown">\r\n\t                <a class="dropdown-toggle" data-toggle="dropdown" href="#">Profile<span class="caret"></span></a>\r\n\t                  <ul class="dropdown-menu"></ul>\r\n\t              </li>\r\n\t\t          </ul>\r\n\t\t        </div><!-- /.navbar-collapse -->\r\n\t\t      </div><!-- /.container-fluid -->\r\n\t\t    </nav>\r\n\t    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\t    ')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\r\n  </body>\r\n</html>')
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
        __M_writer('\r\n')
        __M_writer('\t    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/navbar.htm", "uri": "navbar.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "27": 2, "28": 8, "29": 19, "30": 19, "31": 19, "36": 21, "41": 60, "42": 62, "43": 62, "44": 62, "50": 20, "56": 20, "62": 58, "68": 58, "69": 60, "75": 69}}
__M_END_METADATA
"""
