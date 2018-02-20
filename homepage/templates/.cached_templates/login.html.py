# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518033144.04997
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/login.html'
_template_uri = 'login.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        csrf_input = context.get('csrf_input', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        csrf_input = context.get('csrf_input', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n  <div style="height: 40px"></div>\r\n  <div class="content">\r\n    <div class="card col-md-6 col-md-push-3" style="padding: 20px;">\r\n      <h3 class="logtext" style="text-align: center;">Enter your username and password below to log in.</h3>\r\n      <form id="loginform" class="loginform" action="/login" method="post">')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n        <div class="form-group">')
        __M_writer(str( form ))
        __M_writer('</div>\r\n          <a href="/homepage/register" class="forgotpass">New? Register Now</a>\r\n          <button type="submit" class="loginbtn" style="float: right;">Login</button>\r\n          <a href="/homepage/forgotpassword" class="forgotpass" style="float:right; padding-right: 15px;">Forgot Password?</a>\r\n        <div class="clearfix"></div>\r\n      </form>\r\n    </div>\r\n  </div>\r\n  <div style="height: 20px"></div>\r\n    \r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/login.html", "uri": "login.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "47": 3, "55": 3, "56": 9, "57": 9, "58": 10, "59": 10, "65": 59}}
__M_END_METADATA
"""
