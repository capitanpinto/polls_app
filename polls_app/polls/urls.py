from django.urls import path, re_path, include

from .controllers import questions
from .controllers import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
    path('new/', questions.new, name="new"),
    path('create/', questions.create_question, name="create"),
]