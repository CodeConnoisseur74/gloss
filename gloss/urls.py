from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from django.urls import include, path


# Custom 404 view
def custom_page_not_found_view(request, exception):  # noqa: ARG001
    return render(request, 'note/404.html', status=404)


# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('note.urls')),
]

# Static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 handler
handler404 = 'gloss.urls.custom_page_not_found_view'
