#django
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login', name='Login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='Logout'),
    url(r'^send-sms/$', 'send_sms.views.sendSMS', name='Send SMS'),
    url(r'^messages/(?P<page>[0-9]+)$', 'send_sms.views.getMessages', name='Messages'),
    url(r'^contacts/(?P<page>[0-9]+)$', 'send_sms.views.viewContact', name='Contacts'),
    url(r'^contacts/edit/(?P<num>[0-9]+)$', 'send_sms.views.editContact', name='EditContact'),
    url(r'^contacts/edit-group/(?P<groupID>[0-9]+)$', 'send_sms.views.editGroup', name='EditGroup'),
    url(r'^contacts/delete/(?P<num>[0-9]+)$', 'send_sms.views.deleteContact', name='DeleteContact'),
    url(r'^contacts/group/delete/(?P<groupID>[0-9]+)$', 'send_sms.views.deleteGroup', name='DeleteContact'),
    url(r'^template/$', 'send_sms.views.createTemplate', name='CreateTemplate'),
    url(r'^template/(?P<templateID>[0-9]+)$', 'send_sms.views.editTemplate', name='EditTemplate'),
    url(r'^template/delete/(?P<templateID>[0-9]+)$', 'send_sms.views.deleteTemplate', name='DeleteTemplate'),
    url(r'^stats/$', 'send_sms.views.usageStats', name='UserStats'),
    url(r'^analytics/$', 'send_sms.views.analytics', name='Analytics'),
    # dans forum system
    url(r'^support/$', 'send_sms.views.support', name='Support'),
    # url(r'^sandbox/$',  'send_sms.views.sandbox', name='Login'),
)
