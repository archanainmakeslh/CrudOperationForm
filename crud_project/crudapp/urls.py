from .import views
from django.urls import path

urlpatterns = [
     #  path('',views.demo,name='demo'),
    path('', views.create, name='create'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:taskid>/', views.delete, name='delete'),
    # path('cbvhome/',views.ItemlistView.as_view(), name='cbvhome')
]
