from django.urls import path
from .views import HomeList


app_name = 'Home'

urlpatterns = [
    path('' , HomeList.as_view() , name='Home_List')
]
