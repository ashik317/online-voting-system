from django.urls import path
from polls.views import IndexView, DetailView, vote, ResultsView

app_name = 'polls'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('vote/<int:question_id>/', vote, name='vote'),
    path('results/<int:pk>/', ResultsView.as_view(), name='results'),
]