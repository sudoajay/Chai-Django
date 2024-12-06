
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
# This docstring provides an overview of the purpose of this file, describing
# how it routes URLs to views and providing examples for various use cases,
# such as function-based views, class-based views, and including other URL configurations.

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# These imports bring in the necessary Django modules and functions:
# - 'admin' from 'django.contrib' for setting up the admin interface.
# - 'path' from 'django.urls' for mapping URL patterns to views.
# - 'settings' and 'static' from 'django.conf' and 'django.conf.urls.static' 
#   to handle static and media files during development.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweets/', include('tweets.urls'))
    # This line adds a route for the Django admin interface. When a user visits the 
    # URL path 'admin/', they are directed to Django's built-in admin site, which allows
    # administrators to manage the site's content and users.

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# This line adds a configuration for serving media files (like images, videos, etc.)
# during development. The 'static()' function is used to serve media files from the
# directory specified by 'MEDIA_ROOT' when the URL matches 'MEDIA_URL'.

 
# Summary:

#     Development: Use + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) in urls.py and set MEDIA_URL and MEDIA_ROOT in settings.py to serve media files directly from the filesystem.
#     Production: Configure your web server (Nginx or Apache) to serve media files directly, and avoid using Django's development server for this purpose.

# This setup ensures that you can handle media files effectively during development and deploy your application in a way that scales well in production environments.