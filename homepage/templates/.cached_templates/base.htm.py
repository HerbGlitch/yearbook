# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519157485.5148735
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['header', 'content']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        page_href = context.get('page_href', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def header():
            return render_header(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\r\n<html>\r\n\t<meta charset="UTF-8">\r\n\t<head>\r\n\t\t<title>Timpview Yearbook</title>\r\n')
        __M_writer('\t\t<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n\t\t<!-- Latest compiled and minified CSS -->\r\n\t\t<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">\r\n\t\t<!-- Latest compiled and minified JavaScript -->\r\n\t\t<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js"></script>\r\n\t\t<!-- Fonts from google -->\r\n\t\t<link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">\r\n\t\t<script defer src="https://use.fontawesome.com/releases/v5.0.6/js/all.js"></script>\r\n\t\t')
        __M_writer(str( django_mako_plus.link_css(self) ))
        __M_writer('\r\n\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\r\n\t</head>\r\n\t<body>\r\n\t\t<div class="footerFix">\r\n\t\t\t<nav style="margin-bottom:0px;" id="mobilized_navbar_fix" class="navbar">\r\n\t\t\t<!-- <nav style="border-bottom:none; margin-bottom:0px; background-color: transparent; border-radius: 1px;" id="mobilized_navbar_fix" class="navbar"> -->\r\n\t\t\t\t<div class="container-fluid">\r\n\t\t\t\t\t<!-- Brand and toggle get grouped for better mobile display -->\r\n\t\t\t\t\t<div class="navbar-header">\r\n\t\t\t\t\t\t<button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">\r\n\t\t\t\t\t\t\t<span class="glyphicon glyphicon-menu-hamburger"></span>\r\n\t\t\t\t\t\t\t<span class="sr-only">Toggle navigation</span>\r\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t\t\t<span class="icon-bar"></span>\r\n\t\t\t\t\t\t</button>\r\n\t\t\t\t\t\t<a class="navbar-brand" href="/index">\r\n\t\t\t\t\t\t\t<!--<img style="height:50px; width:200px; margin-top:-15px;" src="http://placehold.it/150x50&text=Logo" alt="Nutrition For Wellness">-->\r\n\t\t\t\t\t\t\t<h1 id="siteName" style="margin-left: 10px; margin-top: -5px; color: orange">Timpview<span style="color:#337AB7">Yearbook</span></h1>\r\n\t\t\t\t\t\t</a>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t\t<!-- Collect the nav links, forms, and other content for toggling -->\r\n\t\t\t\t\t<div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n\t\t\t\t\t\t<ul class="nav navbar-nav navbar-right">\r\n\t            <li><a href="/upload/">Upload</a></li>\r\n\t\t\t\t\t\t\t<li><a href="/student-life/">Student Life</a></li>\r\n\t\t\t\t\t\t\t<li><a href="/clubs/">Clubs</a></li>\r\n\t\t\t\t\t\t\t<li><a href="/staffers/">Staffers</a></li>\r\n\t\t\t\t\t\t\t<li><a href="/sports/">Sports</a></li>\r\n\t\t\t\t\t\t\t<li><a href="/candids/">Candids</a></li>\r\n')
        if user.is_superuser:
            if not user.adminify:
                __M_writer('\t\t\t\t\t\t\t\t\t<li><a href="/index.adminify/')
                __M_writer(str( page_href ))
                __M_writer('">adminify</a></li>\r\n')
            else:
                __M_writer('\t\t\t\t\t\t\t\t\t<li><a href="/index.un_adminify/')
                __M_writer(str( page_href ))
                __M_writer('">un-adminify</a></li>\r\n')
        if request.user.is_authenticated:
            __M_writer('\t\t\t\t\t\t\t\t<li class="dropdown">\r\n\t\t\t\t\t\t\t\t\t<a class="dropdown-toggle" data-toggle="dropdown" href="#">')
            __M_writer(str( request.user.username ))
            __M_writer('<span class="caret"></span></a>\r\n\t\t\t\t\t\t\t\t\t<ul class="dropdown-menu">\r\n\t\t\t\t\t\t\t\t\t\t<li><a href="/logout/">Logout</a></li>\r\n\t\t\t\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t\t\t\t</li>\r\n')
        else:
            __M_writer('\t\t\t\t\t\t\t\t<li><a href="/login/">Login</a></li>\r\n')
        __M_writer('\t\t\t\t\t\t</ul>\r\n\t\t\t\t\t</div><!-- /.navbar-collapse -->\r\n\t\t\t\t</div><!-- /.container-fluid -->\r\n\t\t\t</nav>\r\n\r\n\t\t\t')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        __M_writer('\t\t\t')
        __M_writer(str( django_mako_plus.link_js(self) ))
        __M_writer('\r\n\t\t</div>\r\n\t</body>\r\n</html>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t')
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
        __M_writer('\t\t\t')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "30": 2, "31": 8, "32": 16, "33": 16, "38": 18, "39": 48, "40": 49, "41": 50, "42": 50, "43": 50, "44": 51, "45": 52, "46": 52, "47": 52, "48": 55, "49": 56, "50": 57, "51": 57, "52": 62, "53": 63, "54": 65, "59": 72, "60": 74, "61": 74, "62": 74, "68": 17, "74": 17, "80": 70, "86": 70, "87": 72, "93": 87}}
__M_END_METADATA
"""
