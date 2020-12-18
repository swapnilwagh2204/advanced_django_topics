def Brother_middleware(get_response):
    print("one time initilization for brother")

    def my_function(request):
        print("this is brother before view execution")
        response = get_response(request)
        print("this is brother after view execution")
        return response
    return my_function


def father_middleware(get_response):
    print("one time initilization for father")

    def my_function(request):
        print("this is father before view execution")
        response = get_response(request)
        print("this is father after view execution")
        return response
    return my_function


def mother_middleware(get_response):
    print("one time initilization for mother")

    def my_function(request):
        print("this is mother before view execution")
        response = get_response(request)
        print("this is mother after view execution")
        return response
    return my_function


# class myMiddConfig:
#     def __init__(self, get_response):
#         self.get_response = get_response
#         print('onw time execution in class based views')

#     def __call__(self, request):
#         print("this is before view execution in class")
#         response = self.get_response(request)
#         print("this is after view execution in class")
#         return response
