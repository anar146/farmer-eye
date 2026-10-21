from django.contrib import admin
from django.urls import path
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from scans.views import scan, history

def health(request):
    return JsonResponse({"app": "Farmer Eye", "status": "ok"})

urlpatterns = [
    path("", health),
    path("admin/", admin.site.urls),
    path("api/scan/", scan),
    path("api/scans/", history),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
