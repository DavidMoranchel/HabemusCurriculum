from django.conf.urls import url
from home import views as bviews

urlpatterns = [
	url(r'^$', bviews.LandingIndex.as_view(), name= 'index'),
]
