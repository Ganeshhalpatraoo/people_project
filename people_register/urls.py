from django.urls import path

from . import views

urlpatterns = [
    path('', views.people_form, name='people_insert'),  # get and post req. for insert operation
    path('<int:id>/', views.people_form, name='people_update'),  # get and post req. for update operation
    path('delete/<int:id>/', views.people_delete, name='people_delete'),
    path('list/', views.people_list, name='people_list')  # get req. to retrieve and display all records
]
