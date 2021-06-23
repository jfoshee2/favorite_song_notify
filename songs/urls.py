from django.urls import path
from . import views


urlpatterns = [
    # song urls
    path('api/song/', views.SongList.as_view({'get': 'list', 'post': 'create'})),
    path('api/song/<int:pk>', views.SongList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # artist urls
    path('api/artist', views.ArtistList.as_view({'get': 'list', 'post': 'create'})),
    path('api/artist/<int:pk>', views.ArtistList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # station urls
    path('api/station', views.StationList.as_view({'get': 'list', 'post': 'create'})),
    path('api/station/<int:pk>', views.StationList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # daily schedule urls
    path('api/daily-schedule', views.DailyScheduleList.as_view({'get': 'list', 'post': 'create'})),
    path('api/daily-schedule/<int:pk>', views.DailyScheduleList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),

    # daily schedule song urls
    path('api/daily-schedule-song', views.DailyScheduleSongList.as_view({'get': 'list', 'post': 'create'})),
    path('api/daily-schedule-song/<int:pk>', views.DailyScheduleSongList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('api/daily-schedule-song/station/<station_id>', views.DailyScheduleSongList.as_view({'get': 'schedule'}))
]
