# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519333408.9683278
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/index.html'
_template_uri = 'index.html'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if not request.user.is_anonymous and request.user.adminify:
            __M_writer('\t\t<a href="/upload/"><div class="sameFilter" id="mainImage"></div>\r\n\t\t<a href="/student-life/"><div class="sameFilter" id="imgTopLeft"></div></a>\r\n\t\t<a href="/clubs/"><div class="sameFilter" id="smallMiddle"></div></a>\r\n\t\t<a href="/sports/"><div class="sameFilter" id="tallRight"></div></a>\r\n\t\t<a href="/staffers/"><div class="sameFilter" id="bottomLeft"></div></a>\r\n\t\t<a href="/candids/"><div class="sameFilter" id="bottomMiddle"></div></a>\r\n')
        else:
            __M_writer('\t\t<a href="/upload/"><div class="sameFilter" id="mainImage"></div>\r\n\t\t<a href="/student-life/"><div class="sameFilter" id="imgTopLeft"></div></a>\r\n\t\t<a href="/clubs/"><div class="sameFilter" id="smallMiddle"></div></a>\r\n\t\t<a href="/sports/"><div class="sameFilter" id="tallRight"></div></a>\r\n\t\t<a href="/staffers/"><div class="sameFilter" id="bottomLeft"></div></a>\r\n\t\t<a href="/candids/"><div class="sameFilter" id="bottomMiddle"></div></a>\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 20, "47": 3, "54": 3, "55": 4, "56": 5, "57": 11, "58": 12, "59": 19, "65": 59}}
__M_END_METADATA
"""
