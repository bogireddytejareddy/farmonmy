from django.conf.urls import url, include
from rest_framework import routers
from datastorage import views
from django.contrib import admin
from django.contrib.gis import admin

router = routers.DefaultRouter()
router.register(r'^personal', views.Personal_InfoViewSet),
router.register(r'^house_keys', views.House_Info_KeysViewSet),
router.register(r'^farm_keys', views.Farm_Info_KeysViewSet),
router.register(r'^house', views.House_InfoViewSet),
router.register(r'^farms', views.Farm_InfoViewSet),
router.register(r'^crops', views.Crop_InfoViewSet),
router.register(r'^wells', views.Wells_InfoViewSet),

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),
]
