# The final step is to configure our URLs. In the topmost, project-level tutorial/urls.py file add include as an import for the snippets app urls which will appear at the empty string ''.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),  # new
    path("", include("snippets.urls")),
]