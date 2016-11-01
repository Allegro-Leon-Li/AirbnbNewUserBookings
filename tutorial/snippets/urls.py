from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
<<<<<<< HEAD

    url(r'^snippets/$', views.snippet_list),
=======
	url(r'^$',views.index, name="index"),
    url(r'^snippets/$', views.snippet_list,name='snippets-instance'),
>>>>>>> 576538a653ce86e782ad300648d0bfbb4b5f255e
    url(r'^snippets/(?P<pk>[0-9]+)$', views.snippet_detail),
    url(r'^users/$', views.user_list,name='user-instance'),
    url(r'^users/(?P<pk>[0-9]+)$', views.user_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)