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
    serializer_class = StatusSerializer

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
        return Response({'alert':'successfully added'})

class AddJobViewset(viewsets.ViewSet):
    def create(self, request):
        admin = User.objects.get(id = request.user.id)
        company = Organisation.objects.filter(admin_name = admin)
        role_name = request.data['role_name']
        location = request.data['location']
        who_can_apply = request.data['who_can_apply']
        salary = request.data['salary']
        skills_req = request.data['skills_req']
        apply_by = request.data['apply_by']
        vacancy = request.data['vacancy']

        addjob = JobPosting.objects.create(
        company = company[0],
        role_name = role_name,
        location = location,
        who_can_apply = who_can_apply,
        salary = salary,
        skills_req = skills_req,
        apply_by = apply_by,
        vacancy = vacancy,
        )

        addjob.save()
        return Response({"alert":"successfully added"})

class RegisterViewset(viewsets.ViewSet):
    permission_classes = (AllowAny,)
    def create(self , request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        try:
            user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    )
            user_type = request.data['user_type']
            profile = Profile.objects.create(
            user = user,
            user_type = user_type,
            )
            profile.save()
            if request.data['user_type'] == 1:
                admin_name = user
                organ_name = request.data['organ_name']
                about_company = request.data['about_company']
                organisation = Organisation.objects.create(
                admin_name = admin_name,
                organ_name = organ_name,
                about_company = about_company,
                )
                organisation.save()
            return Response({'alert':'successfully added'})
        except:
            return Response({"alert":"username already exists"})
