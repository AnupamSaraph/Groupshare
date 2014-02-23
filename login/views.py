from login.form import *
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.template import RequestContext,Context
 
@csrf_protect
def register(request):
	content=None;
	t=None;
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email']
	            )
			t=get_template('registration/success.html');
			content=t.render(Context({ }));	
		return render(request,'home1.html',{'empcontent':t,'content_title':"Registered Sucessfully"});
	else:                      
		form = RegistrationForm()
    		#variables = RequestContext(request, {'form': form})
 
    #return render_to_response('registration/register.html',variables,)
		return render(request,'home1.html',{'content_title':"New User Resigeration",'form':form,'action_url':'/register/'} );

 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home1(request):
    home=True
    return render_to_response('home1.html',{ 'user': request.user ,'home':home})
