"""teacher URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from teacherManage.views import *
from teacher import settings
from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^show/', show),
    url(r'^searchTeacher', search_teacher),
    url(r'^teacherDetails/', show_teacher_details, name="teacherDetails"),
    url(r'^login1/', login1),
    url(r'^register1/', register_choice),
    url(r'^login2/', login2),
    url(r'^register2/', register2),
    url(r'^register_teacher/', register_teacher),
    url(r'^register_student/', register1),
    url(r'^login_teacher/', login_teacher),
    url(r'^register/', register),
    url(r'^login/', login),
    url(r'^back_to_login_student/', login1),
    url(r'^to_login_student/', login1),
    url(r'^back_to_register_student/', register1),
    url(r'^back_to_register_teacher/', register2),
    url(r'^back_to_login_teacher/', login2),
    url(r'^to_login_teacher/', login2),
    # url(r'^tour/', tour),
    url(r'^login_VIP/', login_VIP),
    url(r'^login3/', login3),
    url(r'^(?P<email>\w+)/teacher/', teacher, name="teacher"),
    url(r'^make_appointment/', make_appointment, name="make_appointment"),
    url(r'^rule_appointments/', rule_appointments),
    url(r'^(?P<email>\w+)/show_to_student/', show_to_student, name="show_to_student"),
    url(r'^teacher_update/', teacher_update, name="teacher_update"),
    url(r'^update_details/', update_details),
    url(r'^(?P<pk>\w+)/allow_teacher/$', allow_teacher, name="allow_teacher"),
    url(r'^found_password1/', found_password_choice),
    url(r'^found_student1/', found_student1),
    url(r'^found_teacher1/', found_teacher1),
    url(r'^found_student/', found_student),
    url(r'^found_teacher/', found_teacher),
    url(r'^back_to_index/', index),
    url(r'^submit_appointment/', submit_appointment),
    #url(r'^student_view_appointments/$', student_view_appointments, name="student_view_appointments"),
    #url(r'^view_appointments/', view_appointments, name="view_appointments"),
    url(r'^allow_appointment/', allow_appointment, name="allow_appointment"),
    url(r'^refuse_appointment/', refuse_appointment, name="refuse_appointment"),
    url(r'^index_student/', index_student, name="index_student"),
    url(r'^all_teacher/', all_teacher, name="all_teacher"),
    url(r'^recommend_teacher/', recommend_teacher, name="recommend_teacher"),
    url(r'^change_password/', change_password, name="change_password"),
    url(r'^password_change/', password_change, name="password_change"),
    url(r'^index_teacher/', index_teacher, name="index_teacher"),
    url(r'^teacher_all_teacher/', teacher_all_teacher, name="teacher_all_teacher"),
    url(r'^teacher_information/', teacher_information, name="teacher_information"),
    url(r'^teacher_change_information/', teacher_change_information, name="teacher_change_information"),
    url(r'^teacher_change_password/', teacher_change_password, name="teacher_change_password"),
    url(r'^password_change_teacher/', password_change_teacher, name="password_change_teacher"),
    url(r'^details_to_VIP/', details_to_VIP, name="details_to_VIP"),
    url(r'^VIP_search/', VIP_search),
    url(r'^teacher_find/', teacher_find),
    url(r'^details_to_teacher/', details_to_teacher, name="details_to_teacher"),
    url(r'^look_date/', look_date, name="look_date"),
    url(r'^look_date_teacher/', look_date_teacher, name="look_date_teacher"),
    url(r'^show_to_tour/', show_to_tour),
    url(r'^all_teacher_tour/', all_teacher_tour),
    url(r'^tour_search/', tour_search),
    url(r'^details_to_tour/', details_to_tour, name="details_to_tour"),


]
urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', views.static.serve, {'document_root': settings.MEDIA_ROOT}, name="media")
    ]
