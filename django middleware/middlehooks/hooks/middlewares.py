
from django.http import response
from django.shortcuts import HttpResponse


class Myprocessmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # koi aur middewae hai to wo lega...aur execute ka mauka milega
        response = self.get_response(request)
        return response

    def process_view(request, *args, **kwargs):
        # agar ye none return karega to django view ko call kar dega,,django isko jut before view call karta hai
        print("this is process view ---> before view")
        # return HttpResponse("this is before view execution")
        return None  # yaha pe view print hoga


class Myexceptionmiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # koi aur middewae hai to wo lega...aur execute ka mauka milega
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        print('exception occurs')
        print(exception.__class__.__name__)
        msg = exception
        return HttpResponse(msg)


class Mytemplatemiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # koi aur middewae hai to wo lega...aur execute ka mauka milega
        response = self.get_response(request)
        return response

    def process_template_response(self, request, response):
        print('process templateresponse from middlware')
        response.context_data['name'] = "wagh"
        return response
