from django.urls import path ,include
from rest_framework   import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('api/', include(router.urls))
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
