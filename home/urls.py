
from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router =routers.DefaultRouter()
router.register(r'studentData',views.StudentView,'studentData')
urlpatterns = [
path("api/",include(router.urls)),
path("",views.home,name="home")
]