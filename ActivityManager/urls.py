from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ActivityManager.views.home', name='home'),
    # url(r'^ActivityManager/', include('ActivityManager.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'philosopher.views.activity.Homepage'),
    url(r'^philosopher/accounts/signup/$', 'philosopher.views.user.Signup', name="Signup"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="Login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/philosopher'}, name="Logout"),
    url(r'^philosopher/accounts/info/(?P<userid>\d+)/$', 'philosopher.views.user.UserInfo', name="UserInfo"),
    url(r'^philosopher/accounts/editinfo/(?P<userid>\d+)/$', 'philosopher.views.user.EditInfo', name="EditUserInfo"),
    url(r'^philosopher/accounts/toggleblack/(?P<userid>\d+)/$', 'philosopher.views.user.ToggleBlack', name="ToggleBlack"),

    url(r'^philosopher/activity/detail/(?P<activityid>\d+)/$', 'philosopher.views.activity.ActivityDetail', name="ActivityDetail"),
    url(r'^philosopher/activity/add/$', 'philosopher.views.activity.AddActivity', name="AddActivity"),
    url(r'^philosopher/activity/examlist/$', 'philosopher.views.activity.ActivityExamList', name="ActivityExamList"),
    url(r'^philosopher/activity/publish/(?P<activityid>\d+)/$', 'philosopher.views.activity.PublishActivity', name="PublishActivity"),
    url(r'^philosopher/activity/delete/(?P<activityid>\d+)/$', 'philosopher.views.activity.DeleteActivity', name="DeleteActivity"),
    url(r'^philosopher/activity/edit/(?P<activityid>\d+)/$', 'philosopher.views.activity.EditActivity', name="EditActivity"),

    url(r'^philosopher/application/apply/(?P<activityid>\d+)/$', 'philosopher.views.application.ApplicationApply', name="ApplicationApply"),
    url(r'^philosopher/application/detail/(?P<applicationid>\d+)/$', 'philosopher.views.application.ApplicationDetail', name="ApplicationDetail"),
    url(r'^philosopher/application/delete/(?P<applicationid>\d+)/$', 'philosopher.views.application.ApplicationDelete', name="ApplicationDelete"),
    url(r'^philosopher/application/handle/(?P<statusid>\d+)/(?P<applicationid>\d+)/$', 'philosopher.views.application.ApplicationHandle', name="ApplicationHandle"),
    url(r'^philosopher/application/edit/(?P<applicationid>\d+)/$', 'philosopher.views.application.ApplicationEdit', name="ApplicationEdit"),

    url(r'^philosopher/activity/search/$', 'philosopher.views.activity.SearchActivity', name="SearchActivity"),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, }),
    
)


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT, 
        }),
   )
