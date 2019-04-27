from django.urls import path,include
from webserver.views import *

urlpatterns=[
path('',home),
path('sdashboard/',sdashboard),
path('posting/',posting),
path('stdetail/',stdetail),
path('addjobs/',addjobs),
path('viewjob/',viewjob),
path('applicants/',applicats),
path('eligible/',eligible),

]
