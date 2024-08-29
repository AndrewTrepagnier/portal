"""
URL configuration for my_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add ia URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
        path("", include("portal.urls")), 
        
        path('admin/', admin.site.urls),
]

"""
The include() allows for other for referencing other URLconfigs. When Django encounters a include(), it chops off whatever partof the URL matched up to 
that point and sends the remianing string to the encountered urlconfig, portal.urls for further processing


including say 'portal/' within the quotes will make your new root url newideas.live/portal, otherwise, the view is just routed to newideas.live


"""

