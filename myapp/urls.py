from django.urls import path
from myapp import views
app_name="myapp" #is used to create a namespace\

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('fact/<n>',views.fact,name="fact"),
    #path("secondarysuffix",address of function,name of mapping)
    path('base',views.base,name="base"),
    path('child',views.child,name="child"),
]
