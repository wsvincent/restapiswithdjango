from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
# Create your views here.

class Home(APIView):
	permission_classes = [IsAuthenticated]

	def get(self,request):
		context={}
		# print(request.headers['Authorization'])
		user=request.user
		context['title']='Home Page'
		context['username']=user.username

		return Response(context,status=status.HTTP_200_OK)



class Register(APIView):

	def validate(self,password1,password2):
		if(password1==password2):
			return password1
		return None


	def get(self,request):
		context={}
		context['title']='Registeration Page'
		return Response(context,status=status.HTTP_200_OK)


	def post(self,request):
		context={}
		username=request.data['username']
		password1=request.data['password1']
		password2=request.data['password2']
		password=self.validate(password1,password2)

		if User.objects.filter(username=username):
			context['errMsg']='Username '+username+" is Occupied."
			return Response(context,status=status.HTTP_409_CONFLICT)

		if password:
			# Create User
			user=User.objects.create_user(username=username,password=password)
			user.email=request.data['email']
			user.save()
			# Create Token
			token=Token.objects.create(user=user)
			token.save()

			context['token']=token.key
			return Response(context,status=status.HTTP_201_CREATED)

		else:
			context['errMsg']='Passwords didn\'t match'
			return Response(context,status=status.HTTP_400_BAD_REQUEST)



class Login(APIView):

	def get(self,request):
		context={}
		context['title']='Login Page'
		return Response(context,status=status.HTTP_200_OK)


	def post(self,request):
		context={}
		username=request.data['username']
		password=request.data['password']
		user=authenticate(username=username,password=password)
		
		if user:
			# Retrive User Token
			token=Token.objects.get(user=user)
			context['token']=token.key
			return Response(context,status=status.HTTP_202_ACCEPTED)
		else:
			context['errMsg']='Incorrect username or password'
			return Response(context,status=status.HTTP_401_UNAUTHORIZED)



class Logout(APIView):
	permission_classes = [IsAuthenticated]


	def get(self,request):
		context={}
		# Delete Existing Token
		token=Token.objects.get(user=request.user)
		token.delete()
		# Create New Token
		token=Token.objects.create(user=request.user)
		token.save()
		
		context['title']='Logout Page'
		print("Logout Successful!")
		return Response(context,status=status.HTTP_200_OK)














# Django-Rest Status Codes
	
# Informational - 1xx
# HTTP_100_CONTINUE
# HTTP_101_SWITCHING_PROTOCOLS

# Successful - 2xx
# HTTP_200_OK
# HTTP_201_CREATED
# HTTP_202_ACCEPTED
# HTTP_203_NON_AUTHORITATIVE_INFORMATION
# HTTP_204_NO_CONTENT
# HTTP_205_RESET_CONTENT
# HTTP_206_PARTIAL_CONTENT
# HTTP_207_MULTI_STATUS
# HTTP_208_ALREADY_REPORTED
# HTTP_226_IM_USED	

# Redirection - 3xx
# HTTP_300_MULTIPLE_CHOICES
# HTTP_301_MOVED_PERMANENTLY
# HTTP_302_FOUND
# HTTP_303_SEE_OTHER
# HTTP_304_NOT_MODIFIED
# HTTP_305_USE_PROXY
# HTTP_306_RESERVED
# HTTP_307_TEMPORARY_REDIRECT
# HTTP_308_PERMANENT_REDIRECT

# Client Error - 4xx
# HTTP_400_BAD_REQUEST
# HTTP_401_UNAUTHORIZED
# HTTP_402_PAYMENT_REQUIRED
# HTTP_403_FORBIDDEN
# HTTP_404_NOT_FOUND
# HTTP_405_METHOD_NOT_ALLOWED
# HTTP_406_NOT_ACCEPTABLE
# HTTP_407_PROXY_AUTHENTICATION_REQUIRED
# HTTP_408_REQUEST_TIMEOUT
# HTTP_409_CONFLICT
# HTTP_410_GONE
# HTTP_411_LENGTH_REQUIRED
# HTTP_412_PRECONDITION_FAILED
# HTTP_413_REQUEST_ENTITY_TOO_LARGE
# HTTP_414_REQUEST_URI_TOO_LONG
# HTTP_415_UNSUPPORTED_MEDIA_TYPE
# HTTP_416_REQUESTED_RANGE_NOT_SATISFIABLE
# HTTP_417_EXPECTATION_FAILED
# HTTP_422_UNPROCESSABLE_ENTITY
# HTTP_423_LOCKED
# HTTP_424_FAILED_DEPENDENCY
# HTTP_426_UPGRADE_REQUIRED
# HTTP_428_PRECONDITION_REQUIRED
# HTTP_429_TOO_MANY_REQUESTS
# HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE
# HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS

# Server Error - 5xx
# HTTP_500_INTERNAL_SERVER_ERROR
# HTTP_501_NOT_IMPLEMENTED
# HTTP_502_BAD_GATEWAY
# HTTP_503_SERVICE_UNAVAILABLE
# HTTP_504_GATEWAY_TIMEOUT
# HTTP_505_HTTP_VERSION_NOT_SUPPORTED
# HTTP_506_VARIANT_ALSO_NEGOTIATES
# HTTP_507_INSUFFICIENT_STORAGE
# HTTP_508_LOOP_DETECTED
# HTTP_509_BANDWIDTH_LIMIT_EXCEEDED
# HTTP_510_NOT_EXTENDED
# HTTP_511_NETWORK_AUTHENTICATION_REQUIRED