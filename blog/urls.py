from django.urls import path
from . import views


# url patterns for the blog page
urlpatterns = [
    path('blog/', views.BlogList.as_view(), name='blog'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('likes/<slug:slug>/', views.BlogLikes.as_view(), name='blog_likes'),
]
