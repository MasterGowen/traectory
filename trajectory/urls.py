from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.auth.decorators import login_required

from .user.views import UserListView, new_user
from .event.views import EventListView
from .trajectory.views import trajectory_view, trajectory_save, stats
from .files.views import user_files, delete

urlpatterns = patterns('',
    url(r'^users/$', login_required(UserListView.as_view()), name='users'),
    url(r'^$', new_user, name='create_user'),
    url(r'^tr/(?P<pk>.+)/$', trajectory_view, name='trajectoryView'),
    url(r'^save/$', trajectory_save, name='trajectorySave'),
    url(r'^stats/$', stats, name='stats'),

    url(r'^files/(?P<pk>.+)/$', user_files, name='Files'),
    url(r'^delete/(?P<pk>.+)/(?P<user_id>.+)/$', delete, name='delete'),

    url(r'^events/$', EventListView.as_view(), name='create_user'),

    url(r'^admin/', include(admin.site.urls)),
)

#urlpatterns += patterns('',
#    url(r'^captcha/', include('captcha.urls')),
#)

urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))