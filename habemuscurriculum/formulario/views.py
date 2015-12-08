from django.views import generic 
from formulario import models as fmodels 

# Create your views here.

class FormaBase(generic.View):
	template_name = 'formulario/index.html'