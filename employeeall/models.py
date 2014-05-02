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
	Order=models.FileField(upload_to='.',blank=True);
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
	Order=models.FileField(upload_to='.',blank=False);
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


class Comment(models.Model):		
	name = models.CharField(max_length=42)
	website = models.URLField(max_length=200, null=True, blank=True)
	text = models.TextField()
	project = models.ForeignKey(Project)
	created_on = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.text

class CommentForm(ModelForm):
	class Meta:
		model=Comment
		fields=['name','website','text','project']


class Act(models.Model):
	No=models.IntegerField(primary_key=True,max_length=6);
	Name=models.CharField(max_length=100);
	Year=models.IntegerField(max_length=4);
	Link=models.URLField(max_length=200, null=True, blank=True);
	def __unicode__(self):	
		return str(self.No)

class ActForm(ModelForm):
	class Meta:
		model=Act
		fields=['No','Name','Year','Link']

class ActEditForm(ModelForm):
	class Meta:
		model=Act
		fields=['Name','Year','Link']

class Chapter(models.Model):
	Chapter_No=models.IntegerField(primary_key=True,max_length=4);
	Text=models.TextField(blank=False);
	Act_No=models.ForeignKey(Act);
	def __unicode__(self):
		return str(self.Chapter_No);

class ChapterForm(ModelForm):
	class Meta:
		model=Chapter
		fields=['Chapter_No','Text','Act_No']

class ChapterEditForm(ModelForm):
	class Meta:
		model=Chapter
		fields=['Text','Act_No']

class Section(models.Model):
	Section_No=models.IntegerField(primary_key=True,max_length=4);
	Text=models.TextField(blank=False);
	Chapter_No=models.ForeignKey(Chapter);
	def __unicode__(self):
		return str(self.Section_No);

class SectionForm(ModelForm):
	class Meta:
		model=Section
		fields=['Section_No','Text','Chapter_No']

class SectionEditForm(ModelForm):
	class Meta:
		model=Section
		fields=['Text','Chapter_No']

			
class ActHistory(models.Model):
	No=models.IntegerField(max_length=6);
	Name=models.CharField(max_length=100);
	Year=models.IntegerField(max_length=4);
	Link=models.URLField(max_length=200, null=True, blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):	
		return str(self.No)

class ChapterHistory(models.Model):
	Chapter_No=models.IntegerField(max_length=4);
	Text=models.TextField(blank=False);
	Act_No=models.IntegerField(max_length=6);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return str(self.Chapter_No);

class SectionHistory(models.Model):
	Section_No=models.IntegerField(max_length=4);
	Text=models.TextField(blank=False);
	Chapter_No=models.IntegerField(max_length=4);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return str(self.Section_No);


