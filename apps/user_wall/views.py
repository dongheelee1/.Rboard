from django.shortcuts import render

def index(request):
	print "user_wall"
	return render(request, 'user_wall/wall.html')
