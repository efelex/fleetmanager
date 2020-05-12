from django.urls import path
from pages.views import home_view, about_view
from . import views
urlpatterns = [
    path('', views.index, name='home_view'),
    path('home', home_view, name='home_view'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('createuser/', views.create_user, name='createuser'),
    path('editprofile/', views.edit_profile, name='editprofile')
]
