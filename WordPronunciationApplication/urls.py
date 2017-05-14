__author__ = 'carlcustav'
from django.conf.urls import url
from WordPronunciationApplication.views import IndexView, WordView

urlpatterns = [
    url(r'^', IndexView.as_view(), name='index'),
    url(r'^words/(?P<searchword>.*)/$', WordView.as_view(), name='searchWord')
    #url(r'^words/', WordView.as_view(), name='searchWord')
]

