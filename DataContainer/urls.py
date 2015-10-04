from django.conf.urls import include, url

urlpatterns = [
    url(r'^container/(?P<slug>[\w\-]+)/', 'DataContainer.views.get_data',name='data_container'),
    url(r'^container/add/', 'DataContainer.views.add_data',name='add_container'),
]