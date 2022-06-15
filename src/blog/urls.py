from django.urls import path
from . import views
from .views import PostCreateView,PostUpdateView,PostDeleteView


urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('post_detail/<int:post_id>',views.post_detail,name='post_detail'),
    path('new_post/',PostCreateView.as_view(),name='new_post'),
    path('post_detail/<slug:pk>/update',PostUpdateView.as_view(),name='post_update'),
    path('post_detail/<slug:pk>/delete',PostDeleteView.as_view(),name='post_delete'),

    
]
