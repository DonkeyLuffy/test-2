from django.urls import path
from watchmate.watchlist_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformListAV

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    path('stream/', StreamPlatformListAV.as_view(), name='stream-platform-list'),
]