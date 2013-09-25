from django.views import generic
from barreviews.models import *

class BarsView(generic.ListView):
    template_name = 'barreviews/index.html'
    context_object_name = 'bars'
    
    def get_queryset(self):
        return (x for x in range(0,1)) #Bar.objects.all()
