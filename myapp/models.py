from django.db import models
from django.utils import timezone
# Create your models here.

class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	mobile=models.CharField(max_length=100)
	email=models.EmailField()
	password=models.TextField()
	cpassword=models.TextField()
	address=models.CharField(max_length=100)



	def __str__(self):
		return self.fname+" "+self.lname

class Post(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	comment=models.TextField(max_length=200)

class Like(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post=models.ForeignKey(Post,on_delete=models.CASCADE)
	like=models.BooleanField(default=False)


	def __str__(self):
		return self.user.fname+" - "+self.post.comment
