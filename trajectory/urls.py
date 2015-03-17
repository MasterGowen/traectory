from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.contrib.auth.decorators import login_required

from .user.views import UserListView, new_user
from .event.views import EventListView
from .trajectory.views import ProgramListView, trajectoryView

urlpatterns = patterns('',
    url(r'^users/$', login_required(UserListView.as_view()), name='users'),
    url(r'^$', new_user, name='create_user'),
    url(r'^traj/(?P<pk>.+)/$', trajectoryView, name='trajectoryView'),

    url(r'^events/$', EventListView.as_view(), name='create_user'),
    url(r'^programs/$', ProgramListView.as_view(), name='programs_list'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
