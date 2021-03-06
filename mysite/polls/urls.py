
from django.conf.urls import url

from . import views

app_name = 'polls'
# urlpatterns = [
#     # ex: /polls/
#     url(r'^$', views.index, name='index'),
#
#     # ex: /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#     # # added the word 'specifics'
#     # url(r'^specifics/(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
#
#     # ex: /polls/5/results/
#     url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
#
#     # ex: /polls/5/vote/
#     url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
# ]

# Amend URLconf
#
# First, open the polls/urls.py URLconf and change it like so:
# Note that the name of the matched pattern in the regexes of the second and third patterns has changed from <question_id> to <pk>.
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
