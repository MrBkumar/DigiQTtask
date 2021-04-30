from django.urls import path
from .views import MovieList, MovieDetail, MovieCreate, MovieUpdate, MovieDelete, CustomLoginView, RegisterView, LoadData
from django.contrib.auth.views import LogoutView
from core.api.views import MovieDetailsView, MovieSortingView, MovieSearchView

urlpatterns = [
    # basic url route
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),

    # movie data related url route
    path('', MovieList.as_view(), name='movies'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie-detail'),
    path('create-Movie/', MovieCreate.as_view(), name='movie-create'),
    path('movie-update/<int:pk>', MovieUpdate.as_view(), name='movie-update'),
    path('movie-delete/<int:pk>', MovieDelete.as_view(), name='movie-delete'),
  
    # movie data related api url route
    path('api/movie/detail/<int:pk>', MovieDetailsView.as_view(), name='api-movie-detail'),
    path('api/movie/sort/<str:sort_by>', MovieSortingView.as_view(), name='api-movie-sort'),
    path('api/movie/search/<str:search_by>', MovieSearchView.as_view(), name='api-movie-search'),
    
    #only one time usage
    path('load-data/', LoadData.as_view(), name='load-data'),
]