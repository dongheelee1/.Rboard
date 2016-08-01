from django.shortcuts import render, redirect
from ..login_registration.models import User
from django.contrib import messages
from django.core.urlresolvers import reverse

def index(request):
	print User.objects.all()
	# get all users to display
	context = {
		'all_users': User.objects.all(), 
		'curr_user': User.objects.filter(id=request.session['user_id'])[0],
	}
	return render(request, 'dashboard/dashboard.html', context)
def show_user_profile(request):
	print "hi"
	context = {
		'user': User.objects.filter(id=request.session['user_id'])[0]
	}
	return render(request, 'dashboard/profile.html', context)
def show_add_user(request):
	return render(request, 'dashboard/add_user.html')
def update_profile(request, my_id):
	print "update_profile"
	username = request.POST['username']
	email = request.POST['email']
	user_results = User.userManager.update_profile(username=username, email=email, user_id=my_id)
	if user_results[0] == True:
		messages.success(request, user_results[1]['update_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)

	return redirect(reverse('show_user_profile'))
def create_user(request):
	print "create_user"
	user_results = User.userManager.register(request.POST['username'], request.POST['email'], request.POST['pw'], request.POST['cpw'])

	if user_results[0] == True:
		messages.success(request, user_results[1]['user_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)
		
	return redirect(reverse('show_add_user'))

def update_description(request, my_id):
	print "update_description"
	description = request.POST['description']
	user_results = User.userManager.update_description(description=description, user_id=my_id)
	if user_results[0] == True:
		messages.success(request, user_results[1]['update_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)
	return redirect(reverse('show_user_profile'))	

def delete_user(request, user_id):
	print "delete_user"
	User.userManager.delete_user(user_id=user_id)
	return redirect(reverse('index'))

def show_admin_edit(request, user_id):
	print user_id
	context = {
		'user': User.objects.filter(id=user_id)[0]
	}
	return render(request, 'dashboard/admin_edit.html', context)

def admin_update_status(request, user_id):
	username = request.POST['username']
	email = request.POST['email']
	user_status = request.POST['user_status']
	user_results = User.userManager.update_status(username=username, email=email, user_id=user_id, user_status=user_status)
	print user_results

	if user_results[0] == True:
		messages.success(request, user_results[1]['update_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)

	return redirect(reverse('show_admin_edit', kwargs={'user_id': user_id}))

def update_password(request, my_id):
	print "hi"
	pw = request.POST['pw']
	cpw = request.POST['cpw']
	user_results = User.userManager.update_password(my_id, pw, cpw)

	if user_results[0] == True:
		messages.success(request, user_results[1]['update_success'])
	else:
		for key, error in user_results[1].iteritems():
			messages.error(request, error)

def admin_update_password(request, user_id):
	update_password(request, user_id)
	return redirect(reverse('show_admin_edit', kwargs={'user_id': user_id}))

def user_update_password(request, my_id):
	update_password(request, my_id)
	return redirect(reverse('show_user_profile'))
