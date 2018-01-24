# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1516660308.1350536
_enable_loop = True
_template_filename = 'C:/Users/HerbGlitch/Desktop/School/yearbook/homepage/templates/images.html'
_template_uri = 'images.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = ['content']



import os


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
        imageqry = context.get('imageqry', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
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
        imageqry = context.get('imageqry', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  ')
        __M_writer('\r\n  <div class="section contentpart">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <h2>Upload Content</h2>\r\n          <form action="/images" id="form" method="post" enctype="multipart/form-data">\r\n            ')
        __M_writer(str( csrf_input ))
        __M_writer('\r\n            <input type="file" class="box" name="file_field" multiple required="False" id="id_file_field">\r\n          </form>\r\n        </div>\r\n      </div>\r\n')
        __M_writer('      <div class="row">\r\n        <div class="col-md-12">\r\n          <h2>Complete:</h2>\r\n')
        for image in imageqry:
            __M_writer('            <div class="col-md-4 imageOverlay">\r\n              <img style="height:auto; width:100%;" src="/static/')
            __M_writer(str( image.mainImage ))
            __M_writer('">\r\n            </div>\r\n')
        __M_writer('        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n  <script src="jquery.js"></script>\r\n  <script src="jquery.form.min.js"></script>\r\n  <script>\r\n    document.getElementById("id_file_field").onchange = function() {\r\n      document.getElementById("form").submit();\r\n    };\r\n  </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/HerbGlitch/Desktop/School/yearbook/homepage/templates/images.html", "uri": "images.html", "source_encoding": "utf-8", "line_map": {"17": 4, "32": 0, "41": 1, "46": 38, "52": 3, "60": 3, "61": 6, "62": 13, "63": 13, "64": 19, "65": 22, "66": 23, "67": 24, "68": 24, "69": 27, "75": 69}}
__M_END_METADATA
"""
