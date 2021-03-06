from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from io import BytesIO
from reportlab.pdfgen import canvas
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
from django.forms.models import model_to_dict
import json
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
					obj=Employeeall(SSNNO=cleandata['SSNNO'],Title=cleandata['Title'],Name=cleandata['Name'],Email_ID=cleandata['Email_ID'],Fax_No=cleandata['Fax_No'],Home_Phone_No=cleandata['Home_Phone_No'],Office_Phone_No=cleandata['Office_Phone_No'],	Designation=cleandata['Designation'],Address_Line=cleandata['Address_Line'],Order=cleandata['Order'],Date_Added="",Added_By=user,Department=cleandata['Department']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Employee Record Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addemployee/',"emp":True} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Employee's Data",'form':form,'action_url':'/addemployee/',"emp":True} );
		else:
			return HttpResponseRedirect('/accounts/login/');

#Add employee ends here

#Depatment info related to an employee begins here
def deptinfo(request,ssn):
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
		            		return render(request,'allpopupform.html',{'content_title':" Organization Added Successfully", 'success':True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addorganization/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Organization's Data",'form':form,'action_url':'/addorganization/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Organization form ends here

#organization all display begins here
def displayOrg(request):
				content=None;			
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Organization.objects.all();
				t= get_template("organization.html");
				content = t.render(Context({'details':qset,'user': request.user }));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Organization'})
			
			
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
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully','success':True})
				else:
					try:	
						ins=Organization.objects.get(ID__exact=ssn)
						form=OrganizationForm(instance=ins);	
					except Organization.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit organization','form':form,'action_url':'editOrg/%s'%(ssn)})




#edit organization ends here

#Organization history begins here
def org_history(request,ssn):
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
					obj=Department(Name=cleandata['Name'],Address=cleandata['Address'],Contact_No=cleandata['Contact_No'],Organization=cleandata['Organization']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':" Department Added Successfully",'success':True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/adddepartment/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Derpartment's Data",'form':form,'action_url':'/adddepartment/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add department form ends here


#Department all display begins here
def displayDept(request):
				content=None;	
			
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Department.objects.all();
				t= get_template("department.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Department'})
			
#Department all display ends here


# edit department begins here
def editDept(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Department.objects.get(ID__iexact=ssn);
				org=old.Organization;			
				if request.method=="POST":
					
					form=DepartmentForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Department.objects.get(ID=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						j.Name=cleandata['Name'];
						j.Address=cleandata['Address'];
						j.Contact_No=cleandata['Contact_No'];
						j.Organization=cleandata['Organization'];
						j.save();
						obj=Departmenthistory(Dept_ID=old.ID,Name=old.Name,Address=old.Address,Contact_No=old.Contact_No,Organization=org.ID,Modified_By=user,Modified_On="");
						obj.save();
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully','success':True})
				else:
					try:	
						ins=Department.objects.get(ID__exact=ssn)
						form=DepartmentForm(instance=ins);	
					except Department.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit organization','form':form,'action_url':'editDept/%s'%(ssn)})




#edit department ends here


#Department history begins here
def dept_history(request,ssn):
		query=Departmenthistory.objects.filter(Dept_ID__iexact=ssn);
		return render(request,"depthistory.html", {'details':query})

#Department history ends here


#Employee belonging to an Department begins here
def dept_employee(request,ssn):
	
		query=Department.objects.get(ID__iexact=ssn);
		deptqset=Department.objects.all();	
		empqset = query.employeeall_set.all();
		orgqset=Organization.objects.get(ID__iexact=query.Organization_id);
		l=[];
		for obj1 in empqset:
			l.append(obj1.SSNNO);
		proqset=Project.objects.filter(Officer_In_Charge_id__in=l);			
		l1=[];
		for obj2 in proqset:
			l1.append(obj2.Third_Party_id);
		thirdqset=ThirdParty.objects.filter(Reg_No__in=l1)
		l2=[];
		for obj3 in empqset:
			l2.append(obj3.Designation_id);
		degqset=Designation.objects.filter(Designation_No__in=l2)

		l3=[];
		l4=[];
		l5=[];
		l6=[];
		for obj4 in degqset:
			l3.append(obj4.Appointment_id)
			l4.append(obj4.Duration_id)
			l5.append(obj4.Powers_And_Duties_id)
			l6.append(obj4.Removal_id)
		appqset=Appointment.objects.filter(No__in=l3)
		durqset=Duration.objects.filter(No__in=l4)
		padqset=PowersAndDuties.objects.filter(No__in=l4)
		remqset=Removal.objects.filter(No__in=l6)				
		actqset=Act.objects.all();
    		chapqset=Chapter.objects.all();
    		secqset=Section.objects.all();
    
		return render_to_response('home3.html',{ 'user': request.user ,'home':True,'org_details':orgqset,'dept_detail':deptqset,'emp_detail':empqset,'pro_detail':proqset,"third_detail":thirdqset,
'act_detail':actqset,'chap_detail':chapqset,'sec_detail':secqset,'deg_detail':degqset,"app_detail":appqset,"dur_detail":durqset,"pad_detail":padqset,
'rem_detail':remqset})
			
		#return render(request,"deptemployee.html", {'details':qset })
	


#Employee belonging to an department ends here


#organization Infomation related to a department begins here
def orginfo(request,ssn):
	
		query=Organization.objects.get(ID__iexact=ssn);
		return render(request,"showorg.html", {'details':query})

#organization Infomation related to a department ends here



#Department belonging to an organization begins here
def org_dept(request,ssn):
	
		orgqset=Organization.objects.all();
		query=Organization.objects.get(ID__iexact=ssn);
		deptqset = query.department_set.all();
		li=[];
		l=[];
		for obj in deptqset: 
		
			li.append(obj.ID);
		empqset = Employeeall.objects.filter(Department_id__in=li);			
					
		for obj1 in empqset:
			l.append(obj1.SSNNO);
		proqset=Project.objects.filter(Officer_In_Charge_id__in=l);			
		l1=[];
		for obj2 in proqset:
			l1.append(obj2.Third_Party_id);
		thirdqset=ThirdParty.objects.filter(Reg_No__in=l1)
		l2=[];
		for obj3 in empqset:
			l2.append(obj3.Designation_id);
		degqset=Designation.objects.filter(Designation_No__in=l2)

		l3=[];
		l4=[];
		l5=[];
		l6=[];
		for obj4 in degqset:
			l3.append(obj4.Appointment_id)
			l4.append(obj4.Duration_id)
			l5.append(obj4.Powers_And_Duties_id)
			l6.append(obj4.Removal_id)
		appqset=Appointment.objects.filter(No__in=l3)
		durqset=Duration.objects.filter(No__in=l4)
		padqset=PowersAndDuties.objects.filter(No__in=l4)
		remqset=Removal.objects.filter(No__in=l6)				
		actqset=Act.objects.all();
    		chapqset=Chapter.objects.all();
    		secqset=Section.objects.all();
    
		return render_to_response('home3.html',{ 'user': request.user ,'home':True,'org_detail':orgqset,'dept_detail':deptqset,'emp_detail':empqset,'pro_detail':proqset,"third_detail":thirdqset,
'act_detail':actqset,'chap_detail':chapqset,'sec_detail':secqset,'deg_detail':degqset,"app_detail":appqset,"dur_detail":durqset,"pad_detail":padqset,
'rem_detail':remqset})
#'act_detail':actset,
#'chap_detail':chapset,'sec_detail':secset,"third_detail":thirdset,"app_detail":appset,"dur_detail":durset,"pad_detail":padset,
#'rem_detail':remset,'deg_detail':degset


		#data = serializers.serialize("json", qset)
    		#return HttpResponse(data, content_type='application/json')

#Department belonging to an organization ends here



#Employee belonging to an organization begins here
def org_employee(request,ssn):
		li=[];	
	
		query=Organization.objects.get(ID__iexact=ssn);
		q = query.department_set.all();
		for obj in q: 
		
			li.append(obj.ID);
		qset = Employeeall.objects.filter(Department_id__in=li);			
		return render(request,"deptemployee.html", {'details':qset })
	

#Employee belonging to an organization ends here

#Project belonging to an organization begins here
def org_project(request,ssn):
		li=[];
		l=[];	
	
		query=Organization.objects.get(ID__iexact=ssn);
		q = query.department_set.all();
		for obj in q: 
		
			li.append(obj.ID);
		qset = Employeeall.objects.filter(Department_id__in=li);
		for obj1 in qset:
			l.append(obj1.SSNNO);
		qset1=Project.objects.filter(Officer_In_Charge_id__in=l);			
		return render(request,"showproject.html", {'project':qset1 })
	


#Project belonging to an organization ends here


def display(request):
				content=None;	
			
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Employeeall.objects.all();
				t= get_template("employee.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Employee',"emp":True})
			
def search(request):
			content=None;	
		
		
			query=request.POST.get('q');
			qset=None
			content=None;
			if query:
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Employeeall.objects.filter(Q(SSNNO__iexact=query) |Q(Name__icontains=query));
				t= get_template("employee.html");
				content = t.render(Context({'details':qset}));
			
			return render(request,"home1.html", {'query':query,'contentsea':content,"search":True,"emp":True})
		

#Edit employee records begins here
def edit(request, ssn):
			 form=None
			 username = None
    			 if request.user.is_authenticated():
        			user = request.user.username
				now=datetime.datetime.now();
				old=Employeeall.objects.get(SSNNO__iexact=ssn);
				dept=old.Department;
				deg=old.Designation;	
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
						j.Department=cleandata['Department'];
						j.save();
						obj=Employeehistory(SSNNO=old.SSNNO,Department=dept.Name,	Title=old.Title,Name=old.Name,
Email_ID=old.Email_ID,Fax_No=old.Fax_No,Home_Phone_No=old.Home_Phone_No,Office_Phone_No=old.Office_Phone_No,
Designation=deg.Designation_Name,Address_Line=old.Address_Line,Added_By=old.Added_By,From=old.Date_Added,To="",Order=old.Order,
Comment=old.Comment);
						
						obj.save();
						return render(request,'allpopupform.html',{'content_title':'Employee Saved',"success":True})
				else:
					try:	
						ins=Employeeall.objects.get(SSNNO__exact=ssn)
						form=EditEmployeeForm(instance=ins);	
					except Employeeall.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Employee','form1':form,'action_url':'edit/%s'%(ssn), 'enctype':"multipart/form-data",'emp':True})
#Edit employee records ends here


def edithistory(request):
				content=None;	
			
				query=Employeehistory.objects.all();
				t=get_template("employeeedithistory.html");
				content=t.render(Context({'employee':query}));
				return render(request,"home1.html", {'history':content,'content_title':'History Of Modification','emp':True})



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
	
		query=Employeehistory.objects.filter(SSNNO__iexact=ssn);
		qset = Employeeall.objects.all();
		#t = get_template("employee.html");
		#t2=get_template("emphistory.html")
		#//content = t.render(Context({'details':qset}));
		#content2=t2.render(Context({'history':query}));	
		return render(request,"emphistory.html",{'history':query})
	

def emp(request,ssn):
	
		query=Employeehistory.objects.filter(SSNNO__iexact=ssn);
		return render(request,"emphistory.html", {'history':query})

def phonehis(request,ssn):
	
		query=Employeehistory.objects.filter(Office_Phone_No__iexact=ssn);
		return render(request,"phonehistory.html", {'history':query})

def designationhis(request,ssn):
	
		query=Employeehistory.objects.filter(Designation=ssn);
		return render(request,"designationhistory.html", {'history':query})

def empinfo(request,ssn):
	
		query=Employeeall.objects.get(SSNNO__iexact=ssn);
		return render(request,"showemployee.html", {'details':query})

def addproject(request):
		username = None;
		
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=ProjectFormAll();	
		
			if request.method=='POST': # If the form has been submitted...
				form=ProjectFormAll(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Project(Project_Name=cleandata['Project_Name'],Start_Date=cleandata['Start_Date'],End_Date=cleandata['End_Date'],Amt_Sanctioned=cleandata['Amt_Sanctioned'],Amt_Proposed=cleandata['Amt_Proposed'],Expenditure_Last_Year=cleandata['Expenditure_Last_Year'],No_of_Installment=cleandata['No_of_Installment'],Officer_In_Charge=cleandata['Officer_In_Charge'],Tender_Notice=cleandata['Tender_Notice'],Tender_Submitted=cleandata['Tender_Submitted'],Contract=cleandata['Contract'],Third_Party=cleandata['Third_Party'])
					obj.save();	
			            	return render(request,'allpopupform.html',{'content_title':"Project Record Added Successfully","success":True} );

				else:
					
			 	       	return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/addproject/','enctype':"multipart/form-data"} );
			
			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title': 'Enter the Project Detail','form1':form,'action_url':'/addproject/','enctype':"multipart/form-data"} );
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
				if old.Third_Party is not None:
					no1=old.Third_Party.Name;
				else:
					no1=None
				no2=old.Officer_In_Charge;			
				if request.method=="POST":
					
					form=ProjectForm(request.POST,request.FILES);
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
						j.Officer_In_Charge=cleandata['Officer_In_Charge'];
						j.Tender_Notice=cleandata['Tender_Notice'];
						j.Tender_Submitted=cleandata['Tender_Submitted'];
						j.Contract=cleandata['Contract'];
						j.Third_Party=cleandata['Third_Party']
						j.save();
						obj=Projecthistory(Project_ID=old.Project_ID,Project_Name=old.Project_Name,Start_Date=old.Start_Date,End_Date=old.End_Date,Amt_Sanctioned=old.Amt_Sanctioned,
Amt_Proposed=old.Amt_Proposed,Expenditure_Last_Year=old.Expenditure_Last_Year,No_of_Installment=old.No_of_Installment,Officer_In_Charge=no2.Name,Tender_Notice=old.Tender_Notice,
Tender_Submitted=old.Tender_Submitted,Contract=old.Contract,Third_Party=no1,Modified_By=user,Modified_On="");
						
						obj.save();
						return render(request,'allpopupform.html',{'content_title':'Project Saved','success':True})
				else:
					try:	
						ins=Project.objects.get(Project_ID__exact=ssn)
						form=ProjectForm(instance=ins);	
					except Project.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Project','form1':form,'action_url':'edit_project/%s'%(ssn),'enctype':"multipart/form-data"})
#Edit project records ends here



def showproject(request):
				content=None;	
			
				query=Project.objects.all();
				t=get_template("showproject.html");
				content=t.render(Context({'project':query,'user': request.user}));
				return render(request,"home1.html", {'history':content,'content_title':'All Project'})
			
#Invididual Project Begins here
def viewproject(request,id1):
		content=None;
	
		query=Project.objects.get(Project_ID__exact=id1);
		qu=query.comment_set.all();
		#t=get_template("viewproject.html");
		#content=t.render(Context({'person':query,'comment':qu}));
		return render(request,"viewproject.html",{'person':query,'comment':qu})
	
#Individual Project Ends here

#Invididual Project Begins here
def projectinfo(request,id1):
		content=None;
	
		query=Project.objects.get(Project_ID__exact=id1);
		thirdqset=ThirdParty.objects.filter(Reg_No__exact=query.Third_Party_id);
		empqset=Employeeall.objects.get(SSNNO__exact=query.Officer_In_Charge_id);
		deptqset=Department.objects.get(ID__exact=empqset.Department_id);
		orgqset=Organization.objects.get(ID__exact=deptqset.Organization_id);
		#t=get_template("viewproject.html");
		#content=t.render(Context({'person':query,'comment':qu}));
		#return render(request,"viewproject.html",{'person':query,'comment':qu})
		proqset=Project.objects.all();
		degqset=Designation.objects.filter(Designation_No=empqset.Designation_id)

		l3=[];
		l4=[];
		l5=[];
		l6=[];
		for obj4 in degqset:
			l3.append(obj4.Appointment_id)
			l4.append(obj4.Duration_id)
			l5.append(obj4.Powers_And_Duties_id)
			l6.append(obj4.Removal_id)
		appqset=Appointment.objects.filter(No__in=l3)
		durqset=Duration.objects.filter(No__in=l4)
		padqset=PowersAndDuties.objects.filter(No__in=l4)
		remqset=Removal.objects.filter(No__in=l6)				
		actqset=Act.objects.all();
    		chapqset=Chapter.objects.all();
    		secqset=Section.objects.all();
    
		return render_to_response('home3.html',{ 'user': request.user ,'home':True,'org_details':orgqset,'dept_details':deptqset,'emp_details':empqset,'pro_detail':proqset,"third_details":thirdqset,
'act_detail':actqset,'chap_detail':chapqset,'sec_detail':secqset,'deg_detail':degqset,"app_detail":appqset,"dur_detail":durqset,"pad_detail":padqset,
'rem_detail':remqset})
		
		
		
#Individual Project Ends here

#Project history begins here
def project_history(request,ssn):
	
		query=Projecthistory.objects.filter(Project_ID__iexact=ssn);
		return render(request,"projecthistory.html", {'project':query})

#Project history ends here


def empproject(request,ssn):
	
		#q=Employeeall.objects.raw('select distinct SSNNO,Name,Email_ID,Fax_No,Office_Phone_No,Home_Phone_No,Designation,Address_Line from employeeall_employeeall, employeeall_project where employeeall_employeeall.SSNNO=employeeall_project.Emp_SSNNO_id');

		query=Employeeall.objects.get(SSNNO__iexact=ssn);
		proqset = query.project_set.all();			
		deptqset=Department.objects.get(ID__iexact=query.Department_id);
		orgqset = Organization.objects.get(ID__iexact=deptqset.Organization_id);
		empqset = Employeeall.objects.all();						
		l1=[];
		for obj2 in proqset:
			l1.append(obj2.Third_Party_id);
		thirdqset=ThirdParty.objects.filter(Reg_No__in=l1)
		l2=[];
		
		degqset=Designation.objects.filter(Designation_No=query.Designation_id)

		l3=[];
		l4=[];
		l5=[];
		l6=[];
		for obj4 in degqset:
			l3.append(obj4.Appointment_id)
			l4.append(obj4.Duration_id)
			l5.append(obj4.Powers_And_Duties_id)
			l6.append(obj4.Removal_id)
		appqset=Appointment.objects.filter(No__in=l3)
		durqset=Duration.objects.filter(No__in=l4)
		padqset=PowersAndDuties.objects.filter(No__in=l4)
		remqset=Removal.objects.filter(No__in=l6)				
		actqset=Act.objects.all();
    		chapqset=Chapter.objects.all();
    		secqset=Section.objects.all();
    
		return render_to_response('home3.html',{ 'user': request.user ,'home':True,'org_details':orgqset,'dept_details':deptqset,'emp_detail':empqset,'pro_detail':proqset,"third_detail":thirdqset,
'act_detail':actqset,'chap_detail':chapqset,'sec_detail':secqset,'deg_detail':degqset,"app_detail":appqset,"dur_detail":durqset,"pad_detail":padqset,
'rem_detail':remqset})
		#return render(request,"emppro.html", {'project':qset })
	
def disemppro(request):
				content=None;	
			
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset=Employeeall.objects.raw('select distinct SSNNO,Name,Email_ID,Fax_No,Office_Phone_No,Home_Phone_No,Designation_id,Address_Line from employeeall_employeeall, employeeall_project where employeeall_employeeall.SSNNO=employeeall_project.Officer_In_Charge_id');				
				t= get_template("empproject.html");
				content = t.render(Context({'details':qset}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Employee'})


#File Open begins here

#def fileupload(request,name):
#	f=open(name);
#	content=f.read();
#	f.close();
#	return render(request,"file.html",{"content":content})

#File Open Ends here

def fileupload(request,name):
    with open(name, 'r') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=%s'%name
        return response
    pdf.closed
#File Open begins here

#def fileupload(request,name):
#	response = HttpResponse(content_type='application/pdf')
#    	response['Content-Disposition'] = 'attachment; filename=%s' %name
#	buffer = BytesIO()
#	p = canvas.Canvas(buffer)
#	p.drawString(100, 100, "Hello world.")
#	p.showPage()
 #  	p.save()
#	pdf = buffer.getvalue()
#
#  	response.write(pdf)
#    	return response
	

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
		            		return render(request,'allpopupform.html',{'content_title':" Comment Added","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addcomment/'});

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Add Comment",'form':form,'action_url':'/addcomment/'});
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
		            		return render(request,'allpopupform.html',{'content_title':" Act Added Successfully","success":True} );
		            		return render(request,'allpopupform.html',{'content_title':" Act Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addact/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Act's Data",'form':form,'action_url':'/addact/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');

#Add Act ends here

#Show all act begins here
def showallact(request):
				content=None;	
	
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Act.objects.all();
				t= get_template("act.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Act'})
	


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
					obj=Chapter(Chapter_No=cleandata['Chapter_No'],Name=cleandata['Name'],Text=cleandata['Text'],Act=cleandata['Act']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':" Chapter Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addchapter/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Chapter's Data",'form':form,'action_url':'/addchapter/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add chapter ends here

#Show all chapter begins here

def showallchapter(request):
				content=None;	
	
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Chapter.objects.all();
				t= get_template("chapter.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Chapter'})
	
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
					obj=Section(Section_No=cleandata['Section_No'],Name=cleandata['Name'],Text=cleandata['Text'],Chapter=cleandata['Chapter']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':" Section Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addsection/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Section's Data",'form':form,'action_url':'/addsection/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');



#Add section ends here

#Show all Section begins here
def showallsection(request):
				content=None;	
	
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Section.objects.all();
				t= get_template("section.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Section'})
	
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
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Act.objects.get(No__exact=ssn)
						form=ActEditForm(instance=ins);	
					except Act.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Act','form':form,'action_url':'editAct/%s'%(ssn)})



#Edit Act ends here


#Edit Chapter begins here
def editChapter(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Chapter.objects.get(Chapter_No__iexact=ssn);
				no=old.Act;	
				if request.method=="POST":
					
					form=ChapterEditForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Chapter.objects.get(Chapter_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Name=cleandata['Name'];
						j.Text=cleandata['Text'];
						j.Act_No=cleandata['Act'];
						j.save();
						obj=ChapterHistory(Chapter_No=old.Chapter_No,Name=old.Name,Text=old.Text,Act=no.No,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Chapter.objects.get(Chapter_No__exact=ssn)
						form=ChapterEditForm(instance=ins);	
					except Chapter.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Chapter','form':form,'action_url':'editChapter/%s'%(ssn)})
#Edit Chapter ends here


#Edit Section begins here
def editSection(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Section.objects.get(Section_No__iexact=ssn);
				no=old.Chapter;	
				if request.method=="POST":
					
					form=SectionEditForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Section.objects.get(Section_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Name=cleandata['Name'];
						j.Text=cleandata['Text'];
						j.Chapter=cleandata['Chapter'];
						j.save();
						obj=SectionHistory(Section_No=old.Section_No,Name=old.Name,Text=old.Text,Chapter=no.Chapter_No,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Section.objects.get(Section_No__exact=ssn)
						form=SectionEditForm(instance=ins);	
					except Section.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Section','form':form,'action_url':'editSection/%s'%(ssn)})
#Edit Section ends here

#Chapter belonging to an Act begins here
def act_chapter(request,ssn):

		
		query=Act.objects.get(No__iexact=ssn);
		chapqset=query.chapter_set.all();
		#t= get_template("act_chapter.html");
		#content = t.render(Context({'chap_detail':chapqset}));
			
		chapter = [model_to_dict(topic) for topic in chapqset];
		chapter_list=json.dumps({'chap_detail':chapter})
		l1=[];
		for obj in chapqset:
			l1.append(obj.Chapter_No)
		secqset	=Section.objects.filter(Chapter_id__in=l1)
		section=[model_to_dict(content) for content in secqset];
		section_list=json.dumps({'chap_detail':chapter,'sec_detail':section},ensure_ascii=False)
		#return render(request,"home3.html",{'chapter':True})
		return HttpResponse(section_list);

#Chapter belonging to an act ends here

#Section belonging to an Chapter begins here
def chapter_section(request,ssn):

		
		query=Chapter.objects.get(Chapter_No__iexact=ssn);
		qset = query.section_set.all();			
		return render(request,"section.html", {'details':qset })

#Section belonging to an chapter ends here

#Section belonging to an act ends here
def act_section(request,ssn):
		li=[];	
	
		query=Act.objects.get(No__iexact=ssn);
		q = query.chapter_set.all();
		for obj in q: 
		
			li.append(obj.Chapter_No);
		qset = Section.objects.filter(Chapter_id__in=li);			
		return render(request,"section.html", {'details':qset })
	
#Section belonging to an act ends here

#Show Act from chapter begins here
def showact(request,ssn):
	
		
		query=Act.objects.get(No__iexact=ssn);			
		return render(request,"showact.html", {'details':query })
	
#Show Act from chapter begins here

#Show chapter from section begins here
def showchapter(request,ssn):

		
		query=Chapter.objects.get(Chapter_No__iexact=ssn);			
		return render(request,"showchapter.html", {'details':query })

#Show Chapter from section begins here

#Show act history begins here
def acthistory(request,ssn):

		query=ActHistory.objects.filter(No__iexact=ssn);
		return render(request,"acthistory.html", {'details':query})


#shoe act history ends here

#Show chapter history begins here
def chapterhistory(request,ssn):

		query=ChapterHistory.objects.filter(Chapter_No__iexact=ssn);
		return render(request,"chapterhistory.html", {'details':query})


#show chapter history ends here

#Show section history begins here
def sectionhistory(request,ssn):

		query=SectionHistory.objects.filter(Section_No__iexact=ssn);
		return render(request,"sectionhistory.html", {'details':query})


#show section history ends here
#Add Appointment begins here
def addapp(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=AppointmentForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=AppointmentForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Appointment(Text=cleandata['Text'],Section=cleandata['Section'],Chapter=cleandata['Chapter'],Act=cleandata['Act'],Order=cleandata['Order']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Appointment Record Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/addapp/','enctype':"multipart/form-data"} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Data",'form1':form,'action_url':'/addapp/','enctype':"multipart/form-data"} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add Appointment ends here
#SHow Appointment Begins here
def show_all_app(request):
				content=None;	

		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Appointment.objects.all();
				t= get_template("appointment.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'Appointment Detail'})

#SHow Appointment Begins here

#Edit Appointment Begins  here
def edit_app(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Appointment.objects.get(No__iexact=ssn);
				no1=old.Section;
				no2=old.Chapter;
				no3=old.Act;			
				if request.method=="POST":
					
					form=AppointmentForm(request.POST,request.FILES);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Appointment.objects.get(No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Section=cleandata['Section'];
						j.Chapter=cleandata['Chapter'];
						j.Act=cleandata['Act'];
						j.Order=cleandata['Order'];
						j.save();
						obj=AppointmentHistory(No=old.No,Text=old.Text,Section=no1.Section_No,Chapter=no2.Chapter_No,Act=no3.No,Order=old.Order,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Appointment.objects.get(No__exact=ssn)
						form=AppointmentForm(instance=ins);	
					except Appointment.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Appointment','form1':form,'action_url':'editapp/%s'%(ssn),'enctype':"multipart/form-data"})

#Edit Appointment Ends Here

#Show appointment history begins here
def app_history(request,ssn):

		query=AppointmentHistory.objects.filter(No__iexact=ssn);
		return render(request,"apphistory.html", {'details':query})

#Show appointment history ends here
#Add Duration begins here
def add_dur(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=DurationForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=DurationForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Duration(Text=cleandata['Text'],Section=cleandata['Section'],Chapter=cleandata['Chapter'],Act=cleandata['Act'],Order=cleandata['Order']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Duration Record Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/adddur/','enctype':"multipart/form-data"} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Data",'form1':form,'action_url':'/adddur/','enctype':"multipart/form-data"} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add Duration ends here
#SHow Duration Begins here
def show_all_dur(request):
				content=None;	

		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Duration.objects.all();
				t= get_template("duration.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'Duration Detail'})

#SHow Duration ends here
#Edit Duration Begins  here
def edit_dur(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Duration.objects.get(No__iexact=ssn);
				no1=old.Section;
				no2=old.Chapter;
				no3=old.Act;			
				if request.method=="POST":
					
					form=DurationForm(request.POST,request.FILES);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Duration.objects.get(No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Section=cleandata['Section'];
						j.Chapter=cleandata['Chapter'];
						j.Act=cleandata['Act'];
						j.Order=cleandata['Order'];
						j.save();
						obj=DurationHistory(No=old.No,Text=old.Text,Section=no1.Section_No,Chapter=no2.Chapter_No,Act=no3.No,Order=old.Order,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Duration.objects.get(No__exact=ssn)
						form=DurationForm(instance=ins);	
					except Duration.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Duration','form1':form,'action_url':'editdur/%s'%(ssn),'enctype':"multipart/form-data"})

#Edit Dur Ends Here
#Show duration history begins here
def dur_history(request,ssn):

		query=DurationHistory.objects.filter(No__iexact=ssn);
		return render(request,"apphistory.html", {'details':query})
#Show duration history begins here
#Add Powers begins here
def add_pad(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=PowersAndDutiesForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=PowersAndDutiesForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=PowersAndDuties(Text=cleandata['Text'],Section=cleandata['Section'],Chapter=cleandata['Chapter'],Act=cleandata['Act'],Order=cleandata['Order']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Powers Record Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/addpad/','enctype':"multipart/form-data"} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Data",'form1':form,'action_url':'/addpad/','enctype':"multipart/form-data"} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add Powers ends here
#SHow PAD Begins here
def show_all_pad(request):
				content=None;	

		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = PowersAndDuties.objects.all();
				t= get_template("power.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'Powers Detail'})

#SHow PAD ends here
#Edit PAD Begins  here
def edit_pad(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=PowersAndDuties.objects.get(No__iexact=ssn);
				no1=old.Section;
				no2=old.Chapter;
				no3=old.Act;			
				if request.method=="POST":
					
					form=PowersAndDutiesForm(request.POST,request.FILES);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = PowersAndDuties.objects.get(No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Section=cleandata['Section'];
						j.Chapter=cleandata['Chapter'];
						j.Act=cleandata['Act'];
						j.Order=cleandata['Order'];
						j.save();
						obj=PowersAndDutiesHistory(No=old.No,Text=old.Text,Section=no1.Section_No,Chapter=no2.Chapter_No,Act=no3.No,Order=old.Order,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=PowersAndDuties.objects.get(No__exact=ssn)
						form=PowersAndDutiesForm(instance=ins);	
					except PowersAndDuties.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Powers and duties ','form1':form,'action_url':'editpad/%s'%(ssn),'enctype':"multipart/form-data"})

#Edit PAD Ends Here


#Show PAD history begins here
def pad_history(request,ssn):

		query=PowersAndDutiesHistory.objects.filter(No__iexact=ssn);
		return render(request,"apphistory.html", {'details':query})
#Show PAD history begins here

#Add Removal begins here
def add_rem(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=RemovalForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=RemovalForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Removal(Text=cleandata['Text'],Section=cleandata['Section'],Chapter=cleandata['Chapter'],Act=cleandata['Act'],Order=cleandata['Order']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Removal Record Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/addrem/','enctype':"multipart/form-data"} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Data",'form1':form,'action_url':'/addrem/','enctype':"multipart/form-data"} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add Removal ends here
#SHow Removal Begins here
def show_all_rem(request):
				content=None;	

		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Removal.objects.all();
				t= get_template("removal.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'Removal Detail'})

#SHow Removal ends here
#Edit Removal Begins  here
def edit_rem(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Removal.objects.get(No__iexact=ssn);
				no1=old.Section;
				no2=old.Chapter;
				no3=old.Act;			
				if request.method=="POST":
					
					form=RemovalForm(request.POST,request.FILES);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Removal.objects.get(No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Text=cleandata['Text'];
						j.Section=cleandata['Section'];
						j.Chapter=cleandata['Chapter'];
						j.Act=cleandata['Act'];
						j.Order=cleandata['Order'];
						j.save();
						obj=RemovalHistory(No=old.No,Text=old.Text,Section=no1.Section_No,Chapter=no2.Chapter_No,Act=no3.No,Order=old.Order,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Removal.objects.get(No__exact=ssn)
						form=RemovalForm(instance=ins);	
					except Removal.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Removal ','form1':form,'action_url':'editrem/%s'%(ssn),'enctype':"multipart/form-data"})

#Edit Removal Ends Here

#Show Removal history begins here
def rem_history(request,ssn):

		query=RemovalHistory.objects.filter(No__iexact=ssn);
		return render(request,"apphistory.html", {'details':query})
#Show Removal history begins here

#Add Designation begins here
def add_deg(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username
			now=datetime.datetime.now();
			form=DesignationForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=DesignationForm(request.POST,request.FILES); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=Designation(Designation_Name=cleandata['Designation_Name'],Appointment=cleandata['Appointment'],Duration=cleandata['Duration'],Powers_And_Duties=cleandata['Powers_And_Duties'],Removal=cleandata['Removal'],Order=cleandata['Order']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':"Designation Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form1':form,'action_url':'/add_desig/','enctype':"multipart/form-data"} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter Data",'form1':form,'action_url':'/add_desig/','enctype':"multipart/form-data"} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Add Designation ends here
#SHow Designation Begins here
def show_all_desig(request):
				content=None;	

		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = Designation.objects.all();
				t= get_template("designation.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'Designation Detail'})

#SHow Designation ends here
#Edit Designation Begins  here
def edit_desig(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=Designation.objects.get(Designation_No__iexact=ssn);
				no1=old.Appointment;
				no2=old.Duration;
				no3=old.Powers_And_Duties;
				no4=old.Removal;	
				if request.method=="POST":
					
					form=DesignationForm(request.POST,request.FILES);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = Designation.objects.get(Designation_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						#j.No=cleandata['No'];
						j.Designation_Name=cleandata['Designation_Name'];
						j.Appointment=cleandata['Appointment'];
						j.Duration=cleandata['Duration'];
						j.Powers_And_Duties=cleandata['Powers_And_Duties'];
						j.Removal=cleandata['Removal'];
						j.Order=cleandata['Order'];
						j.save();
						obj=DesignationHistory(Designation_No=old.Designation_No,Designation_Name=old.Designation_Name,Appointment=no1.No,Duration=no2.No,Powers_And_Duties=no3.No,Removal=no4.No,Order=old.Order,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=Designation.objects.get(Designation_No__exact=ssn)
						form=DesignationForm(instance=ins);	
					except Designation.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Designation ','form1':form,'action_url':'editdesig/%s'%(ssn),'enctype':"multipart/form-data"})

#Edit Designation Ends Here
#Show Designation history begins here
def desig_history(request,ssn):
	
		query=DesignationHistory.objects.filter(Designation_No__iexact=ssn);
		return render(request,"desighistory.html", {'details':query})
#Show Designation history begins here
#Add Organization form begins here
#Show Designation history begins here

def add_third(request):
		username = None;
		form=None;
    		if request.user.is_authenticated():
        		user = request.user.username;
			form=ThirdPartyForm();	
		
			if request.method=='POST': # If the form has been submitted...
				form=ThirdPartyForm(request.POST); # A form bound to the POST data
		
				if form.is_valid(): # All validation rules pass
					cleandata=form.cleaned_data;
					obj=ThirdParty(Reg_No=cleandata['Reg_No'],Name=cleandata['Name'],Address=cleandata['Address'],Established_Year=cleandata['Established_Year'],Kind_Of_Company=cleandata['Kind_Of_Company'],Director_Name=cleandata['Director_Name'],Din_No=cleandata['Din_No']);
					obj.save();	
		            		return render(request,'allpopupform.html',{'content_title':" Third Party Added Successfully","success":True} );
				else:
					
		 	       		return render(request,'allpopupform.html',{'content_title':"Invalid or Insufficient data Try again",'form':form,'action_url':'/addthirdparty/'} );

			else:
					
		 	       	return render(request,'allpopupform.html',{'content_title':"Enter ThirdParty's Data",'form':form,'action_url':'/addthirdparty/'} );
		else:
			return HttpResponseRedirect('/accounts/login/');


#Organization form ends here
#Third party all display begins here
def show_third(request):
				content=None;	
	
		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
				qset = ThirdParty.objects.all();
				t= get_template("thirdparty.html");
				content = t.render(Context({'details':qset,'user': request.user}));
			
				return render(request,"home1.html", {'empcontent':content,'content_title':'All Third Party'})
	
#Third Party all display ends here

# edit thirdparty begins here
def edit_party(request, ssn):
			 form=None;
    			 if request.user.is_authenticated():
				user = request.user.username
				now=datetime.datetime.now();
				old=ThirdParty.objects.get(Reg_No__iexact=ssn);	
				if request.method=="POST":
					
					form=EditThirdPartyForm(request.POST);
					if form.is_valid():
						cleandata=form.cleaned_data;
						j = ThirdParty.objects.get(Reg_No=ssn);
						#j.EmpID=request.POST['EmpID'];
											
						j.Name=cleandata['Name'];
						j.Address=cleandata['Address'];
						j.Established_Year=cleandata['Established_Year'];
						j.Kind_Of_Company=cleandata['Kind_Of_Company'];
						j.Director_Name=cleandata['Director_Name'];
						j.Din_No=cleandata['Din_No'];
						j.save();
						obj=ThirdPartyHistory(Reg_No=old.Reg_No,Name=old.Name,Address=old.Address,Established_Year=old.Established_Year,Kind_Of_Company=old.Kind_Of_Company,Director_Name=old.Director_Name,Din_No=old.Din_No,Modified_By=user,Modified_On="");
						obj.save();	
						return render(request,'allpopupform.html',{'content_title':'Updated Successfully',"success":True})
				else:
					try:	
						ins=ThirdParty.objects.get(Reg_No__exact=ssn)
						form=EditThirdPartyForm(instance=ins);	
					except ThirdParty.DoesNotExist:
						ins=None;
					
				return render(request,'allpopupform.html',{'content_title':'Edit Third Party','form':form,'action_url':'editparty/%s'%(ssn)})




#edit Thirdparty ends here

#Show third party history begins here
def party_history(request,ssn):
	
		query=ThirdPartyHistory.objects.filter(Reg_No__iexact=ssn);
		return render(request,"partyhistory.html", {'details':query})
#Show Third Party history begins here
#Show appointment information of an designation begins here
def desig_app(request,ssn):

		query=Appointment.objects.get(No__iexact=ssn);
		return render(request,"desig_app.html", {'details':query})

#Show appointment information of an designation ends here

#Show duration information of an designation begins here
def desig_dur(request,ssn):

		query=Duration.objects.get(No__iexact=ssn);
		return render(request,"desig_app.html", {'details':query})

#Show duration information of an designation ends here
#Show pad information of an designation begins here
def desig_pad(request,ssn):
	#if request.user.is_authenticated():
		query=PowersAndDuties.objects.get(No__iexact=ssn);
		return render(request,"desig_app.html", {'details':query})

#Show pad information of an designation ends here
#Show rem information of an designation begins here
def desig_rem(request,ssn):
	#if request.user.is_authenticated():
		query=Removal.objects.get(No__iexact=ssn);
		return render(request,"desig_app.html", {'details':query})

#Show removal information of an designation ends here
#Show act of an appointment begins here
def app_act(request,ssn):
	#if request.user.is_authenticated():
		query=Act.objects.get(No__iexact=ssn);
		return render(request,"appact.html", {'details':query})

#Show  act of an appointment ends here
#Show chapter of an appointment begins here
def app_chapter(request,ssn):
	#if request.user.is_authenticated():
		query=Chapter.objects.get(Chapter_No__iexact=ssn);
		return render(request,"appchapter.html", {'details':query})

#Show  chapter of an appointment ends here
#Show chapter of an appointment begins here
def app_section(request,ssn):
	#if request.user.is_authenticated():
		query=Section.objects.get(Section_No__iexact=ssn);
		return render(request,"appsection.html", {'details':query})

#Show  chapter of an appointment ends here

#Show third party of an project begins here
def project_party(request,ssn):
	#if request.user.is_authenticated():
		query=ThirdParty.objects.get(Reg_No__iexact=ssn);
		return render(request,"projectparty.html", {'details':query})

#Show third party of an project ends here

#Like google search for the home page begins here

@csrf_exempt
def allsearch(request):
			content=None;
			content1=None;
			content2=None;	
			filter=Q()	
			q1=Q()
			q2=Q()
			q3=Q()
			q4=Q()
			query=request.POST.get('q');
			qset=None
			qset1=None
			qset2=None
			qset3=None
			content=None;
			if query:
				if query.find(":") >1:
					str1=query.split(":")
					a,b=str1;
					c=b.split(" ")
					l1=[]
					l2=[]
					filter=Q()
					for i in c:
						if i.isdigit():
							l1.append(i)
						else:
							l2.append(i)			
					str1 = ' '.join(l2)
		
					if a.lower()=='employee':
						q=Q()
						#filter=Q()
						for t in c:
							#filter=filter|Q(Address_Line__icontains=t)		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
							q|= Q(SSNNO__iexact=t) |Q(Name__icontains=t)|Q(Address_Line__icontains=t)|Q(Email_ID__icontains=t)						
						qset = Employeeall.objects.filter(q);
						t= get_template("employee.html");
						c = RequestContext(request, {'details': qset})
						content = t.render(c);
				
					if a.lower()=='project':
						q = Q()
						
						#c=b.split(" ")
						#l1=[]
						#l2=[]
						#for i in c:
						#	if i.isdigit():
						#		l1.append(i)
						#	else:
						#		l2.append(i)			
						#str1 = ''.join(l2)
					#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
						for t1 in l1:
							if len(t1)==4:
								filter|=Q(Start_Date__year=t1)
							else:
								filter|=Q()
						
						for t in c:
									
							q |= Q(Project_Name__iexact=t) |Q(Amt_Proposed__iexact=t)| Q(filter);
						
						qset=Project.objects.filter(q)						
						t= get_template("showproject.html");
						c = RequestContext(request, {'project': qset})
						content = t.render(c);
			
					if a.lower()=='act':
						q=Q()
						for t in c:
							q|=Q(Year__iexact=t) |Q(Name__iexact=t)
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
						qset = Act.objects.filter(q);
						t= get_template("act.html");
						c = RequestContext(request, {'details': qset})
						content = t.render(c);

					if a.lower()=='chapter':
						q=Q()
						for t in c:
							q|=Q(Chapter_No__iexact=t) |Q(Text__icontains=t)
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
						qset = Chapter.objects.filter(q);
						t= get_template("chapter.html");
						c = RequestContext(request, {'details': qset})
						content = t.render(c);

					if a.lower()=='section':
					
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
						qset = Section.objects.filter(Q(Section_No__in=l1) | Q(Text__icontains=str1));
						t= get_template("section.html");
						c = RequestContext(request, {'details': qset})
						content = t.render(c);

					if a.lower()=='organization':
						q=Q()
						for t in c:
							q|=(Q(Contact_No__iexact=t) | Q(Name__icontains=t)|Q(Address__icontains=t))
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
						qset = Organization.objects.filter(q);
						t= get_template("organization.html");
						c = RequestContext(request, {'details': qset})
						content = t.render(c);

					if a.lower()=='thirdparty':
						q=Q()
						
						for t in c:
							q|=(Q(Reg_No__iexact=t) | Q(Name__icontains=t) | Q(Address__icontains=t) | Q(Established_Year__iexact=t))
						qset = ThirdParty.objects.filter(q);
						t= get_template("thirdparty.html");
						c = Context({'details': qset})
						content = t.render(c);
				else:
					name=query.split(" ")
					for n in name:
						if n.lower()=="organization": 
							for n in name:
								q1|=Q(Contact_No__iexact=n) | Q(Name__icontains=n)|Q(Address__icontains=n)
								qset=Organization.objects.filter(q1)

						if n.lower()=="employee":
							for n in name:
								q2|= Q(SSNNO__iexact=n) |Q(Name__icontains=n)|Q(Address_Line__icontains=n)|Q(Email_ID__icontains=n)		
							
								qset1 = Employeeall.objects.filter(q2);
						

						if n.lower()=="project":
							for n in name:						
								if n.isdigit() and len(n)==4:
									filter|=Q(Start_Date__year=n)
								else:
									filter|=Q()		
							for n in name:
								q3 |= Q(Project_Name__icontains=n) |Q(Amt_Proposed__iexact=n)| Q(filter);
								qset2=Project.objects.filter(q3);

						
						if n.lower()=="thirdparty":
							for n in name:
								q4|=(Q(Reg_No__iexact=n) | Q(Name__iexact=n) | Q(Address__icontains=n) | Q(Established_Year__iexact=n))
								qset3=ThirdParty.objects.filter(q4);

						t= get_template("allpage.html");
						c1 = Context({'details': qset,'empl':qset1,'pro':qset2,'third':qset3})
						content=t.render(c1);							
							
						
						#filter=Q()
							
							#filter=filter|Q(Address_Line__icontains=t)		
				#qset = (Q(SSNNO__iexact=query) |Q(EmpID__iexact=query) |Q(Name__iexact=query))
												
							
							
							
		
			return render(request,"home1.html", {'query':query,'contentsea':content,'contentemp':content2,'allsearch':True,"emp":True})
		
#Like google search for the home page begins here
