from django.urls import path
from . import views


urlpatterns = [
    path('',views.main,name='main'),
    path('<int:page>',views.home,name='home'),
    path('edit-user/<str:id>',views.editUser,name='edit-user'),
    path('create-user/',views.createUser,name='create-user'),
    path('export/',views.download,name='export'),
]
