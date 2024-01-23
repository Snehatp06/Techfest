from django.urls import path
from .import views

app_name='administration'
urlpatterns = [
    path('adminindex',views.admin_index,name='admin_index'),
    path('add',views.add,name='add'),
    path('details',views.details,name='details'),
]