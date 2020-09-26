from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import handler404, handler500, handler403, handler400
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
	]
urlpatterns += staticfiles_urlpatterns()

# page not found
handler404 = 'home.views.view_error'
#server error
handler500 = 'home.views.view_error'
#perm my_custom_permission_denied_view
handler403 = 'home.views.view_error'
#bad request
handler400 = 'home.views.view_error'
