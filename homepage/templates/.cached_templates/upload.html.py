# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1519333668.8223104
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
        imageqry = context.get('imageqry', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form_drop_down = context.get('form_drop_down', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        imageqry = context.get('imageqry', UNDEFINED)
        def content():
            return render_content(context)
        form_drop_down = context.get('form_drop_down', UNDEFINED)
        csrf_input = context.get('csrf_input', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
                __M_writer('" id="possible_inapropriate')
                __M_writer(str(image.id))
                __M_writer('" width="100%"/>\r\n                <button onClick="window.location = \'/upload.approved/')
                __M_writer(str( image.id ))
                __M_writer('\'" id="submit')
                __M_writer(str( image.id ))
                __M_writer('" class="confirm">\r\n                  <i class="fa fa-check"></i>\r\n                </button>\r\n                <button class="trash" id="trash')
                __M_writer(str( image.id ))
                __M_writer('" data-singleton="true" onClick="alertShow(')
                __M_writer(str( image.id ))
                __M_writer(')"><i class="fas fa-exclamation-triangle"></i></button>\r\n                <div style="display:none;" class="alert alert-warning" id="alert')
                __M_writer(str( image.id ))
                __M_writer('" role="alert">\r\n                  <strong>Please select the reason for reporting this image</strong> Are you sure you want to report this Image?\r\n                  <form action="" id="form_drop_down" method="post" enctype="multipart/form-data">\r\n        \t\t\t\t\t\t')
                __M_writer(str( csrf_input ))
                __M_writer('\r\n        \t\t\t\t\t\t')
                __M_writer(str( form_drop_down ))
                __M_writer('\r\n                    <button class="trash_small" onClick="window.location = \'/upload.delete_Image/')
                __M_writer(str(image.id ))
                __M_writer('\'">Report</button>\r\n                  </form>\r\n\r\n                  <button class="cancel" onClick="alertHide(')
                __M_writer(str( image.id ))
                __M_writer(')">Cancel</button>\r\n                </div>\r\n              </div>\r\n            </div>\r\n')
            __M_writer('        </div>\r\n      </div>\r\n    </div>\r\n    <script src="jquery.js"></script>\r\n    <script src="jquery.form.min.js"></script>\r\n    <script>\r\n      document.getElementById("id_file_field").onchange = function() {\r\n        document.getElementById("form").submit();\r\n      };\r\n\r\n      function alertShow(id){\r\n        var displayAlert = document.getElementById("alert" + id);\r\n        displayAlert.style="display: block;";\r\n\r\n        var possible_inapropriateHidden = document.getElementById("possible_inapropriate" + id);\r\n        possible_inapropriateHidden.style = "display: none;";\r\n        var trashHidden = document.getElementById("trash" + id);\r\n        trashHidden.style= "display: none;";\r\n        var submitHidden = document.getElementById("submit" + id);\r\n        submitHidden.style = "display: none;";\r\n      }\r\n\r\n      function alertHide(id){\r\n        var hideAlert = document.getElementById("alert" + id);\r\n        hideAlert.style="display: none;";\r\n\r\n        var possible_inapropriateHidden = document.getElementById("possible_inapropriate" + id);\r\n        possible_inapropriateHidden.style = "display: initial;";\r\n        var trashShow = document.getElementById("trash" + id);\r\n        trashShow.style= "display: inital;";\r\n        var submitShow = document.getElementById("submit" + id);\r\n        submitShow.style = "display: inital;";\r\n      }\r\n\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/yearbook/Desktop/yearbook/yearbook/homepage/templates/upload.html", "uri": "upload.html", "source_encoding": "utf-8", "line_map": {"28": 0, "39": 1, "44": 151, "50": 3, "60": 3, "61": 4, "62": 5, "63": 11, "64": 11, "65": 24, "66": 25, "67": 27, "68": 27, "69": 28, "70": 29, "71": 29, "72": 29, "73": 29, "74": 29, "75": 32, "76": 33, "77": 33, "78": 33, "79": 33, "80": 33, "81": 37, "82": 37, "83": 37, "84": 37, "85": 37, "86": 40, "87": 40, "88": 42, "89": 42, "90": 43, "91": 43, "92": 48, "93": 81, "94": 82, "95": 94, "96": 95, "97": 97, "98": 97, "99": 97, "100": 97, "101": 98, "102": 98, "103": 98, "104": 98, "105": 101, "106": 101, "107": 101, "108": 101, "109": 102, "110": 102, "111": 105, "112": 105, "113": 106, "114": 106, "115": 107, "116": 107, "117": 110, "118": 110, "119": 115, "125": 119}}
__M_END_METADATA
"""
