from django.shortcuts import render

def home(request):
	return render(request,"home.html")
	
def sdashboard(request):
	return render(request, "studentdashboard.html")

def posting(request):
	return render(request,"posting.html")

def stdetail(request):
	return render(request,"studentedudetails.html")
def addjobs(request):
	return render(request,"addjobs.html")

def viewjob(request):
	return render(request,"viewjob.html")

def applicats(request):
	return render(request,"applicants.html")


def eligible(request):
	return render(request,"eligible.html")



