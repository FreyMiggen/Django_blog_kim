"""trydjango URL Configuration

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
from trydjango.settings import MEDIA_ROOT
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('members/',include('django.contrib.auth.urls')),
    path('members/',include('authentication.urls')),
    path('blog/',include('myblog.urls')),
    path('chat/',include('public_chat.urls')),
    
]

urlpatterns+=static(settings.MEDIA_URL, document_root=MEDIA_ROOT) # whenever go to that media_url, do ahead and follow that media root to locte media files
