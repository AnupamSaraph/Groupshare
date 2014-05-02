from django.utils import timezone
import datetime
from django.db.models import Q
from django.shortcuts import render_to_response,render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django import forms
from django.utils.translation import ugettext_lazy as _
from employeeall.models import * #Employeeall,Projecthistory,Organizationhistory,Departmenthistory,Comment,CommentForm,Act,ActForm,Chapter,ChapterForm,Section,SectionForm, EmployeeForm,EditEmployeeForm,Employeehistory,Project,ProjectFormAll,OrganizationForm,DepartmentForm,Organization,Department,ProjectForm,
ActHistory,ChapterHistory,SectionHistory
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
				user = request.user.username
				now=datetime.datetime.now();
				old=Organization.objects.get(ID__iexact=ssn);	
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
						obj=Organizationhistory(Org_ID=old.ID,Name=old.Name,Address=old.Address,Contact_No=old.Contact_No,Mission=old.Mission,Web_Url=old.Web_Url,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Organization.objects.get(ID__exact=ssn)
						form=OrganizationForm(instance=ins);	
					except Organization.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit organization','form':form,'action_url':'editOrg/%s'%(ssn)})




#edit organization ends here

#Organization history begins here
def org_history(request,ssn):
	if request.user.is_authenticated():
		query=Organizationhistory.objects.filter(Org_ID__iexact=ssn);
		return render(request,"organhistory.html", {'details':query})

#Organization history ends here


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
				user = request.user.username
				now=datetime.datetime.now();
				old=Department.objects.get(ID__iexact=ssn);			
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
						obj=Departmenthistory(Dept_ID=old.ID,Name=old.Name,Address=old.Address,Contact_No=old.Contact_No,Modified_By=user,Modified_On="");
						obj.save();
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Department.objects.get(ID__exact=ssn)
						form=DepartmentForm(instance=ins);	
					except Department.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit organization','form':form,'action_url':'editDept/%s'%(ssn)})




#edit department ends here


#Department history begins here
def dept_history(request,ssn):
	if request.user.is_authenticated():
		query=Departmenthistory.objects.filter(Dept_ID__iexact=ssn);
		return render(request,"depthistory.html", {'details':query})

#Department history ends here


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

#Project belonging to an organization begins here
def org_project(request,ssn):
	li=[];
	l=[];	
	if request.user.is_authenticated():
		query=Organization.objects.get(ID__iexact=ssn);
		q = query.department_set.all();
		for obj in q: 
		
			li.append(obj.ID);
		qset = Employeeall.objects.filter(Dep_ID_id__in=li);
		for obj1 in qset:
			l.append(obj1.SSNNO);
		qset1=Project.objects.filter(Emp_SSNNO_id__in=l);			
		return render(request,"showproject.html", {'project':qset1 })
	else:
		return HttpResponseRedirect('/accounts/login/');



#Project belonging to an organization ends here


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


#Edit employee records begins here
def edit(request, ssn):
			 form=None
			 username = None
    			 if request.user.is_authenticated():
        			user = request.user.username
				now=datetime.datetime.now();
				old=Employeeall.objects.get(SSNNO__iexact=ssn);	
				if request.method=="POST":
					
					form=EditEmployeeForm(request.POST,request.FILES);
					if form.is_valid():
						
            					#instance = Employeeall(Order=request.FILES['Order']);
						#instance.save();
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
						j.Order=request.FILES['Order'];
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
					
				return render(request,'home1.html',{'content_title':'Edit Employee','form':form,'action_url':'edit/%s'%(ssn), 'enctype':"multipart/form-data",'emp':True})
#Edit employee records ends here


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


#Edit project records begins here
def edit_project(request, ssn):
			 form=None
			 username = None
    			 if request.user.is_authenticated():
        			user = request.user.username
				now=datetime.datetime.now();
				old=Project.objects.get(Project_ID__iexact=ssn);		
				if request.method=="POST":
					
					form=ProjectForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Project.objects.get(Project_ID=ssn);
						
						j.Project_Name=cleandata['Project_Name'];
						j.Start_Date=cleandata['Start_Date'];
						j.End_Date=cleandata['End_Date'];
						j.Amt_Sanctioned=cleandata['Amt_Sanctioned'];
						j.Amt_Proposed=cleandata['Amt_Proposed'];
						j.Expenditure_Last_Year=cleandata['Expenditure_Last_Year'];
						j.No_of_Installment=cleandata['No_of_Installment'];
						j.Emp_SSNNO=cleandata['Emp_SSNNO'];
						j.save();
						obj=Projecthistory(Project_ID=old.Project_ID,Project_Name=old.Project_Name,Start_Date=old.Start_Date,End_Date=old.End_Date,Amt_Sanctioned=old.Amt_Sanctioned,
Amt_Proposed=old.Amt_Proposed,Expenditure_Last_Year=old.Expenditure_Last_Year,No_of_Installment=old.No_of_Installment,
Modified_By=user,Modified_On="");
						
						obj.save();
						return render(request,'home1.html',{'content_title':'Project Saved'})
				else:
					try:	
						ins=Project.objects.get(Project_ID__exact=ssn)
						form=ProjectForm(instance=ins);	
					except Project.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit Project','form':form,'action_url':'edit_project/%s'%(ssn)})
#Edit project records ends here



def showproject(request):
			content=None;	
			if request.user.is_authenticated():
				query=Project.objects.all();
				t=get_template("showproject.html");
				content=t.render(Context({'project':query}));
				return render(request,"home1.html", {'history':content,'content_title':'All Project'})
			else:
				return HttpResponseRedirect('/accounts/login/');
#Invididual Project Begins here
def viewproject(request,id1):
	content=None;
	if request.user.is_authenticated():
		query=Project.objects.get(Project_ID__exact=id1);
		qu=query.comment_set.all();
		t=get_template("viewproject.html");
		content=t.render(Context({'person':query,'comment':qu}));
		return render(request,"home1.html",{'content':content,'content_title':'Project Information'})
	else:
		return HttpResponseRedirect('/accounts/login');
#Individual Project Ends here

#Project history begins here
def project_history(request,ssn):
	if request.user.is_authenticated():
		query=Projecthistory.objects.filter(Project_ID__iexact=ssn);
		return render(request,"projecthistory.html", {'project':query})

#Project history ends here


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

#File Open begins here

def fileupload(request,name):
	f=open(name);
	content=f.read();
	f.close();
	return render(request,"file.html",{"content":content})

#File Open Ends here

#Comment Form Begins here
def addcomment(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=CommentForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=CommentForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Comment(name=cleandata['name'],website=cleandata['website'],text=cleandata['text'],project=cleandata['project'],created_on="");
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Comment Added"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addcomment/'});

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Add Comment",'form':form,'action_url':'/addcomment/'});
		else:
			return HttpResponseRedirect('/accounts/login/');



#Comment form ends here	_


#Add Act From Begins Here
def addact(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=ActForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=ActForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Act(No=cleandata['No'],Name=cleandata['Name'],Year=cleandata['Year'],Link=cleandata['Link']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Act Added Successfully"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addact/'} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Act's Data",'form':form,'action_url':'/addact/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');

#Add Act ends here

#Show all act begins here
def showallact(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Act.objects.all();
				t= get_template("act.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Act'})
			else:
				return HttpResponseRedirect('/accounts/login/');



#Show all act ends here


#Add Chapter Begins here
def addchapter(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=ChapterForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=ChapterForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Chapter(Chapter_No=cleandata['Chapter_No'],Text=cleandata['Text'],Act_No=cleandata['Act_No']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Chapter Added Successfully"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addchapter/'} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Chapter's Data",'form':form,'action_url':'/addchapter/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add chapter ends here

#Show all chapter begins here

def showallchapter(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Chapter.objects.all();
				t= get_template("chapter.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Chapter'})
			else:
				return HttpResponseRedirect('/accounts/login/');

#Show All chapter ends here

#Add section begins here
def addsection(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=SectionForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=SectionForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Section(Section_No=cleandata['Section_No'],Text=cleandata['Text'],Chapter_No=cleandata['Chapter_No']);
					obj.save();	
		            		return render(request,'home1.html',{'content_title':" Section Added Successfully"} );
				else:
					
		 	       		return render(request,'home1.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addsection/'} );

			else:
					
		 	       	return render(request,'home1.html',{'content_title':"Enter Section's Data",'form':form,'action_url':'/addsection/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');



#Add section ends here

#Show all Section begins here
def showallsection(request):
			content=None;	
			if request.user.is_authenticated():		
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Section.objects.all();
				t= get_template("section.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Section'})
			else:
				return HttpResponseRedirect('/accounts/login/');

#Show all Section ends here

#Edit Act begins here
def editAct(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Act.objects.get(No__iexact=ssn);	
				if request.method=="POST":
					
					form=ActEditForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Act.objects.get(No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Name=cleandata['Name'];
						j.Year=cleandata['Year'];
						j.Link=cleandata['Link'];
						j.save();
						obj=ActHistory(No=old.No,Name=old.Name,Year=old.Year,Link=old.Link,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Act.objects.get(No__exact=ssn)
						form=ActEditForm(instance=ins);	
					except Act.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit Act','form':form,'action_url':'editAct/%s'%(ssn)})



#Edit Act ends here


#Edit Chapter begins here
def editChapter(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Chapter.objects.get(Chapter_No__iexact=ssn);
				no=old.Act_No;	
				if request.method=="POST":
					
					form=ChapterEditForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Chapter.objects.get(Chapter_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Act_No=cleandata['Act_No'];
						j.save();
						obj=ChapterHistory(Chapter_No=old.Chapter_No,Text=old.Text,Act_No=no.No,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Chapter.objects.get(Chapter_No__exact=ssn)
						form=ChapterEditForm(instance=ins);	
					except Chapter.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit Chapter','form':form,'action_url':'editChapter/%s'%(ssn)})
#Edit Chapter ends here


#Edit Section begins here
def editSection(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Section.objects.get(Section_No__iexact=ssn);
				no=old.Chapter_No;	
				if request.method=="POST":
					
					form=SectionEditForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Section.objects.get(Section_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Chapter_No=cleandata['Chapter_No'];
						j.save();
						obj=SectionHistory(Section_No=old.Section_No,Text=old.Text,Chapter_No=no.Chapter_No,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'home1.html',{'content_title':'Updated Successfully'})
				else:
					try:	
						ins=Section.objects.get(Section_No__exact=ssn)
						form=SectionEditForm(instance=ins);	
					except Section.DoesNotExist:
						ins=None;
					
				return render(request,'home1.html',{'content_title':'Edit Section','form':form,'action_url':'editSection/%s'%(ssn)})
#Edit Section ends here

#Chapter belonging to an Act begins here
def act_chapter(request,ssn):
	if request.user.is_authenticated():
		
		query=Act.objects.get(No__iexact=ssn);
		qset = query.chapter_set.all();			
		return render(request,"chapter.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');

#Chapter belonging to an act ends here

#Section belonging to an Chapter begins here
def chapter_section(request,ssn):
	if request.user.is_authenticated():
		
		query=Chapter.objects.get(Chapter_No__iexact=ssn);
		qset = query.section_set.all();			
		return render(request,"section.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');

#Section belonging to an chapter ends here

#Section belonging to an act ends here
def act_section(request,ssn):
	li=[];	
	if request.user.is_authenticated():
		query=Act.objects.get(No__iexact=ssn);
		q = query.chapter_set.all();
		for obj in q: 
		
			li.append(obj.Chapter_No);
		qset = Section.objects.filter(Chapter_No_id__in=li);			
		return render(request,"section.html", {'details':qset })
	else:
		return HttpResponseRedirect('/accounts/login/');

#Section belonging to an act ends here

#Show Act from chapter begins here
def showact(request,ssn):
	if request.user.is_authenticated():
		
		query=Act.objects.get(No__iexact=ssn);			
		return render(request,"showact.html", {'details':query })
	else:
		return HttpResponseRedirect('/accounts/login/');
#Show Act from chapter begins here

#Show chapter from section begins here
def showchapter(request,ssn):
	if request.user.is_authenticated():
		
		query=Chapter.objects.get(Chapter_No__iexact=ssn);			
		return render(request,"showchapter.html", {'details':query })
	else:
		return HttpResponseRedirect('/accounts/login/');
#Show Chapter from section begins here

#Show act history begins here
def acthistory(request,ssn):
	if request.user.is_authenticated():
		query=ActHistory.objects.filter(No__iexact=ssn);
		return render(request,"acthistory.html", {'details':query})


#shoe act history ends here

#Show chapter history begins here
def chapterhistory(request,ssn):
	if request.user.is_authenticated():
		query=ChapterHistory.objects.filter(Chapter_No__iexact=ssn);
		return render(request,"chapterhistory.html", {'details':query})


#show chapter history ends here

#Show section history begins here
def sectionhistory(request,ssn):
	if request.user.is_authenticated():
		query=SectionHistory.objects.filter(Section_No__iexact=ssn);
		return render(request,"sectionhistory.html", {'details':query})


#show section history ends here

