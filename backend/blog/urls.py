from django.urls import path
from . import views
from .views import BlogPostListView, BlogPostDetailView, BlogPostCategoryView, AuthorListView


urlpatterns = [
    path('author', AuthorListView.as_view()),
    path('', BlogPostListView.as_view()),
    path('category/', BlogPostCategoryView.as_view()),
    path('/', BlogPostDetailView.as_view()),
]
