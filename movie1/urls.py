
from django.conf.urls import url
from . import views
app_name='movie1'
urlpatterns = [
    url(r'^$',views.index,name='index'),

    url(r'^(?P<movie_id>[0-9]+)/$',views.detail,name='detail'),

    url(r'^(?P<movie_id>[0-9]+)/favorite$',views.favorite,name='favorite'),

]

