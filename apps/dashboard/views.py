from django.shortcuts import render
from ..login_registration.models import User

def index(request):
	print User.objects.all()
	# get all users to display
	context = {
		'all_users': User.objects.all(), 
		'curr_user': User.objects.filter(id=request.session['user_id'])[0],
	}
	return render(request, 'dashboard/dashboard.html', context)