

from django.urls import path,include
from webserver.views import *




urlpatterns=[
path('',home),
path('sdashboard/',sdashboard),

]
