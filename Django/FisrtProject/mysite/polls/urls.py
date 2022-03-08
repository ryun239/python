from operator import index
from django.urls import path
from . import views


# Base URL에서 경로를 따라 왔다
# URL 주소에 따라 알맞은 views.p로 라우팅 시켜 준다.
# 첫 번째 ''는 Base URL 에 있는 ..../polls/ 를 의미 한다.
urlpatterns = [
    path('', views.index, name='index'),
    #ex) /polls/5
    path('<int:question_id>/', views.detail, name = 'detail'),
    #ex) /polls/results
    path('<int:question_id>/results/', views.results, name='results'),
    #ex) /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
