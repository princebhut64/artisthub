from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from random import *
from .utils import *

def index(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		tid=Team.objects.all().order_by('-id')
		if uid.role =="Artist":
			context={
							'uid':uid,
							'tid':tid,
						}
			return render(request,'index.html',{'context':context})
		else:
			context={
							'uid':uid,
							'tid':tid,
						}
			return render(request,'userindex.html',{'context':context})
	else:
		return render(request,'signup.html')

def login(request):
	if request.method=="POST":
			email=request.POST['email']
			password=request.POST['password']
			try:
				uid=User.objects.get(email=email)
				if uid:
					if uid.password==password and uid.role=='Artist':
						request.session['s_email']=uid.email
						context={
							'uid':uid,
						}
						
						return render(request,'shopregister.html',{'context':context})
					elif uid.password==password and uid.role=="User":
						request.session['s_email']=uid.email
						context={
							'uid':uid,
						}
						return render(request,'userindex.html',{'context':context})
					else:
						s_msg='Your password is incorrect'
						return render(request,'login.html',{'s_msg':s_msg})
				else:
					s_msg='Email Does Not Exist '
					return render(request,'login.html',{'s_msg':s_msg})
			except:
				s_msg='Email Does not Exist'
				return render(request,'login.html',{'s_msg':s_msg})
	else:
		return render(request,'login.html')

def forgot_password(request):
    return render(request,'forgot_password.html') 

def send_otp(request):
	# try:
	email=request.POST['email']
	generate_otp=randint(1111,9999)
	uid=User.objects.get(email=email)
	if uid:
		uid.otp=generate_otp
		uid.save()   #update
		sendmail(" Forgot Password ","mail_template",email,{'otp':generate_otp,'uid':uid})
		return render(request,'reset_password.html',{'email':email,'otp':generate_otp})
	else:
		e_msg="Email does not exist"
		return render(request,'forgot_password.html',{'e_msg':e_msg})
    # except:
    #     e_msg="Email does not exist"
    #     return render(request,'forgot_password.html',{'e_msg':e_msg})
		
def reset_password(request):
	try:
		email=request.POST['email']
		otp=request.POST['otp']
		otp1=request.POST['otp1']
		password=request.POST['password']
		cpassword=request.POST['cpassword']
		uid=User.objects.get(email=email)
		print("-----------",email)
		if uid:
			if otp1==otp and password==cpassword:
				
				uid.password=password
				uid.save()
				s_msg="password reset succesfully"
				return render(request,'login.html',{'s_msg':s_msg})
			else:
				s_msg="invalid otp or password"
				return render(request,'reset_password.html',{'s_msg':s_msg})
	except:
		s_msg="invalid Email"
		return render(request,'login.html',{'s_msg':s_msg})

def logout(request):
	if 's_email' in request.session:
		del request.session['s_email']
		return render(request,'signup.html')
	else:
		return render(request,'signup.html')

def signup(request):
	if request.POST:
		if request.POST['choice']=='User':
			fname=request.POST['fname']
			lname=request.POST['lname']
			contact=request.POST['contact']
			email=request.POST['email']
			password=request.POST['password']
			repassword=request.POST['repassword']
			if password==repassword:
				
				uid=User.objects.create(fname=fname,lname=lname,contactno=contact,email=email,password=password,role=request.POST['choice'])
				s_msg='Your Registration successfully'
				
				return render(request,'login.html',{'s_msg':s_msg})
			else:
				s_msg='Email already Exist'
				return render(request,'signup.html',{'s_msg':s_msg})
		else:
			fname=request.POST['fname']
			lname=request.POST['lname']
			contact=request.POST['contact']
			email=request.POST['email']
			password=request.POST['password']
			repassword=request.POST['repassword']
			if password==repassword:
				print("------------->",fname)
				uid=User.objects.create(fname=fname,lname=lname,contactno=contact,email=email,password=password,role=request.POST['choice'])
				s_msg='Your Registration successfully'
				return render(request,'login.html',{'s_msg':s_msg})
			else:
				s_msg='Email already Exist'
				return render(request,'signup.html',{'s_msg':s_msg})
	else:
		return render(request,'signup.html')
			
def albums(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		context={
				'uid':uid,
			}
		if uid.role=="Artist":
			
			return render(request,'albums.html',{'context':context})
		else:
			
			return render(request,'useralbums.html',{'context':context})
	else:
		return render(request,'login.html')
	
def comingsoon1(request):
	return render(request,'comingsoon1.html')

def events(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		eid=Events.objects.all().order_by('-id')
		context={
			'uid':uid,
			'eid':eid,
		}
		if uid.role=="Artist":
			return render(request,'events.html',{'context':context})
		else:
			return render(request,'userevents.html',{'context':context})
	else:
		return render(request,'login.html')

def faq(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		context={
			'uid':uid,	
		}
		if uid.role=="Artist":
			return render(request,'faq.html',{'context':context})
		
		else:
			return render(request,'userfaq.html',{'context':context})
	else:
		return render(request,'login.html')
	
def gallery1(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		if uid.role=="Artist":
			context={
				'uid':uid,
			}
			return render(request,'gallery1.html',{'context':context})
		else:
			context={
				'uid':uid,
			}
			return render(request,'usergallery.html',{'context':context})
	else:
		return render(request,'login.html')

def shopregister(request):
	if 's_email' in request.session:
		if request.POST:
			uid=User.objects.get(email=request.session['s_email'])
			a_fname=request.POST['a_fname']
			a_lname=request.POST['a_lname']
			a_email=request.POST['a_email']
			a_address=request.POST['a_address']
			a_city=request.POST['a_city']
			a_postcode=request.POST['a_postcode']
			a_phone=request.POST['a_phone']
			a_state=request.POST['a_state']
			a_country=request.POST['a_country']
			a_fax=request.POST['a_fax']
			a_description=request.POST['a_description']
			try:
				a_profile_pic=request.FILES['a_profile_pic']
				aid=Artist.objects.create(user_id=uid,address=a_address,city=a_city,postcode=a_postcode,State=a_state,country=a_country,fax=a_fax,profile_pic=a_profile_pic,description=a_description)
				context={
					'uid':uid,
					'aid':aid

				}
				return render(request,'index.html',{'context':context})
			except:
				aid=Artist.objects.create(user_id=uid,address=a_address,city=a_city,postcode=a_postcode,State=a_state,country=a_country,fax=a_fax,description=a_description)
				context={
					'uid':uid,
					'aid':aid

				}
				return render(request,'index.html',{'context':context})

		else:
			uid=User.objects.get(email=request.session['s_email'])
			context={
				'uid':uid
			}
			return render(request,'shopregister.html',{'context':context})
	else:
		return render(request,'login.html')

def shop(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		aid=Artist.objects.all().order_by('-id')
		context={
			'uid':uid,
			'aid':aid
		}
		if uid.role=="Artist":
			return render(request,'shop.html',{'context':context})
		else:
			return render(request,'usershop.html',{'context':context})

	else:
		return render(request,'login.html')

def singlealbum(request):
	return render(request,'singlealbum.html')

def team(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		tid=Team.objects.all().order_by('-id')
		if uid.role=="Artist":		
			context={
				'uid':uid,
				'tid':tid,
			}
			return render(request,'team.html',{'context':context})
		else:
			context={
				'uid':uid,
				'tid':tid,
			}
			return render(request,'userteam.html',{'context':context})
	else:
		return render(request,'login.html')

def teamsingle(request):
	return render(request,'userteam.html')

def about(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		if uid.role=="Artist":		
			context={
				'uid':uid,
			}
			return render(request,'about.html',{'context':context})
		else:
			context={
				'uid':uid,
			}
			return render(request,'userabout.html',{'context':context})
	else:
		return render(request,'login.html')
	
def shopproduct(request,pk):
	if 's_email' in request.session:
		if request.POST:
			uid=User.objects.get(email=request.session['s_email'])
			aid=Artist.objects.get(id=pk)
			a_email=aid.user_id.email
			fname=request.POST['fname']
			lname=request.POST['lname']
			email=request.POST['email']
			address=request.POST['address']
			city=request.POST['city']
			phone=request.POST['phone']
			event_name=request.POST['event_name']
			event_date=request.POST['event_date']         
			budget=request.POST['budget']
			description=request.POST['description']
			
			bookaid=BookArtist.objects.create(user_id=uid,artist_id=aid,address=address,city=city,event_name=event_name,event_date=event_date,budget=budget,description=description)
			bookaid=BookArtist.objects.all()
			context={
				'uid':uid,
				'aid':aid,
				'bookaid':bookaid,
				'fname':fname,
				'event_name':event_name,'event_date':event_date,'description':description,'budget':budget,
			}
			BookArtistMail(" Book Artist ","book_artist_mail",a_email,{'fname':fname,'aid':aid,'bookaid':bookaid,'event_name':event_name,'event_date':event_date,'budget':budget,'description':description})
			
			return render(request,'userindex.html',{'context':context})
		else:
			uid=User.objects.get(email=request.session['s_email'])
			aid=Artist.objects.get(id=pk)
			context={
				'uid':uid,
				'aid':aid,
			}
			return render(request,'shopproduct.html',{'context':context})
		uid=User.objects.get(email=request.session['s_email'])
		aid=Artist.objects.get(id=pk)
		
		context={
			'uid':uid,
			'aid':aid,
		}
		return render(request,'shopproduct.html',{'context':context})
	else:
		return render(request,'login.html')
	
def contact4(request):
	if 's_email' in request.session:
		if request.POST:
			uid=User.objects.get(email=request.session['s_email'])
			name=request.POST['name']
			phone=request.POST['phone']
			email=request.POST['email']
			subject=request.POST['subject']
			message=request.POST['message']
			cid=Contact.objects.create(fullname=name,contactno=phone,email=email,message=message,subject=subject)
			context={
				'uid':uid,
				'cid':cid,
			}
			
			if uid.role=="Artist":
				return render(request,'contact4.html',{'context':context})
			else:
				
				return render(request,'usercontact4.html',{'context':context})
		else:
			uid=User.objects.get(email=request.session['s_email'])
			context={
					'uid':uid,	
				}
			if uid.role=="Artist":
				return render(request,'contact4.html',{'context':context})
			else:
				return render(request,'usercontact4.html',{'context':context})
	else:
		return render(request,'login.html')

def userlist(request):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		aid=Artist.objects.get(user_id=uid)
		bookaid=BookArtist.objects.filter(artist_id=aid)
		context={
			'uid':uid,
			'aid':aid,
			'bookaid':bookaid                
		}
		return render(request,'auserlist.html',{'context':context})
	else:
		return render(request,'login.html')

def ver_user(request,pk):
	if 's_email' in request.session:
		uid=User.objects.get(email=request.session['s_email'])
		aid=Artist.objects.get(user_id=uid)
		bookaid=BookArtist.objects.get(id=pk)
		a_email=bookaid.user_id.email
		fname=bookaid.user_id.fname
		event_name=bookaid.event_name
		afname=aid.user_id.fname

		if bookaid.is_verified == False:
			bookaid.is_verified = True
			bookaid.save()
			EventApproveMail(" Event Approve from Artist ","event_approve_mail",a_email,{'fname':fname,'event_name':event_name,'afname':afname})
		elif bookaid.is_verified == True:    
			bookaid.is_verified = False
			bookaid.save()
		bookaid=BookArtist.objects.filter(artist_id=aid)
		context={
			'uid':uid,
			'aid':aid,
			'bookaid':bookaid
		}
		return render(request,'auserlist.html',{'context':context})
	else:
		return render(request,'login.html')

def newsletter(request):
	if 's_email' in request.session:
		print('-------------------------------')
		uid=User.objects.get(email=request.session['s_email'])
		print('-------------------------',email)
		tid=Team.objects.all().order_by('-id')
		if uid.role =="Artist":
			if request.POST:
				email=request.POST['email']
				
				nsid=Newsletter.objects.create(email=email)
				context={
								'uid':uid,
								'tid':tid,
							}
				return render(request,'index.html',{'context':context})
			
		else:
			if request.POST:
				email=request.POST['email']
				nsid=Newsletter.objects.create(email=email)
				context={
								'uid':uid,
								'tid':tid,
							}
				return render(request,'userindex.html',{'context':context})
			
	else:
		return render(request,'login.html')


# if bid.is_verified == False:
# 			bid.is_verified = True
# 			bid.save()
# 		elif bid.is_verified == True:    
# 			bid.is_verified = False
# 			bid.save()
# 		context={
# 			'uid':uid,
# 			'aid':aid,
# 			'bookaid':bookaid
# 		}


#  if "m_email" in request.session:
#         uid=User.objects.get(email=request.session['m_email']) 
#         cid=Member.objects.get(user_id=uid)           
#         vid=Visitors.objects.filter(vm_id=cid.m_id)
#         context={
#             "uid":uid,
#             "cid":cid,
#             "vid":vid,
#         }
#         return render(request,"member/m_view_visitors.html",{"context":context})
#     else:
#         return render(request,'member/m_login.html')