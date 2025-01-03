"""
URL configuration for FirstProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from FirstApp import views
from MultiViewApp import views as v1
from App1 import views as v2
from App2 import views as v3
urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/',views.display),
    path('welcome2/',views.show),
    path('hello/',views.hello),
    path('dtime/',views.datetime),
    
    #MultiViewApp urls
    path('morn/',v1.f1),
    path('aftn/',v1.f2),
    path('even/',v1.f3),
    
    #App1
    path('f11/',v2.f11),
    #App2
    path('f22/',v3.f22),
    
    # re_path('^.*$/',views.homepage),
    re_path('^.*$',views.homepage),

]
