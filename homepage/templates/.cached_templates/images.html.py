# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1510174030.4148867
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/images.html'
_template_uri = 'images.html'
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
    return runtime._inherit_from(context, 'navbar.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        imageqry = context.get('imageqry', UNDEFINED)
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
        imageqry = context.get('imageqry', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="section contentpart">\r\n\t\t<div class="container">\r\n')
        __M_writer('\t\t\t<div class="row">\r\n\t\t\t\t<div class="col-md-12">\r\n')
        for image in imageqry:
            __M_writer('\t\t\t\t\t\t<div class="col-md-4 imageOverlay">\r\n\t\t\t\t\t\t\t<img style="height:auto; width:100%;" src="/static/')
            __M_writer(str( image.mainImage ))
            __M_writer('">\r\n\t\t\t\t\t\t</div>\r\n')
        __M_writer('\t\t\t\t</div>\r\n\t\t\t</div>\r\n\t\t</div>\r\n\t</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/images.html", "uri": "images.html", "source_encoding": "utf-8", "line_map": {"28": 0, "36": 1, "46": 3, "53": 3, "54": 7, "55": 9, "56": 10, "57": 11, "58": 11, "59": 14, "65": 59}}
__M_END_METADATA
"""