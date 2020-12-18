# Middleware:
# it is frameworks of hooks into djangos request response processing
from django.conf import settings

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
