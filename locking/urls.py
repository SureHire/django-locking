from django.conf.urls import url
from django.views.i18n import JavaScriptCatalog

# We need at least one url inside urlpatterns to keep include('locking.urls')
# from throwing an exception
urlpatterns = [
    url(r'jsi18n/$', JavaScriptCatalog.as_view(), {'packages': 'locking'}),
]
