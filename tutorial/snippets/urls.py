from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from .views import UserList, UserDetail, LocationDetail

urlpatterns = [

    url(r'^test$', views.test, name="test"),
    # url(r'^sign$', 'django.contrib.auth.views.login', name="signin"),
    url(r'^usersloc/(?P<account_in>\w+)$', views.userinfo),
    url(r'^$', views.index, name="index"),
    url(r'^login$', views.login, name="login"),
    # url(r'^users/$', views.user_list, name='user-instance'),
    # url(r'^users/(?P<pk>[0-9]+)$', views.user_detail),
    # url(r'^users/loc/(?P<pk>[0-9]+)$', views.loc_detail),
    url(r'^users/$', UserList.as_view(), name='user-instance'),
    # url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^users/(?P<account>\w+)$', UserDetail.as_view()),
    url(r'^users/loc/(?P<account>\w+)$', LocationDetail.as_view())



]

urlpatterns = format_suffix_patterns(urlpatterns)
