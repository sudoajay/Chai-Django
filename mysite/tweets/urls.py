
# The urls.py file in Django is crucial for defining how URLs are routed to views in your application. 
# It helps manage different paths and ensure that requests are handled by the correct view. 
# The example provided sets up the basic routing for the admin interface and serves media files during development,
#  but it can be extended to include additional routes for your application's views.


"""
URL configuration for mysite project.

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
from django.urls import path


urlpatterns = [
    # path('', admin.site.urls),

    # This line adds a route for the Django admin interface. When a user visits the 
    # URL path 'admin/', they are directed to Django's built-in admin site, which allows
    # administrators to manage the site's content and users.

] 