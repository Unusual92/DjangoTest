from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.get_article, name = 'article'),
    path('about/', TemplateView.as_view(template_name='news_blog/about.html'), name='about'),
    
]
