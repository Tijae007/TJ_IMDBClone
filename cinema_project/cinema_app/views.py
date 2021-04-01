from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic import YearArchiveView
from django.views.generic.edit import FormView

from .models import Movie, MovieLinks

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

class MovieList(ListView):
    model = Movie
    
    def get_context_data(self, **kwargs):
        context = super(MovieList, self).get_context_data(**kwargs)
        context['top_rated'] = Movie.objects.filter(status='TR')
        context['most_watched'] = Movie.objects.filter(status='MW')
        context['recently_added'] = Movie.objects.filter(status='RA')

        return context

class MovieDetail(DetailView):
    model = Movie

    def get_object(self):
        object = super(MovieDetail, self).get_object()
        object.views_count += 1
        object.save()
        return object

    def get_context_data(self, **kwargs):
        context = super(MovieDetail, self).get_context_data(**kwargs)
        context['links'] = MovieLinks.objects.filter(movie=self.get_object())
        context['related_movies'] = Movie.objects.filter(category=self.get_object().category)
        return context


class MovieCategory(ListView):
    model = Movie
    paginate_by = 2
    template_name = 'cinema_app/mostcategory.html'
    
    def get_queryset(self):
        self.category = self.kwargs['category']
        return Movie.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(MovieCategory, self).get_context_data(**kwargs)
        context['movie_category'] = self.category
        return context


class MovieLanguage(ListView):
    model = Movie
    paginate_by = 4
    template_name = 'cinema_app/movielanguage.html'

    def get_queryset(self):
        self.language = self.kwargs['lang']
        return Movie.objects.filter(language=self.language)

    def get_context_data(self, **kwargs):
        context = super(MovieLanguage, self).get_context_data(**kwargs)
        context['movie_language'] = self.language
        return context


class MovieSearch(ListView):
    model = Movie
    paginate_by = 8
    template_name = 'cinema_app/search.html'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        else:
            object_list = self.model.objects.none()
        return object_list


class MovieYear(YearArchiveView):
    paginate_by = 4
    template_name = 'cinema_app/year.html'
    
    queryset = Movie.objects.all()
    date_field = 'year_of_production'
    make_object_list = True
    allow_future = True


class MovieStatus(ListView):
    model = Movie
    paginate_by = 8
    template_name = 'cinema_app/moviestatus.html'
    
    def get_queryset(self):
        self.status = self.kwargs['status']
        return Movie.objects.filter(status=self.status)

    def get_context_data(self, **kwargs):
        context = super(MovieStatus, self).get_context_data(**kwargs)
        context['movie_status'] = self.status
        return context


def contact(request): 
    return render(request, 'cinema_app/contact.html')

def terms(request): 
    return render(request, 'cinema_app/terms.html')

