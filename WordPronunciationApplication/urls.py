__author__ = 'carlcustav'
from django.conf.urls import url
from WordPronunciationApplication.views import IndexView, WordView, FileUpload
import WordPronunciationApplication as app

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^words/(?P<searchword>.*)/$', WordView.as_view(), name='searchword'),
    url(r'^upload/$', FileUpload.as_view()),
    url(r'^sound/', app.views.get_sound),
]

