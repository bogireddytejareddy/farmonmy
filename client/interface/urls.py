from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^house/$',views.house),
	url(r'^wells/$',views.wells),
	url(r'^farm/$',views.farm),
	url(r'^wells/3d.html/$',views.threed),
	url(r'^3d/$',views.threed,name='3d'),
	url(r'^farm/pie.html/$',views.piechart),
	url(r'^graph/$',views.graph),
	url(r'^analytics/$',views.analytics),
	url(r'^home/$',views.homepage),
]
