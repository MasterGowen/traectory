from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from django.contrib.auth.decorators import login_required

from .user.views import UserListView, new_user
from .event.views import EventListView
from .trajectory.views import trajectory_view, trajectory_save, stats
from .files.views import user_files, delete
from .contest.views import create_contest_item, read_contest_item_all, read_contest_item, create_contest_item_rank

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
                       url(r'^contest/add_new/$', create_contest_item, name='create_contest_item'),
                       url(r'^contest/all/$', read_contest_item_all, name='read_contest_item_all'),
                       url(r'^contest/(?P<pk>\d+)/$', read_contest_item, name='read_contest_item'),
                       url(r'^contest/(?P<pk>\d+)/rank/$', create_contest_item_rank, name='create_contest_item_rank'),
                       )

urlpatterns += patterns('',
                        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                            'document_root': settings.MEDIA_ROOT
                        }))

if settings.DEBUG404:
    urlpatterns += patterns('',
                            (r'^notv/static/(?P<path>.*)$', 'django.views.static.serve',
                             {'document_root': settings.STATIC_ROOT}
                            ),
    )