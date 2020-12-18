from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from blog.models import BlogPost, Author
from blog.serializers import BlogPostSerializer, AuthorSerializer


# def author_list(request):
#     authors = Author.objects.all()
#     return render(request, 'blog/author_list.html', {'authors': authors})

class AuthorListView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'name'
    permission_classes = (permissions.AllowAny,)

    def author_list(request):
        authors = Author.objects.all()
        return render(request, 'blog/author_list.html', {'authors': authors})


class BlogPostListView(ListCreateAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)

    def blogpost_list(request):
        blogposts - BlogPost.objects.all()
        return render(request, 'blog/blogpost_list.html', {'blogposts': blogpost})

class BlogPostDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.order_by('-date_created')
    serializer_class = BlogPostSerializer
    lookup_field = 'slug'
    permission_classes = (permissions.AllowAny,)


class BlogPostCategoryView(APIView):
    serializer_class = BlogPostSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        category = data['category']
        queryset = BlogPost.objects.order_by(
            '-date_created').filter(category__iexact=category)

        serializer = BlogPostSerializer(queryset, many=True)

        return Response(serializer.data)
