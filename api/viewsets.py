from rest_framework import viewsets
from api.models import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from api.serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token

class TokenViewset(viewsets.ViewSet):
    permission_classes = (AllowAny,)

    def create(self, request):
        tok = request.data['token']
        token = Token.objects.get(key = tok).user
        profile = Profile.objects.get(user = token).user_type
        if(profile==1):
            return Response({"choice":"RECRUITER"})
        else:
            return Response({"choice":"STUDENT"})

class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

class CompanyViewset(viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationDetailSerializer
    permission_classes = (AllowAny,)

class PostingViewset(viewsets.ModelViewSet):
    queryset = JobPosting.objects.all()
    serializer_class = JobPostingSerializer

class StuDashboardViewset(viewsets.ViewSet):
    def list(self, request):
        user = Candidate.objects.filter(user = request.user).first()
        queryset = ApplicationStatus.objects.filter(candidate = user)
        status = StatusSerializer(queryset, many = True)
        return Response(status.data)

class ProfileViewset(viewsets.ViewSet):
    def create(self, request):
        stu_name = request.data['stu_name']
        age = int(request.data['age'])
        sslc_percent = float(request.data['sslc_percent'])
        pu_percent = float(request.data['pu_percent'])
        degree = request.data['degree']
        course_name = request.data['course_name']
        aggregate = float(request.data['aggregate'])
        about_me = request.data['about_me']
        skills = request.data['skills']
        resume = request.FILES['resume']
        applyjob = Candidate.objects.create(
        user = User.objects.get(id = request.user.id),
        stu_name = stu_name,
        age = age,
        sslc_percent = sslc_percent,
        pu_percent = pu_percent,
        degree = degree.upper(),
        course_name = course_name.upper(),
        aggregate = aggregate,
        about_me = about_me,
        skills = skills,
        resume = resume,
        )
        return Response({'alert':'successfully created'})

class EditProfileViewset(viewsets.ViewSet):
    def create(self,request):
        stu_name = request.data['stu_name']
        age = int(request.data['age'])
        sslc_percent = float(request.data['sslc_percent'])
        pu_percent = float(request.data['pu_percent'])
        degree = request.data['degree']
        course_name = request.data['course_name']
        aggregate = float(request.data['aggregate'])
        about_me = request.data['about_me']
        skills = request.data['skills']
        resume = request.FILES['resume']
        applyjob = Candidate.objects.get(user = request.user).update(
        stu_name = stu_name,
        age = age,
        sslc_percent = sslc_percent,
        pu_percent = pu_percent,
        degree = degree.upper(),
        course_name = course_name.upper(),
        aggregate = aggregate,
        about_me = about_me,
        skills = skills,
        resume = resume,
        )
        return Response({'alert':'successfully edited'})


class AddJobViewset(viewsets.ViewSet):
    def create(self, request):
        admin = User.objects.get(id = request.user.id)
        company = Organisation.objects.get(admin_name = admin)
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

class ApplicantViewset(viewsets.ViewSet):
    def list(self, request):
        user = request.user
        organisation = Organisation.objects.get(admin_name = user)
        jobposting = JobPosting.objects.get(company=organisation)
        status = ApplicationStatus.objects.filter(company=jobposting, status='a')
        candidates = [app.candidate for app in status]
        candidate = CandidateSerializer(candidates, many=True)
        return Response(candidate.data)

class ApplicantFilterViewset(viewsets.ViewSet):
    def list(self, request):
        sslc_percent = request.data['sslc_percent']
        pu_percent = request.data['pu_percent']
        aggregate = request.data['aggregate']
        user = request.user
        organisation = Organisation.objects.get(admin_name = user)
        jobposting = JobPosting.objects.get(company=organisation)
        status = ApplicationStatus.objects.filter(company=jobposting, status='a')
        candidate = Candidate.objects.filter(sslc_percent__gte=sslc_percent, pu_percent__gte=pu_percent,aggregate__gte=aggregate)
        candidates = []
        for item in status:
            for cand in candidate:
                if str(item.candidate) == str(cand.stu_name):
                    candidates.append(item.candidate)
        candidate = CandidateSerializer(candidates, many=True)
        return Response(candidate.data)
class FilterJobViewset(viewsets.ViewSet):
    def list(self, request):
        comp = request.data['company']
        loc = request.data['location']
        organisation = [Organisation.objects.get(organ_name = i) for i in comp]
        jobposting1 = [JobPosting.objects.get(company=i) for i in organisation]
        print(jobposting1)
        jobposting2 = [JobPosting.objects.get(location = j) for j in loc]
        print(jobposting2)
        jobs1 = JobPostingSerializer(jobposting1, many=True)
        jobs2 = JobPostingSerializer(jobposting2, many=True)
        serializer = {"jobposting1":jobs1.data,
                        "jobposting2":jobs2.data}
        return Response(serializer)        



class StatusUpdateViewset(viewsets.ViewSet):
    def create(self, request):
        stu_user_id = request.data['id']
        admin = User.objects.get(id = request.user.id)
        organisation = Organisation.objects.get(admin_name = admin)
        jobposting = JobPosting.objects.get(company = organisation)
        user = User.objects.get(id = stu_user_id)
        candidate = Candidate.objects.get(user = user)
        status = ApplicationStatus.objects.filter(candidate = candidate, company =jobposting).update(status = request.data['status'])
        return Response({"alert":"successfully updated"})

class ViewJobPostingsViewset(viewsets.ViewSet):
    def list(self,request):
        user = User.objects.get(id = request.user.id)
        organisation = Organisation.objects.get(admin_name = user)
        jobposting = JobPosting.objects.get(company = organisation)
        post = JobPostingSerializer(jobposting)
        return Response(post.data)

    def create(self,request):
        role_name = request.data['role_name']
        location = request.data['location']
        who_can_apply = request.data['who_can_apply']
        salary = request.data['salary']
        skills_req = request.data['skills_req']
        apply_by = request.data['apply_by']
        vacancy = request.data['vacancy']
        user = User.objects.get(id = request.user.id)
        organisation = Organisation.objects.get(admin_name = user)
        jobposting = JobPosting.objects.get(company = organisation).update(
        role_name = role_name,
        location = location,
        who_can_apply = who_can_apply,
        salary = salary,
        skills_req = skills_req,
        apply_by = apply_by,
        vacancy = vacancy,
        )
        jobposting.save()
        return Response({"alert":"successfully updated"})

    def destroy(self,request, pk = None):
        user = User.objects.get(id = pk)
        organisation = Organisation.objects.get(admin_name = user)
        jobposting = JobPosting.objects.get(company = organisation).delete()
        jobposting.save()
        return Response({"alert":"successfully deleted"})

class ApplyJobViewset(viewsets.ViewSet):
    # permission_classes = (AllowAny,)
    def create(self,request):
        candidate_tab = Candidate.objects.get(user = request.user)
        organisation_name = request.data['organisation_name']
        organisation = Organisation.objects.get(organ_name = organisation_name)
        jobposting = JobPosting.objects.get(company = organisation)
        status = ApplicationStatus.objects.create(
        candidate = candidate_tab,
        company = jobposting,
        status = request.data['status'],
        )
        return Response({"alert":"successfully applied"})
