from django.urls import path
from .import views

app_name='administration'
urlpatterns = [
    path('adminindex',views.admin_index,name='admin_index'),
    path('add',views.add,name='add'),
    path('details/<int:id>/',views.details,name='details'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]