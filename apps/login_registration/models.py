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
			if user and bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8')) == user[0].password:
				print bcrypt.hashpw(password.encode('utf-8'), user[0].password.encode('utf-8'))
				print user[0].password
				return (True, user)
			else:
				messages['register_error'] = "Must register before logging in"
				return(False, messages)

	def update_status(self, username, email, user_id, user_status):
		messages = {}

		if not username and not email:
			messages['all_fields_error'] = "No fields can be blank"
		if messages:
			return (False, messages)
		else:
			user = self.get(id=user_id)
			user.username = username
			user.email = email
			user.user_status = user_status
			user.save()
			messages['update_success'] = "Updated successfully!"
			return (True, messages)
	def update_profile(self, username, email, user_id):
		messages = {}
		if not username and not email: 
			messages['all_fields_error'] = "No fields can be blank"
		if messages:
			return (False, messages)
		else:
			user = self.get(id=user_id)
			user.username=username
			user.email = email
			user.save()
			messages['update_success'] = "Updated successfully"
			return (True, messages)
	def update_password(self, user_id, pw, cpw):
		messages = {}
		if not pw and not cpw:
			messages['all_fields_error'] = "No fields can be blank"
		elif pw != cpw:
			messages['password_error'] = "Passwords must match"
		if messages:
			return (False, messages)
		else:
			user = self.get(id=user_id)
			#bcrypt password
			password = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
			user = self.get(id=user_id)
			user.password = password
			user.save()
			messages['update_success'] = "Updated successfully"
			return (True, messages)

	def update_description(self, description, user_id):
		messages = {}
		if not description:
			messages['description_error'] = "Description can't be blank"
		if messages:
			return(False, messages)
		else:
			user = self.get(id=user_id)
			user.description = description
			user.save()
			messages['update_success'] = 'Updated successfully'
			return (True, messages)
	def delete_user(self, user_id):
		return self.filter(id=user_id).delete()


# Create your models here.
class User(models.Model):
	username = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	description = models.TextField(max_length=2500, default='', editable=True)
	user_status = models.IntegerField(default=0)
	updated_at = models.DateTimeField(auto_now_add = True, auto_now=False)
	created_at = models.DateTimeField(auto_now_add = False, auto_now=True)
	userManager = UserManager()
	objects = models.Manager()

	def __str__(self):
		return self.username
	class Meta:
		db_table = 'users'