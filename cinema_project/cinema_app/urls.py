from django.urls import path
from .views import MovieList, MovieDetail, MovieCategory, MovieLanguage, MovieSearch, MovieYear, MovieStatus, contact, terms
from cinema_app import views


app_name = 'cinema_app'

urlpatterns = [
    path('', MovieList.as_view(), name='movie_list'),
    path('<slug:slug>', MovieDetail.as_view(), name='movie_detail'),
    path('year/<int:year>', MovieYear.as_view(), name='movie_year'),
    path('category/<str:category>', MovieCategory.as_view(), name='movie_category'),
    path('status/<str:status>', MovieStatus.as_view(), name='movie_status'),
    path('language/<str:lang>', MovieLanguage.as_view(), name='movie_language'),
    path('search/', MovieSearch.as_view(), name='movie_search'),
    path('contact-page/', views.contact, name='contact'),
    path('terms-page/', views.terms, name='terms'),





    

]