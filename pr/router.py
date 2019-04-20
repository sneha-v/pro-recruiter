from api.viewsets import *
from rest_framework import routers
from api.viewsets import *

router = routers.DefaultRouter()
router.register(r'user', UserViewset, base_name = 'allusers')
router.register(r'allposting', PostingViewset, base_name = 'postings')
router.register(r'sdashboard',StuDashboardViewset, base_name = 'studash')
router.register(r'applyjob',ApplyJobViewset, base_name = 'applyjobs')
router.register(r'addjob', AddJobViewset, base_name = 'addjob')
router.register(r'register', RegisterViewset, base_name = 'register')
router.register(r'applicants', ApplicantViewset, base_name = 'Applicant')
