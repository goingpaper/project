from django.views import generic
#from barreviews.models import *

class IndexView(generic.ListView):
    template_name = 'barreviews/index.html'
    context_object_name = 'index'
    
    def get_queryset(self):
        return (x for x in range(0,1))

class BarsView(generic.ListView):
    template_name = 'barreviews/bars.html'
    context_object_name = 'bars'
    
    def get_queryset(self):
        return (x for x in range(0,1)) #Bar.objects.all()

class UsersView(generic.ListView):
    template_name = 'barreviews/users.html'
    context_object_name = 'users'
    
    def get_queryset(self):
        return (x for x in range(0,1)) #User.objects.all()

class DrinksView(generic.ListView):
    template_name = 'barreviews/drinks.html'
    context_object_name = 'drinks'
    
    def get_queryset(self):
        return (x for x in range(0,1)) #Drink.objects.all()

class ReviewsView(generic.ListView):
    template_name = 'barreviews/reviews.html'
    context_object_name = 'reviews'
    
    def get_queryset(self):
        return (x for x in range(0,1)) #Review.objects.all()