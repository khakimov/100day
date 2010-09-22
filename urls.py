from django.conf.urls.defaults import *
from django.conf import settings


from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^cto/', include('cto.foo.urls')),
    (r'^admin/', include(admin.site.urls)),

    (r'^$', 'cto.goal.views.index'),
    (r'^(?P<user>\w+)/$', 'cto.goal.views.personal_day'),

    # Uncomment the next line to enable the admin:
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/100day/cto/static'}),
    )
