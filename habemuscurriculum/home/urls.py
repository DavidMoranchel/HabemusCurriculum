from django.conf.urls import url
from home import views as bviews

urlpatterns = [
	url(r'^$', bviews.BlogIndex.as_view(), name= 'index'),
]
