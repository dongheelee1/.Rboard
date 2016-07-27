from __future__ import unicode_literals
import bcrypt
from django.db import models
import re
email_regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

class UserManager(models.Manager):
	def register(self, username, email, password, confirm_password):
		messages = {}
		#validations
		if not username or not email or not password or not confirm_password:
			messages['all_fields_error'] = "No fields can be blank"
		if len(username) < 2: 
			messages['first_name_error'] = "First name is too short"
		if not email_regex.match(email):
			messages['email_error'] = 'Email is not of the correct format'
		if password != confirm_password:
			messages['passwords_error'] = "Passwords don't match"
		else:
			if len(password)<5:
				messages['password_error'] = "Password must be at least 5 characters"

		user_exists = User.objects.filter(email=email)
		print self.all()
		if messages:
			return(False, messages)
		else:
			if user_exists: 
				messages['user_error'] = "User already exists"
				return (False, messages)
			else:
				#bcrypt password
				password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
				#get number of users in database
				users = self.all()
				print users
				if len(users) < 1:
					self.create(username=username, email=email, password=password, user_status=1)
				else:
					self.create(username=username, email=email, password=password, user_status=0)
				messages['user_success'] = 'User successfully registered'
				return (True, messages)

	def login(self, email, password):
		messages = {}
		if not email or not password:
			messages['all_fields_error'] = "No fields can be blank"
		if messages:
			return (False, messages)
		else:
			user = self.filter(email=email)
			print "hello"
			print bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
			print user[0].password

			if user and bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
				return (True, user)
			else:
				messages['register_error'] = "Must register before logging in"
				return(False, messages)



# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	user_status = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now_add = True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add = False, auto_now=True)
	userManager = UserManager()
	objects = models.Manager()

	def __str__(self):
		return self.username
	class Meta:
		db_table = 'users'