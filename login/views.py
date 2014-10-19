from login.form import *
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.template import RequestContext,Context
from employeeall.models import * 
@csrf_protect
def register(request):
	content=None;
	t=None;
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(first_name=form.cleaned_data['first_name'],last_name=cleaned_data['last_name'],email=form.cleaned_data['email'],username=form.cleaned_data['username'],password=form.cleaned_data['password1'])
			user.save()
			return render(request,'home1.html',{'content_title':"Registered Sucessfully"});
		else:                      
			form = RegistrationForm()
    			return render(request,'home1.html',{'content_title':"New User Resigeration",'form':form,'action_url':'/user/register/'});
 	else:
		form= RegistrationForm()
    #return render_to_response('registration/register.html',variables,)
		return render(request,'home1.html',{'content_title':"New User Resigeration",'form':form,'action_url':'/user/register/'} );


def loginpio(request):	
	content=None;
	t=None;
	t=get_template('registration/login.html');
	content=t.render(Context({ }));	
	return render(request,'home1.html',{'empcontent':content});
	
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
#@login_required
def home1(request):
    home=True
    orgset=Organization.objects.all();
    deptset=Department.objects.all();	
    empset=Employeeall.objects.all();
    proset=Project.objects.all();
    actset=Act.objects.all();
    chapset=Chapter.objects.all();
    secset=Section.objects.all();
    thirdset=ThirdParty.objects.all();
    appset=Appointment.objects.all();
    durset=Duration.objects.all();
    padset=PowersAndDuties.objects.all();
    remset=Removal.objects.all();
    degset=Designation.objects.all();	
    return render_to_response('home3.html',{ 'user': request.user ,'home':home,'org_detail':orgset,'dept_detail':deptset,'emp_detail':empset,'pro_detail':proset,'act_detail':actset,
'chap_detail':chapset,'sec_detail':secset,"third_detail":thirdset,"app_detail":appset,"dur_detail":durset,"pad_detail":padset,
'rem_detail':remset,'deg_detail':degset})
