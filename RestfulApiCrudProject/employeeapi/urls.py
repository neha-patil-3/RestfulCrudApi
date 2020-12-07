from django.urls import re_path

from employeeapi import views

urlpatterns = [
    re_path(r'^employees/$', views.employee_list),
    re_path(r'^employees/(?P<pk>[0-9]+)$', views.employee_detail)
]

