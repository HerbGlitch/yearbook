# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516653722.7437866
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
        def content():
            return render_content(context._locals(__M_locals))
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
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <style>\r\n    \thtml, body {\r\n    \t\tpadding: 0;\r\n    \t\tmargin: 0;\r\n    \t}\r\n    \tdiv{\r\n    \t\tfloat: left;\r\n    \t\tdisplay: inline;\r\n    \t}\r\n    </style>\r\n\t<div id="mainImage">\r\n')
        __M_writer('\t</div>\r\n    <a href="/student-life/"><div class="sameFilter" id="imgTopLeft"></div></a>\r\n    <a href="/clubs/"><div class="sameFilter" id="smallMiddle"></div></a>\r\n    <a href="/sports/"><div class="sameFilter" id="tallRight"></div></a>\r\n    <a href="/staffers/"><div class="sameFilter" id="bottomLeft"></div></a>\r\n    <a href="/candids/"><div class="sameFilter" id="bottomMiddle"></div></a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "35": 1, "45": 3, "51": 3, "52": 20, "58": 52}}
__M_END_METADATA
"""
