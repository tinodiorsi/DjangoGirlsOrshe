from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^administration/', include(admin.site.urls)),
    url(r'^kutya/', include(admin.site.urls)),
    url(r'', include('blog.urls'))
]
