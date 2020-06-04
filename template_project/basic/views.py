from django.shortcuts import render

# Create your views here.
def index(request):
	data = {'data':'hello world'}
	return render(request,'basic/index.html',{'data':'hello world'})

def other(request):
	return render(request,'basic/other.html')

def relative(request):
	return render(request,'basic/relative_url_template.html')