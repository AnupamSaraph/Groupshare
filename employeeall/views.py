from django.utils import timezone
import datetime
from django.db.models import Q
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from django.utils.translation import ugettext_lazy as _
from employeeall.models import Employeeall, EmployeeForm,EditEmployeeForm,Employeehistory,Project,ProjectFormAll,OrganizationForm,DepartmentForm,Organization,Department
from django.template import RequestContext,Context
from django.template.loader import get_template
from django.contrib.auth.models import User

# Add Employee begins here
def contact(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=EmployeeForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=EmployeeForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Employeeall(SSNNO=cleandata['SSNNO'],Title=cleandata['Title'],Name=cleandata['Name'],Email_ID=cleandata['Email_ID'],Fax_No=cleandata['Fax_No'],Home_Phone_No=cleandata['Home_Phone_No'],Office_Phone_No=cleandata['Office_Phone_No'],	Designation=cleandata['Designation'],Address_Line=cleandata['Address_Line'],Order=cleandata['Order'],Date_Added="",Added_By=user,Dep_ID=cleandata['Dep_ID']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':"Employee Record Added Successfully","emp":True} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addemployee/',"emp":True} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Employee's Data",'form':form,'action_url':'/addemployee/',"emp":True} );
		else:
			return HttpResponseRedirect('/accounts/login/');

#Add employee ends here

#Depatment info related to an employee begins here
def deptinfo(request,ssn):
	if request.user.is_authenticated():
		query=Department.objects.get(ID__iexact=ssn);
		return render(request,"showdept.html", {'details':query})

#Department info related to an employee ends here 

#Add Organization form begins here
def addorganization(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=OrganizationForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=OrganizationForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Organization(Name=cleandata['Name'],Address=cleandata['Address'],Contact_No=cleandata['Contact_No'],Mission=cleandata['Mission'],Web_Url=cleandata['Web_Url']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Organization Added Successfully"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addorganization/'} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Organization's Data",'form':form,'action_url':'/addorganization/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Organization form ends here

#organization all display begins here
def displayOrg(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Organization.objects.all();
				t= get_template("organization.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Organization'})
			else:
				return HttpResponseRedirect('/accounts/login/');

#organization all display ends here
# edit organization begins here
def editOrg(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():	
				if request.method=="POST":
					
					form=OrganizationForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Organization.objects.get(ID=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						j.Name=cleandata['Name'];
						j.Address=cleandata['Address'];
						j.Contact_No=cleandata['Contact_No'];
						j.Mission=cleandata['Mission'];
						j.Web_Url=cleandata['Web_Url'];
						j.save();
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Organization.objects.get(ID__exact=ssn)
						form=OrganizationForm(instance=ins);	
					except Organization.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit organization','form':form,'action_url':'editOrg/%s'%(ssn)})




#edit organization ends here

#Add Department form begins here
def addDepartment(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=DepartmentForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=DepartmentForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Department(Name=cleandata['Name'],Address=cleandata['Address'],Contact_No=cleandata['Contact_No'],Organization_ID=cleandata['Organization_ID']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Department Added Successfully"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/adddepartment/'} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Derpartment's Data",'form':form,'action_url':'/adddepartment/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add department form ends here


#Department all display begins here
def displayDept(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Department.objects.all();
				t= get_template("department.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Department'})
			else:
				return HttpResponseRedirect('/accounts/login/');

#Department all display ends here


# edit department begins here
def editDept(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():	
				if request.method=="POST":
					
					form=DepartmentForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Department.objects.get(ID=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						j.Name=cleandata['Name'];
						j.Address=cleandata['Address'];
						j.Contact_No=cleandata['Contact_No'];
						j.Organization_ID=cleandata['Organization_ID'];
						j.save();
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Department.objects.get(ID__exact=ssn)
						form=DepartmentForm(instance=ins);	
					except Department.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit organization','form':form,'action_url':'editDept/%s'%(ssn)})




#edit organization ends here

#Employee belonging to an Department begins here
def dept_employee(request,ssn):
	if request.user.is_authenticated():
		query=Department.objects.get(ID__iexact=ssn);	
		qset = query.employeeall_set.all();
			
		return render(request,"deptemployee.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');



#Employee belonging to an department ends here


#organization Infomation related to a department begins here
def orginfo(request,ssn):
	if request.user.is_authenticated():
		query=Organization.objects.get(ID__iexact=ssn);
		return render(request,"showorg.html", {'details':query})

#organization Infomation related to a department ends here



#Department belonging to an organization begins here
def org_dept(request,ssn):
	if request.user.is_authenticated():
		
		query=Organization.objects.get(ID__iexact=ssn);
		qset = query.department_set.all();			
		return render(request,"department.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');



#Department belonging to an organization ends here



#Employee belonging to an organization begins here
def org_employee(request,ssn):
	li=[];	
	if request.user.is_authenticated():
		query=Organization.objects.get(ID__iexact=ssn);
		q = query.department_set.all();
		for obj in q: 
		
			li.append(obj.ID);
		qset = Employeeall.objects.filter(Dep_ID_id__in=li);			
		return render(request,"deptemployee.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');



#Employee belonging to an organization ends here

def display(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Employeeall.objects.all();
				t= get_template("employee.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Employee',"emp":True})
			else:
				return HttpResponseRedirect('/accounts/login/');

def search(request):
		content=None;	
		if request.user.is_authenticated():	
		
			query=request.POST.get('q');
			qset=None
			content=None;
			if query:
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Employeeall.objects.filter(SSNNO__icontains=query);
				t= get_template("result_table.html");
				content = t.render(Context({'employee':qset}));
			
			return render(request,"home1.html", {'query':query,'content':content,"search":True,"emp":True})
		else:
			return HttpResponseRedirect('/accounts/login/');



def edit(request, ssn):
			 form=None
			 username = None
    			 if request.user.is_authenticated():
        			user = request.user.username
				now=datetime.datetime.now();
				old=Employeeall.objects.get(SSNNO__iexact=ssn);	
				if request.method=="POST":
					
					form=EditEmployeeForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Employeeall.objects.get(SSNNO=ssn);
						#j.EmpID=request.POST['EmpID'];
						
						j.Title=cleandata['Title'];						
						j.Name=cleandata['Name'];
						j.Email_ID=cleandata['Email_ID'];
						j.Fax_No=cleandata['Fax_No'];
						j.Home_Phone_No=cleandata['Home_Phone_No'];
						j.Office_Phone_No=cleandata['Office_Phone_No'];
						j.Designation=cleandata['Designation'];
						j.Address_Line=cleandata['Address_Line'];
						j.Order=cleandata['Order'];
						j.Added_By=user;
						j.Date_Added="";
						j.Comment=cleandata['Comment'];
						j.Dep_ID_id=cleandata['Dep_ID'];
						j.save();
						obj=Employeehistory(SSNNO=old.SSNNO,Dep_ID=old.Dep_ID_id,	Title=old.Title,Name=old.Name,
Email_ID=old.Email_ID,Fax_No=old.Fax_No,Home_Phone_No=old.Home_Phone_No,Office_Phone_No=old.Office_Phone_No,
Designation=old.Designation,Address_Line=old.Address_Line,Added_By=old.Added_By,From=old.Date_Added,To="",Order=old.Order,
Comment=old.Comment);
						
						obj.save();
						return render(request,'home1.html',{'content_title':'Employee Saved',"emp":True})
				else:
					try:	
						ins=Employeeall.objects.get(SSNNO__exact=ssn)
						form=EditEmployeeForm(instance=ins);	
					except Employeeall.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit Employee','form':form,'action_url':'edit/%s'%(ssn),'emp':True})



def edithistory(request):
			content=None;	
			if request.user.is_authenticated():
				query=Employeehistory.objects.all();
				t=get_template("employeeedithistory.html");
				content=t.render(Context({'employee':query}));
				return render(request,"home1.html", {'history':content,'content_title':'History Of Modification','emp':True})
			else:
				return HttpResponseRedirect('/accounts/login/');




def find(request):
		content=None;
		qset=None
		qu=None;
		query=None;
		if request.user.is_authenticated():	
			if request.method=='GET':
				query=request.GET.get('q','');
				if query:
					qu = (Q(SSNNO__icontains=query) | Q(Name__icontains=query));
					qset = Employeeall.objects.filter(qu);
					t= get_template("employee.html");
					content = t.render(Context({'details':qset}));
			
					return render(request,"home1.html", {'empcontent':content,"content_title":"Filtered List",'emp':True})
				else:
					t=get_template("fliterempdis.html");
					content=t.render(Context({}))
					return render(request,"home1.html",{'empcontent':content,'emp':True})
			else:
				t=get_template("fliterempdis.html");
				content=t.render(Context({}))
				return render(request,"home1.html",{'empcontent':content,'emp':True})
		else:
			return HttpResponseRedirect('/accounts/login/');



def filteremp(request):
		content=None;
		qset=None
		qu=None;
		query=None;
		if request.user.is_authenticated():	
			if request.method=='GET':
				query=request.GET.get('q','');
				if query:
					qu = (Q(SSNNO__iexact=query) | Q(Name__icontains=query));
					qset = Employeehistory.objects.filter(qu);
					t= get_template("employeeedithistory.html");
					content = t.render(Context({'employee':qset}));
			
					return render(request,"home1.html", {'empcontent':content,"content_title":"Filtered  Hisory List",'emp':True})
				else:
					t=get_template("fliterempdis.html");
					content=t.render(Context({}))
					return render(request,"home1.html",{'empcontent':content,'emp':True})
			else:
				t=get_template("fliterempdis.html");
				content=t.render(Context({}))
				return render(request,"home1.html",{'empcontent':t,'emp':True})
		else:
			return HttpResponseRedirect('/accounts/login/');


def emphis(request,ssn):
	if request.user.is_authenticated():
		query=Employeehistory.objects.filter(SSNNO__iexact=ssn);
		qset = Employeeall.objects.all();
		t = get_template("employee.html");
		t2=get_template("emphistory.html")
		content = t.render(Context({'details':qset}));
		content2=t2.render(Context({'history':query}));	
		return render(request,"home1.html", {'empcontent':content,'content_title':'All Employee',"emp":True})
	else:
		return HttpResponseRedirect('/accounts/login/');


def emp(request,ssn):
	if request.user.is_authenticated():
		query=Employeehistory.objects.filter(SSNNO__iexact=ssn);
		return render(request,"emphistory.html", {'history':query})

def phonehis(request,ssn):
	if request.user.is_authenticated():
		query=Employeehistory.objects.filter(Office_Phone_No__iexact=ssn);
		return render(request,"phonehistory.html", {'history':query})

def designationhis(request,ssn):
	if request.user.is_authenticated():
		query=Employeehistory.objects.filter(Designation=ssn);
		return render(request,"designationhistory.html", {'history':query})

def empinfo(request,ssn):
	if request.user.is_authenticated():
		query=Employeeall.objects.get(SSNNO__iexact=ssn);
		return render(request,"showemployee.html", {'details':query})

def addproject(request):
		username = None;
		
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=ProjectFormAll();	
		
			if request.method=='POST': # If the form has been submitted...
				form=ProjectFormAll(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Project(Project_ID=cleandata['Project_ID'],Project_Name=cleandata['Project_Name'],Start_Date=cleandata['Start_Date'],End_Date=cleandata['End_Date'],Amt_Sanctioned=cleandata['Amt_Sanctioned'],Amt_Proposed=cleandata['Amt_Proposed'],Expenditure_Last_Year=cleandata['Expenditure_Last_Year'],No_of_Installment=cleandata['No_of_Installment'],Emp_SSNNO=cleandata['Emp_SSNNO'])
					obj.save();	
			            	return render(request,'home1.html',{'content_title':"Project Record Added Successfully"} );

				else:
					
			 	       	return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addproject/'} );
			
			else:
					
		 	       	return render(request,'home1.html',{'content_title': 'Enter the Project Detail','form':form,'action_url':'/addproject/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');




def showproject(request):
			content=None;	
			if request.user.is_authenticated():
				query=Project.objects.all();
				t=get_template("showproject.html");
				content=t.render(Context({'project':query}));
				return render(request,"home1.html", {'history':content,'content_title':'All Project'})
			else:
				return HttpResponseRedirect('/accounts/login/');


def empproject(request,ssn):
	if request.user.is_authenticated():
		q=Employeeall.objects.raw('select distinct SSNNO,Name,Email_ID,Fax_No,Office_Phone_No,Home_Phone_No,Designation,Address_Line from employeeall_employeeall, employeeall_project where employeeall_employeeall.SSNNO=employeeall_project.Emp_SSNNO_id');

		query=Employeeall.objects.get(SSNNO__iexact=ssn);
		qset = query.project_set.all();			
		return render(request,"emppro.html", {'project':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');

def disemppro(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset=Employeeall.objects.raw('select distinct SSNNO,Name,Email_ID,Fax_No,Office_Phone_No,Home_Phone_No,Designation,Address_Line from employeeall_employeeall, employeeall_project where employeeall_employeeall.SSNNO=employeeall_project.Emp_SSNNO_id');				
				t= get_template("empproject.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Employee'})
			else:
				return HttpResponseRedirect('/accounts/login/');

