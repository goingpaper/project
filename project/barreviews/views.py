from django.views import generic
from barreviews.models import *

class IndexView(generic.ListView):
    template_name = 'barreviews/index.html'
    context_object_name = 'index'

class BarsView(generic.ListView):
    template_name = 'barreviews/bars.html'
    context_object_name = 'bars'
    
    def get_queryset(self):
        return Bar.objects.all()
