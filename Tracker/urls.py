from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from result.views import SheetViewset

router = routers.DefaultRouter()
router.register(r'sheet', SheetViewset, 'sheet')

urlpatterns = [
    path('', include(router.urls)),
    path('fake-admin/', admin.site.urls),
]
