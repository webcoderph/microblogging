from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.context_processors import csrf
from forms import MyRegistrationForm
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return HttpResponseRedirect('/posts/all/')

def login(request):
	c = {}
	c.update(csrf(request))
	return render_to_response('login.html', c)

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is not None:
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin')
	else:
		return HttpResponseRedirect('/accounts/invalid')	

def loggedin(request):
	return render_to_response('loggedin.html',{'full_name': request.user.username})

def invalid_login(request):	
	return render_to_response('invalid.html')

def logout(request):
	auth.logout(request)
	return render_to_response('logout.html')	

def register(request):
	if request.method == "POST":
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/login')


	args = {}
	args.update(csrf(request))  
	
	args['form'] = MyRegistrationForm()

	return render_to_response('register.html', args)			




