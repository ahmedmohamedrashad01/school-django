from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('display', views.display, name='display'),
    path('delete/<int:std_id>', views.delete, name='delete'),
    path('edit/<int:std_id>', views.edit, name='edit'),
   

   ]
