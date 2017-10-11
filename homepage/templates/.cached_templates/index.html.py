# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1507749245.2545717
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
        csrf_input = context.get('csrf_input', UNDEFINED)
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
        csrf_input = context.get('csrf_input', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n    <style>\r\n    \thtml, body {\r\n    \t\tpadding: 0;\r\n    \t\tmargin: 0;\r\n    \t}\r\n    \tdiv{\r\n    \t\tfloat: left;\r\n    \t\tdisplay: inline;\r\n    \t}\r\n    </style>\r\n\t<div id="mainImage">\r\n\t\t<div id="MILocation">\r\n            <form action="" id="form" method="post" enctype="multipart/form-data">\r\n                ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n                <h1 style="margin-top: 1em;" id="mainText">Upload a photo</h1>\r\n                <p style="margin-top: 2em; color: #fff;">Drag a photo on the box or click the box for a file explorer upload window</p>\r\n                <input type="file" class="box" name="file_field" multiple required="False" id="id_file_field" style="margin-top: -17em;">\r\n            </form>\r\n\t\t</div>\r\n\t</div>\r\n    <div class="sameFilter" id="imgTopLeft"></div>\r\n    <div class="sameFilter" id="smallMiddle"></div>\r\n    <div class="sameFilter" id="tallRight"></div>\r\n    <div class="sameFilter" id="bottomLeft"></div>\r\n    <div class="sameFilter" id="bottomMiddle"></div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "46": 3, "53": 3, "54": 17, "55": 17, "61": 55}}
__M_END_METADATA
"""
