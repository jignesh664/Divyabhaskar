from django.shortcuts import render,redirect
from .models import User,Post,Like
# Create your views here.



def index(request):
	return render(request,'index.html')

def signup(request):
	if request.method=="POST":
		try:
			user=User.objects.get(email=request.POST['email'])
			msg='Email Already Exists'
			return render(request,'signup.html',{'msg':msg})
		except:		
			if request.POST['password']==request.POST['cpassword']:
				User.objects.create(
					fname=request.POST['fname'],
					lname=request.POST['lname'],
					mobile=request.POST['mobile'],
					email=request.POST['email'],
					password=request.POST['password'],
					cpassword=request.POST['cpassword'],
					address=request.POST['address'],
				)
				msg="Sign Up Successfully"
				return render(request,'login.html',{'msg':msg})
			else:
				msg="Password and Confirm Password Does Not Matched"
				return render(request,'signup.html',{'msg':msg})

	else:		
		return render(request,'signup.html')	


def login(request):
	if request.method=="POST":
		if request.POST['action']=='Login':
			try:

				user=User.objects.get(
				email=request.POST['email'],
				password=request.POST['password']
				)
				if user:
					request.session['email']=user.email
					request.session['fname']=user.fname
					return render(request,'index.html')
			except:
				msg="Username and Password Invalid"	
				return render(request,'login.html',{'msg':msg})		
		else:
			pass
	return render(request,'login.html')	
def logout(request):
	try:
		del request.session['email']

		return render(request,'login.html')
	except:
		pass


def post(request):
	if request.method=="POST":
		user=User.objects.get(email=request.session['email'])
		post=Post.objects.create(
			user=user,
			comment=request.POST['comment']
			)
		Like.objects.create(
				user=user,
				post=post,
				like=False	
			)
		msg="Post Added Successfully"
		likes=Like.objects.all()
		return render(request,'social.html',{'likes':likes,'msg':msg})
	else:
		likes=Like.objects.all()
		return render(request,'social.html',{'likes':likes})

def like(request,pk):
	
	post=Post.objects.get(pk=pk)
	user=User.objects.get(email=request.session['email'])

	try:
		print("try called")
		likes=Like.objects.get(post=post)
		print("Object Fetched")
		if likes.like==True:
			likes.like=False
			likes.save()
		elif likes.like==False:
			likes.like=True
			likes.save()
		
		likes=Like.objects.all()
		return render(request,'social.html',{'likes':likes})		
	except:
		print("Except Called")
		likes=Like.objects.all()
		return render(request,'social.html',{'likes':likes})


