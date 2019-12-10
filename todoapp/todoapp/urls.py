from django.urls import include, path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

api_urls = [
    path('freelancers/', include('userprofile.urls')),
    path('', include('users.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls)
]

urlpatterns += i18n_patterns(

    path('api/', include(api_urls)),
    path('', include(api_urls)),
    prefix_default_language=False,


)
