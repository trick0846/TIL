from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('',views.index,name='index'),
    path('myinfo/',views.myinfo,name='myinfo'),
    path('project/',views.project,name='project'),
    path('skills/',views.skills,name='skills'),

]