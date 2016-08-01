from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
from django.core.urlresolvers import reverse
def show_login(request):
	print "login"
	return render(request, 'login_registration/login.html')

def show_register(request):
	print "register"
	return render(request, 'login_registration/register.html')
	
def create_login(request):
	user_results = User.userManager.login(request.POST['email'], request.POST['pw'])
	print user_results
	print User.objects.all()
	if user_results[0] == True:
		request.session['username'] = user_results[1][0].username
		request.session['user_id'] = user_results[1][0].id
		return redirect('../../dashboard')
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)
	return redirect(reverse('show_login'))
	
def create_register(request):
	user_results = User.userManager.register(request.POST['username'], request.POST['email'], request.POST['pw'], request.POST['cpw'])

	if user_results[0] == True:
		messages.success(request, user_results[1]['user_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)
		
	return redirect(reverse('show_register'))
