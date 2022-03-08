from operator import index
from django.urls import path
from . import views


# Base URL에서 경로를 따라 왔다
# URL 주소에 따라 알맞은 views.p로 라우팅 시켜 준다.
# 첫 번째 ''는 Base URL 에 있는 ..../polls/ 를 의미 한다.
app_name ='polls'
urlpatterns = [
    path('', views.index, name='index'),
    #ex) /polls/5
    # the 'name' value as called by the {% url %} template tag
    path('<int:question_id>/', views.detail, name = 'detail'),
    #ex) /polls/results
    path('<int:question_id>/results/', views.results, name='results'),
    #ex) /polls/5/vote
    path('<int:question_id>/vote/', views.vote, name='vote'),
    ## 만약 상세 뷰의 URL을 polls/specifics/12/로 바꾸고 싶다면, 템플릿에서 바꾸는 것이 아니라 polls/urls.py에서 바꿔야 합니다.
    # ...
    # # added the word 'specifics'
    # path('specifics/<int:question_id>/', views.detail, name='detail'),
    # ...
]
