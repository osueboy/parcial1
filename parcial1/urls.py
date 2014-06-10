from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'registroentrada.views.homeview', name='home'),
                       url(r'^checkin/$', 'registroentrada.views.form_empleado', name='checkin'),
                       url(r'^checkin_landing/$', 'registroentrada.views.landing', name='checkin'),
                       url(r'^admin/', include(admin.site.urls))
                       )