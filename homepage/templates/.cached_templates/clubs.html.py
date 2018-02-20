# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1518729197.8372693
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/clubs.html'
_template_uri = 'clubs.html'
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
        if not request.user.adminify:
            __M_writer('\t\t<div class="section contentpart">\r\n\t\t\t<div class="container">\r\n\t\t\t\t<div class="row">\r\n\t\t\t\t\t<div class="col-md-12">\r\n\t\t\t\t\t\t<h1 style="width:100%; margin-top: 40px; text-align: center">Clubs</h1>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        else:
            __M_writer('\t\t<div class="section contentpart">\r\n\t\t\t<div class="container">\r\n\t\t\t\t<div class="row">\r\n\t\t\t\t\t<div class="col-md-12">\r\n\t\t\t\t\t\t<h1 style="width:100%; margin-top: 40px; text-align: center">Clubs Admin</h1>\r\n\t\t\t\t\t</div>\r\n\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/clubs.html", "uri": "clubs.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "41": 25, "47": 3, "54": 3, "55": 4, "56": 5, "57": 14, "58": 15, "64": 58}}
__M_END_METADATA
"""
