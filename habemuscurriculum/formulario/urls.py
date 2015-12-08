from django.conf.urls import url
from formulario import views as fViews

urlpatterns = [
	url(r'^$', fViews.FormaBase.as_view(), name= 'formularioBase'),
]
