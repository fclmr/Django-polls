from django.urls import path

from . import views_bk

app_name = 'polls'
urlpatterns = [
    path('', views_bk.IndexView.as_view(), name='index'),
    path('index/', views_bk.index_1, name='index_1'),
    path('specifics/<int:question_id>/', views_bk.detail, name='detail'),
    path('<int:question_id>/results/', views_bk.results, name='results'),
    path('<int:question_id>/vote/', views_bk.vote, name='vote'),
]