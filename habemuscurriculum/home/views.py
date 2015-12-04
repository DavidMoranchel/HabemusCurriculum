from django.views import generic 
from home import models as bmodels 

# Create your views here.

class BlogIndex(generic.ListView):
	queryset = bmodels.Entry.objects.filter(publish=True)#de entry trae todos los objetos con ese filtro
	template_name = 'home/index.html'

	
class PostDetail(generic.DetailView):
	model = bmodels.Entry
	template_name = 'blog/post.html'