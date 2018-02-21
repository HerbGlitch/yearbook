# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519242037.4152846
_enable_loop = True
_template_filename = 'C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/upload.html'
_template_uri = 'upload.html'
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
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        imageqry = context.get('imageqry', UNDEFINED)
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
        csrf_input = context.get('csrf_input', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context)
        imageqry = context.get('imageqry', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if not request.user.adminify:
            __M_writer('    <div class="section contentpart">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-12">\r\n          <h1 style="width:100%; margin-top: 40px; text-align: center">Your Images</h1>\r\n            <form action="/upload" id="form" method="post" enctype="multipart/form-data">\r\n              ')
            __M_writer(str( csrf_input ))
            __M_writer('\r\n              <label for="id_file_field" class="custom-file-upload">\r\n                <i class="fas fa-cloud-upload-alt"></i> Upload\r\n              </label>\r\n              <input type="file" class="box" name="file_field" multiple required="False" id="id_file_field">\r\n            </form>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="section contentpart">\r\n      <div class="container">\r\n        <div class="row">\r\n')
            for image in imageqry:
                __M_writer('            <div class="col-md-4">\r\n              <div class="image_styling">\r\n                <img src="/static/')
                __M_writer(str( image.mainImage ))
                __M_writer('" width="100%"/>\r\n')
                if image.submitted:
                    __M_writer('                  <button onClick="window.location = \'/upload.unsubmit/')
                    __M_writer(str( image.id ))
                    __M_writer('\'" id="submit')
                    __M_writer(str( image.id ))
                    __M_writer('" class="confirm">\r\n                    <i class="fas fa-times tooltips" href="#"><span class="marvel">Unsubmit</span></i>\r\n                  </button>\r\n')
                else:
                    __M_writer('                  <button onClick="window.location = \'/upload.submit/')
                    __M_writer(str( image.id ))
                    __M_writer('\'" id="submit')
                    __M_writer(str( image.id ))
                    __M_writer('" class="confirm">\r\n                    <i class="fas fa-check tooltips" href="#"><span class="marvel">Submit</span></i>\r\n                  </button>\r\n')
                __M_writer('                <button class="trash" id="trash')
                __M_writer(str( image.id ))
                __M_writer('" data-singleton="true" onClick="alertShow(')
                __M_writer(str( image.id ))
                __M_writer(')">\r\n                  <i class="far fa-trash-alt tooltips" href="#"><span class="marvel">Delete</span></i>\r\n                </button>\r\n                <div style="display:none;" class="alert alert-danger" id="alert')
                __M_writer(str( image.id ))
                __M_writer('" role="alert">\r\n                  <strong>Alert:</strong> Are you sure you want to delete this Image?\r\n                  <button class="trash_small" onClick="window.location = \'/upload.delete_Image/')
                __M_writer(str( image.id ))
                __M_writer('\'">Delete</button>\r\n                  <button class="cancel" onClick="alertHide(')
                __M_writer(str( image.id ))
                __M_writer(')">Cancel</button>\r\n                </div>\r\n              </div>\r\n            </div>\r\n')
            __M_writer('        </div>\r\n      </div>\r\n    </div>\r\n    <script src="jquery.js"></script>\r\n    <script src="jquery.form.min.js"></script>\r\n    <script>\r\n      document.getElementById("id_file_field").onchange = function() {\r\n        document.getElementById("form").submit();\r\n      };\r\n\r\n      function alertShow(id){\r\n        var displayAlert = document.getElementById("alert" + id);\r\n        displayAlert.style="display: block;";\r\n\r\n        var trashHidden = document.getElementById("trash" + id);\r\n        trashHidden.style= "display: none;";\r\n        var submitHidden = document.getElementById("submit" + id);\r\n        submitHidden.style = "display: none;";\r\n      }\r\n\r\n      function alertHide(id){\r\n        var hideAlert = document.getElementById("alert" + id);\r\n        hideAlert.style="display: none;";\r\n\r\n        var trashShow = document.getElementById("trash" + id);\r\n        trashShow.style= "display: inital;";\r\n        var submitShow = document.getElementById("submit" + id);\r\n        submitShow.style = "display: inital;";\r\n      }\r\n\r\n      function deleteImage(){\r\n      }\r\n    </script>\r\n')
        elif request.user.adminify:
            __M_writer('    <div class="section contentpart">\r\n      <div class="container">\r\n        <div class="row">\r\n          <div class="col-md-12">\r\n            <h1 style="width:100%; margin-top: 40px; text-align: center">Image Admin</h1>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n    <div class="section contentpart">\r\n      <div class="container">\r\n        <div class="row">\r\n')
            for image in imageqry:
                __M_writer('            <div class="col-md-4">\r\n              <div class="image_styling">\r\n                <img src="/static/')
                __M_writer(str( image.mainImage ))
                __M_writer('" width="100%"/>\r\n                <button onClick="window.location = \'/upload.approved/')
                __M_writer(str( image.id ))
                __M_writer('\'" id="submit')
                __M_writer(str( image.id ))
                __M_writer('" class="submit">\r\n                  <i class="fa fa-check"></i>\r\n                </button>\r\n                <button class="trash" id="trash')
                __M_writer(str( image.id ))
                __M_writer('" data-singleton="true" onClick="alertShow(')
                __M_writer(str( image.id ))
                __M_writer(')"><i class="fas fa-exclamation-triangle"></i></button>\r\n                <div style="display:none;" class="alert alert-warning" id="alert')
                __M_writer(str( image.id ))
                __M_writer('" role="alert">\r\n                  <strong>Alert:</strong> Are you sure you want to report this Image?\r\n                  <button class="trash_small" onClick="window.location = \'/upload.delete_Image/')
                __M_writer(str(image.id ))
                __M_writer('\'">Report</button>\r\n                  <button class="cancel" onClick="alertHide(')
                __M_writer(str( image.id ))
                __M_writer(')">Cancel</button>\r\n                </div>\r\n              </div>\r\n            </div>\r\n')
            __M_writer('        </div>\r\n      </div>\r\n    </div>\r\n    <script src="jquery.js"></script>\r\n    <script src="jquery.form.min.js"></script>\r\n    <script>\r\n      document.getElementById("id_file_field").onchange = function() {\r\n        document.getElementById("form").submit();\r\n      };\r\n\r\n      function alertShow(id){\r\n        var displayAlert = document.getElementById("alert" + id);\r\n        displayAlert.style="display: block;";\r\n\r\n        var trashHidden = document.getElementById("trash" + id);\r\n        trashHidden.style= "display: none;";\r\n        var submitHidden = document.getElementById("submit" + id);\r\n        submitHidden.style = "display: none;";\r\n      }\r\n\r\n      function alertHide(id){\r\n        var hideAlert = document.getElementById("alert" + id);\r\n        hideAlert.style="display: none;";\r\n\r\n        var trashShow = document.getElementById("trash" + id);\r\n        trashShow.style= "display: inital;";\r\n        var submitShow = document.getElementById("submit" + id);\r\n        submitShow.style = "display: inital;";\r\n      }\r\n\r\n      function deleteImage(){\r\n      }\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/upload.html", "uri": "upload.html", "source_encoding": "utf-8", "line_map": {"28": 0, "38": 1, "43": 144, "49": 3, "58": 3, "59": 4, "60": 5, "61": 11, "62": 11, "63": 24, "64": 25, "65": 27, "66": 27, "67": 28, "68": 29, "69": 29, "70": 29, "71": 29, "72": 29, "73": 32, "74": 33, "75": 33, "76": 33, "77": 33, "78": 33, "79": 37, "80": 37, "81": 37, "82": 37, "83": 37, "84": 40, "85": 40, "86": 42, "87": 42, "88": 43, "89": 43, "90": 48, "91": 81, "92": 82, "93": 94, "94": 95, "95": 97, "96": 97, "97": 98, "98": 98, "99": 98, "100": 98, "101": 101, "102": 101, "103": 101, "104": 101, "105": 102, "106": 102, "107": 104, "108": 104, "109": 105, "110": 105, "111": 110, "117": 111}}
__M_END_METADATA
"""
