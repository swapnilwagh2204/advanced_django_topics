# Middleware:
# it is frameworks of hooks into djangos request response processing
from django.conf import settings
import django.shortcuts

# its light, low level plugin system globally altering djangos input or output
# each middleware conponent is reponsible for doing some specific functions

# built in middlewares
# custom middlewares

# banda-- -> bhai-- -> baap--- -> bandi
# multiple middlewares hp sakte hai


# function bases middlewares

# A middlewares factory is callable that takes a get_response callable and returns a middleware.
# A middleware is callable that takes a request and returns a response, just like views

# syntax:


# def my_middleware(get_response):
#     # one time configuration and initialization
#     def my_function(request):
#         # code to be executed before the view is called
#         response = get_response(request)
#         # code to be executed after the view is called
#         return response
#     return my_function

# get_response()
# agar last middlewares se gaya hoga too view ho akta hai....ya next middlewares ho sakta hai
# jab tak last nahi aa jata tab tak wo run hota jayega

# middlewares can live anywhere in your python path.

# activate middleware

# to activte middlewares component .add it in list of middlewares in settings
# order maintain karna padta hai
# e.g.-> authenticationMiddleware session middlewares chya nntr thevaych

# middleware=[
#     blog.middleware.my_middleware,  #sample middleware.
# ]


# class bases middlewares


# class Mymiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         # one time configuraion  and initialisation

#     def __call__(self, request):
#         # code to be executed for each request before the view and later middleware called
#         response = self.get_response(request)
#         # code to be executed for each request after the view is called.
#         return response


# __call__ hhar request ke sath chalta hai...lekin __init__ sirf web server jab start hota haii tab chalta hai...

# activating middleware :
# add middleware into django settings

# class.middlewares.Mymiddleware

# flow of middleware running:
#   for those with one time initiaalisation..they will execute in reverse direction than that of we specified in settings.py
#   whenn we hit the the request..it will execute according to our given direction....while when we get he response ....we will get it by reverse order
#   like the initiaalised one.

# if we dont want to send the cursor to the next middleware or we want to get response from the middle middlware itself..then instead of using 
# get_response(request) we can use HttpResponse..and the response in want....dont forget to import HttpResponse first.

# middlewares hooks
# special methods for class based middlewares(not used for function based views)

# process_view(request,view_func,view_args,view_kwargs)--> it is called just before django calls  the view.

# it should either return none or HttpResponse objects

# if it returns none ,django will django will continue to processing this request ,executing any other process_view() middleware and then  the appropriate view.

# if it returns HttpResponse object ,djngo wont bother calling the  appropriate view ,it will apply response middleware to that HttpResponse and return the result.

# process_exception(request,exception)- django calls  process_exception() when a  view raises an exception.

# it should return  either none or an HttpResponse object

# if it returns HttpResponse object ,the template response and  response middleware will be applied and  the resulting response returned to the browser.
# otherwise ,default exception handling kicks in .

# where request = it is an HttpRequest object
# exception = it is an exception object raised  by view function


# Note - middleware are run in reverse order during the response phase, which includes process execution. if an exception  middleware  returns a response, the 
# process_exception methods of the middleware classes  above that middleware wont be called at all.


# process_template_response(request, response)
# this method is called just after the view  has finished  executing,if the response instance has  a render method,indicating that it  is  a templateresponse 
# or equivalent.

# it must return respnseobject  that implements a render method.

# request=it is an HttpResponse object
# response=it is an templateresponse object returned by a django view or  by middleware.


# templateresponse:

# templateresponse--> it  is a subclass of simpletemplatesresponse that knows about the current HttpRequest.
# A templateresponse objct can be used anywhere that a normal django.http.HttpRESPONSE can be used.it is also used as alternative to calling render.

# method:
# __init__(request,template,context=none,)
