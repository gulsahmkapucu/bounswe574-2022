from django.urls import path
from django.views.generic.base import RedirectView

from .views import articles, create, create_article, create_success, join, leave

app_name = 'spaces'

urlpatterns = [
    path('create/', create, name='create'),
    path('create/success/<int:id>', create_success, name='create_success'),
    path('<int:id>', RedirectView.as_view(pattern_name='spaces:articles', permanent=False), name='view'),
    path('<int:id>/join', join, name='join'),
    path('<int:id>/leave', leave, name='leave'),
    path('<int:id>/articles', articles, name='articles'),
    path('<int:space_id>/articles/create', create_article, name='create_article'),
]
