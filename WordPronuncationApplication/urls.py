__author__ = 'carlcustav'
from django.conf.urls import url
from . import views
from WordPronuncationApplication.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index')
]

