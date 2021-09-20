# models:

# save() method in django-- -> saves the data into model.
# clean() - -> adds the validations in the model.


# one should not use models for writing the business logic.
# models should only deal with data models and relations.


# views and apis:


# class snippetviewset(viewsets.ModelViewSet):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer


# this is the viewset for the snippet model.
# it can perform all crud operations in the model with the 3 lines only.

# so what happends behind the three lines:
# createmodelmixin().create() is called.
# snippetserializer validations is triggered.
# snippetserializer.create is called.
# if we want to add additional business logic, we should put it into serializer class.


# serializers:

# it transforms the python/orm objects data into json.
# transforms json to python/orm objects.


# A note on abstraction:
# if you want to abstract the code, you should use the serializers.
# if you are putting something in your database, use little abstraction as possible.
# if you are getting something from the database, use as much  abstraction as possible.but dont overdo it.

# so where we should put the heavy business logic:

# app/sevices.py - - -> module

# a general unit that holds the business logic all together
# service--> a simple, type annoted function
# speaks the domain language of the software that we are  creating.
# can handle permission and multiple cross-cutting concerns, such as callling other services and tasks.
# works mostly and mainly with models.

# the core of the logic is all services exist one single codebase and there should not be anything assocarated with the models and orms in apis and models.py
