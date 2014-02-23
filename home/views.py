# Create your views here.
from django.shortcuts import render_to_response

def index(request):
	home=True;
        return render_to_response('home.html',{'home':True,'style':"/static/css/style.css"} );
 
