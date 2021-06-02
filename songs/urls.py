from django.urls import path
from . import views


urlpatterns = [
    path('api/song/', views.SongList.as_view()),
]
