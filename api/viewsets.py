from rest_framework import viewsets
from api.models import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from api.serializers import *
from rest_framework.permissions import AllowAny


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class ProfileViewset(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationDetailSerializer
    permission_classes = (AllowAny,)

class PostingViewset(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class StuDashboardViewset(viewsets.ModelViewSet):
    queryset = ApplicationStatus.objects.all()
    serializer_class = ForStatusSerializer

class ApplyJobViewset(viewsets.ViewSet):
    def create(self, request):
        stu_name = request.data['stu_name']
        age = request.data['age']
        sslc_percent = request.data['sslc_percent']
        pu_percent = request.data['pu_percent']
        degree = request.data['degree']
        course_name = request.data['course_name']
        aggregate = request.data['aggregate']
        about_me = request.data['about_me']
        skills = request.data['skills']
        resume = request.data['resume']
        applyjob = Candidate.objects.create(
        user = User.objects.get(id = request.user.id),
        stu_name = stu_name,
        age = age,
        sslc_percent = sslc_percent,
        pu_percent = pu_percent,
        degree = degree,
        course_name = course_name,
        aggregate = aggregate,
        about_me = about_me,
        skills = skills,
        resume = resume,
        )
        applyjob.save()
        return Response({'alert':'created'})

class AddJobViewset(viewsets.ViewSet):
    def create(self, request):
        admin_name = User.objects.get(id = request.user.id)
        print(admin_name)
        company = Organisation.objects.filter(admin_name = admin_name)
        role_name = request.data['role_name']
        location = request.data['location']
        who_can_apply = request.data['who_can_apply']
        salary = request.data['salary']
        skills_req = request.data['skills_req']
        apply_by = request.data['apply_by']
        vacancy = request.data['vacancy']

        addjob = JobPosting.objects.create(
        company = company,
        role_name = role_name,
        location = location,
        who_can_apply = who_can_apply,
        salary = salary,
        skills_req = skills_req,
        apply_by = apply_by,
        vacancy = vacancy,
        )

        addjob.save()
        return Response({"alert":"success"})
