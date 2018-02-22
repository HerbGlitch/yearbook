# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519334094.9169157
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/register.html'
_template_uri = 'register.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        csrf_input = context.get('csrf_input', UNDEFINED)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <div style="height: 40px"></div>\r\n  <div class="content">\r\n    <div class="col-md-6 col-md-push-3" style="padding: 20px;">\r\n      <h3 style="text-align: center;">Enter your username and password below to log in.</h3>\r\n      <form id="loginform" class="loginform" action="/register" method="post">')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n        <div class="form-group">')
        __M_writer(str( form ))
        __M_writer('</div>\r\n          <a href="/login" class="login">Already a User?</a>\r\n          <button type="submit" class="loginbtn" style="float: right;">Register</button>\r\n      </form>\r\n    </div>\r\n  </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/register.html", "uri": "register.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "42": 15, "48": 3, "56": 3, "57": 8, "58": 8, "59": 9, "60": 9, "66": 60}}
__M_END_METADATA
"""
