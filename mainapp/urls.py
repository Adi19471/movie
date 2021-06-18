from django.urls import path
from mainapp import views


urlpatterns = [
   
    path('',views.home,name="home"),
    path('detaile/<int:id>/',views.detaile,name="detaile"),
    path('add/',views.add_movies,name='add_movies'),
    path('edit/<int:id>/',views.edit_movies,name="edit_movies"),
    path('del/<int:id>/',views.delete_movie,name="delete_movie"),
]