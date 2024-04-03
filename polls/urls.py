from django.urls import path

from . import views
from .views import ChoiceCreateView
from .views import QuestionCreateView
from .views import QuestionUpdateView
from .views import ChoiceUpdateView



app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"), #제너릭의 기본이 pk
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('question/new/', QuestionCreateView.as_view(), name='question_new'),
    path('question/<int:pk>/choice/new/', ChoiceCreateView.as_view(), name='choice_new'),
    path('question/<int:pk>/update/', QuestionUpdateView.as_view(), name='question_update'),
    path('question/<int:pk>/choice/update', ChoiceUpdateView.as_view(), name='question_update'),
   


]