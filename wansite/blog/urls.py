from blog import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('<int:year>/', views.year_archive),
    path('<int:year>/<int:month>/', views.month_archive),
    path('<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    path('post/<pk>', views.post_detail, name="post_detail"),
]