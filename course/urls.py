from django.conf.urls import url
from . import views as course_views

app_name = 'course'
urlpatterns = [
    url(r'^$', course_views.index, name = 'index'),
    url(r'^trpage/$', course_views.index2, name = 'index2'),
    url(r'^getname/$', course_views.get_name, name = 'get_name'),
    url(r'^yourname/$', course_views.yourname, name = 'yourname'),
    url(r'^thanks/$', course_views.thanks, name = 'thanks'),
    url(r'^getcontact/$', course_views.get_contact, name = 'get_contact'),
]
