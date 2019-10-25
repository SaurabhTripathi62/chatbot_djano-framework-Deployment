"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
'''from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
]'''#this part was orignal
#===========
from django.conf.urls import url
from django.contrib import admin
from chat_app.views import ChatterBotAppView, ChatterBotApiView
from chatterbot.conversation import Statement

from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from chat_app import views

urlpatterns = [
    url(r'^$', ChatterBotAppView.as_view(), name='main'),
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^api/chatterbot/', ChatterBotApiView.as_view(), name='chatterbot'),
    url('chat',views.ChatterBotApiView.as_view())
]



#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('summary', views.call_model.as_view())   #call_model is class name in view.py *
