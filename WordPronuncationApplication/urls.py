__author__ = 'carlcustav'
from django.conf.urls import url
from . import views
from WordPronuncationApplication.views import IndexView, WordView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^words/', WordView.as_view(), name='searchWord')

]

