from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import *
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    validate_password = make_password
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password','first_name')
        extra_kwargs = {'password':{'write_only':True}}
        read_only_fields = ('id',)

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ('user','user_type')


class ForUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

class OrganisationDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Organisation
        fields = ('user','organ_name','about_company')
        depth = 1


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'
        depth=1
class ForOrganStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = ('organ_name',)

class ForCandidateSerializer(serializers.ModelSerializer):
    user = ForUserSerializer()
    class Meta:
        model = Candidate
        fields = ('stu_name','user',)
        depth = 1

class ForJobPostingSerializer(serializers.ModelSerializer):
    company = ForOrganStatusSerializer()
    class Meta:
        model = JobPosting
        fields = ('company','role_name',)
        depth = 1

class ForStatusSerializer(serializers.ModelSerializer):
    job_posting = ForJobPostingSerializer()
    candidate = ForCandidateSerializer()
    class Meta:
        model = ApplicationStatus
        fields = ('job_posting', 'status', 'candidate',)
        depth=1
class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"

class JobPostingSerializer(serializers.ModelSerializer):
    company = OrganisationSerializer()
    class Meta:
        model = JobPosting
        fields = ('company', 'role_name',)
        depth=1

class StatusSerializer(serializers.ModelSerializer):
    job_posting = JobPostingSerializer()
    candidate = CandidateSerializer()
    class Meta:
        model = ApplicationStatus
        fields = ('job_posting', 'status', 'candidate',)
        depth=1

# class ApplyJobSerializer(serializers.ModelSerializer):
#     user = UserSerializer()
#     class Meta:
#         model = Candidate
#         fields
