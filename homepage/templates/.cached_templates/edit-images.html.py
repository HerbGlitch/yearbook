# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1517512402.4511647
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/edit-images.html'
_template_uri = 'edit-images.html'
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
        imageqry = context.get('imageqry', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n')
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
        imageqry = context.get('imageqry', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if request.user.is_superuser:
            __M_writer('\t  <div class="section contentpart">\r\n\t    <div class="container">\r\n\t      <div class="row">\r\n\t        <div class="col-md-12">\r\n\t        <h1 style="width:100%; margin-top: 40px; text-align: center">Edit Images</h1>\r\n\t        </div>\r\n\t      </div>\r\n\t    </div>\r\n\t  </div>\r\n\t  <div class="section contentpart">\r\n\t    <div class="container">\r\n\t      <div class="row">\r\n')
            for image in imageqry:
                __M_writer('\t          <div class="col-md-4">\r\n\t            <div class="image_styling">\r\n\t              <img src="/static/')
                __M_writer(str( image.mainImage ))
                __M_writer('" width="100%"/>\r\n\t              <button onClick="" id="submit')
                __M_writer(str( image.id ))
                __M_writer('" class="confirm">Submit: <i class="fa fa-check"></i></button>\r\n\t              <button class="trash" id="trash')
                __M_writer(str( image.id ))
                __M_writer('" data-singleton="true" onClick="alertShow(')
                __M_writer(str( image.id ))
                __M_writer(')"><i class="fa fa-trash-o"></i></button>\r\n\t              <div style="display:none;" class="alert alert-danger" id="alert')
                __M_writer(str( image.id ))
                __M_writer('" role="alert">\r\n\t                <strong>Alert:</strong> Are you sure you want to delete this Image?\r\n\t                <button class="trash_small" onClick="window.location = \'/edit-images.delete_Image/')
                __M_writer(str( image.id ))
                __M_writer('\'">Delete</button>\r\n\t                <button class="cancel" onClick="alertHide(')
                __M_writer(str( image.id ))
                __M_writer(')">Cancel</button>\r\n\t              </div>\r\n\t            </div>\r\n\t          </div>\r\n')
            __M_writer('\t      </div>\r\n\t    </div>\r\n\t  </div>\r\n')
            return ''
        finally:
            context.caller_stack._pop_frame()


    """
    __M_BEGIN_METADATA
    {"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/edit-images.html", "uri": "edit-images.html", "source_encoding": "utf-8", "line_map": {"28": 0, "37": 1, "38": 2, "43": 35, "49": 4, "57": 4, "58": 5, "59": 6, "60": 18, "61": 19, "62": 21, "63": 21, "64": 22, "65": 22, "66": 23, "67": 23, "68": 23, "69": 23, "70": 24, "71": 24, "72": 26, "73": 26, "74": 27, "75": 27, "76": 32, "82": 76}}
    __M_END_METADATA
"""
