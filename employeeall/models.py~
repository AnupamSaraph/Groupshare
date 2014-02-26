from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Organization(models.Model):
	ID=models.AutoField(primary_key=True);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Mission=models.TextField(blank=False);
	Web_Url=models.URLField(max_length=200);
	def __unicode__(self):
		return  '%d' % ( self.ID )

class OrganizationForm(ModelForm):
 class Meta:
	model=Organization
	fields=['Name','Address','Contact_No','Mission','Web_Url']


class Organizationhistory(models.Model):
	Org_ID=models.IntegerField(max_length=6);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Mission=models.TextField(blank=False);
	Web_Url=models.URLField(max_length=200);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);

	def __unicode__(self):
		return  '%d' % ( self.ID )


class Department(models.Model):
	ID=models.AutoField(primary_key=True);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Organization_ID=models.ForeignKey('Organization');
	def __unicode__(self):
		return  '%d' % ( self.ID )

class DepartmentForm(ModelForm):
 class Meta:
	model=Department
	fields=['Name','Address','Contact_No','Organization_ID']


class Departmenthistory(models.Model):
	Dept_ID=models.IntegerField(max_length=6);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return  '%d' % ( self.ID )



class Employeeall(models.Model):
	SSNNO=  models.IntegerField(primary_key=True,max_length=6);
	Title = models.CharField(max_length=3, choices=TITLE_CHOICES);    
	Name = models.CharField(max_length=100);
	Email_ID = models. EmailField(max_length=254);
	Fax_No=  models.IntegerField(max_length=6);    
	Home_Phone_No = models.CharField(max_length=100);
	Office_Phone_No = models.CharField(max_length=100);
	Designation=models.CharField(max_length=200,blank=False);
	Address_Line =models.TextField(blank=False);
	Order=models.FileField(upload_to='media/files/',blank=True);
        Date_Added=models.DateField(auto_now=True,editable=True,blank=True);
	Added_By=models.CharField(max_length=100);
	Comment=models.TextField(blank=True);
	Dep_ID=models.ForeignKey('Department');
	def __unicode__(self):
		return  '%d' % ( self.SSNNO )

class EmployeeForm(ModelForm):
 class Meta:
	model=Employeeall
	fields=['SSNNO','Title','Name','Email_ID','Fax_No','Home_Phone_No','Office_Phone_No','Designation','Address_Line','Order','Dep_ID']

class EditEmployeeForm(ModelForm):
 class Meta:
	model=Employeeall
	fields=['Title','Name','Email_ID','Fax_No','Home_Phone_No','Office_Phone_No','Designation','Address_Line','Order','Comment','Dep_ID']




class Employeehistory(models.Model):
	SSNNO=  models.IntegerField(max_length=6);
	Dep_ID=models.IntegerField(max_length=6);
	Title = models.CharField(max_length=3, choices=TITLE_CHOICES);    
	Name = models.CharField(max_length=100);
	Email_ID = models. EmailField(max_length=254);
	Fax_No=  models.IntegerField(max_length=6);    
	Home_Phone_No = models.CharField(max_length=100);
	Office_Phone_No = models.CharField(max_length=100);
	Designation=models.CharField(max_length=200,blank=False);
	Address_Line =models.TextField(blank=False);
        From=models.DateField(auto_now=False,editable=True,blank=True);
	To=models.DateField(auto_now=True,editable=True,blank=True);	
	Added_By=models.CharField(max_length=100);
	Order=models.FileField(upload_to='employee',blank=True);
	Comment=models.TextField(blank=True);
	def __unicode__(self):	
		return str(self.SSNNO)

class Project(models.Model):
	Project_ID=models.IntegerField(primary_key=True,max_length=6);
	Project_Name=models.CharField(max_length=100);
	Start_Date=models.DateField(editable=True);
	End_Date=models.DateField(editable=True);
	Amt_Proposed=models.DecimalField(max_digits=13, decimal_places=3);
	Amt_Sanctioned=models.DecimalField(max_digits=13, decimal_places=3);
	Expenditure_Last_Year=models.DecimalField(max_digits=13, decimal_places=3);
	No_of_Installment=models.IntegerField(max_length=6);
	Emp_SSNNO=models.ForeignKey('Employeeall');
	def __unicode__(self):	
		return '%d' %(self.Project_ID)


class ProjectForm(ModelForm):
	class Meta:
		model=Project
		fields=['Project_Name','Start_Date','End_Date','Amt_Proposed','Amt_Sanctioned','Expenditure_Last_Year','No_of_Installment','Emp_SSNNO']


class ProjectFormAll(ModelForm):
	class Meta:
		model=Project
		fields=['Project_ID','Project_Name','Start_Date','End_Date','Amt_Proposed','Amt_Sanctioned','Expenditure_Last_Year','No_of_Installment','Emp_SSNNO']


class Projecthistory(models.Model):
	Project_ID=models.IntegerField(max_length=6);
	Project_Name=models.CharField(max_length=100);
	Start_Date=models.DateField(editable=True);
	End_Date=models.DateField(editable=True);
	Amt_Proposed=models.DecimalField(max_digits=13, decimal_places=3);
	Amt_Sanctioned=models.DecimalField(max_digits=13, decimal_places=3);
	Expenditure_Last_Year=models.DecimalField(max_digits=13, decimal_places=3);
	No_of_Installment=models.IntegerField(max_length=6);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):	
		return '%d' %(self.Project_ID)

