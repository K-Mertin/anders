from django.conf.urls import url
from inventory import views
from rest_framework.urlpatterns import format_suffix_patterns

# #function base
# urlpatterns = [
#     url(r'^', views.snippet_list),
#     url(r'^(?P<pk>[0-9]+)/$', views.snippet_detail),
# ]

#class base
urlpatterns = [
    url(r'^product/(?P<pk>.*?)$', views.ProductView.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.ProductDetail.as_view()),
   # url(r'^',views.hello_world)
]

urlpatterns = format_suffix_patterns(urlpatterns)