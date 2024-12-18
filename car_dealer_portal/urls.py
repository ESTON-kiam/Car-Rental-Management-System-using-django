from django.urls import path, include, re_path

from car_dealer_portal import views
from car_dealer_portal.views import *

# from django.conf.urls import url

urlpatterns = [
    re_path(r'^index/$', index),
    re_path(r'^contact/$', contact),
    re_path(r'^login/$', login),
    re_path(r'^auth/$', auth_view),
    re_path(r'^logout/$', logout_view),
    re_path(r'^register/$', register),
    re_path(r'^registration/$', registration),
    re_path(r'^add_vehicle/$', add_vehicle),
    re_path(r'^manage_vehicles/$', manage_vehicles),
    re_path(r'^order_list/$', order_list),
    re_path(r'^complete/$', complete),
    re_path(r'^history/$', history),
    re_path(r'^delete/$', delete),
    re_path(r'edit_profile/$', edit_profile),
    re_path(r'^view_profile/$', view_profile),
    re_path(r'^updated/$', updated),
    re_path(r'^update_vehicle/(?P<vehicle_id>\d+)/$', views.update_vehicle, name='update_vehicle'),
    re_path(r'^vehicle_chart/$',vehicle_chart),
]