from django import urls
from . import views

urlpatterns = [
    urls.path('', views.post_list, name='post_list'),
    urls.path('post/<int:pk>/', views.post_detail, name='post_detail')
]