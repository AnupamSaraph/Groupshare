from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)

class Act(models.Model):
	No=models.IntegerField(primary_key=True,max_length=6);
	Name=models.CharField(max_length=100);
	Year=models.IntegerField(max_length=4);
	Link=models.URLField(max_length=200, null=True, blank=True);
	def __unicode__(self):	
		return '%s' %(self.Name)

class ActForm(ModelForm):
	class Meta:
		model=Act
		fields=['No','Name','Year','Link']

class ActEditForm(ModelForm):
	class Meta:
		model=Act
		fields=['Name','Year','Link']

class Chapter(models.Model):
	Chapter_No=models.IntegerField(primary_key=True,max_length=6);
	Name=models.CharField(max_length=100);
	Text=models.TextField(blank=False);
	Act=models.ForeignKey('Act');
	def __unicode__(self):
		return  '%s' %(self.Name);

class ChapterForm(ModelForm):
	class Meta:
		model=Chapter
		fields=['Chapter_No','Name','Text','Act']

class ChapterEditForm(ModelForm):
	class Meta:
		model=Chapter
		fields=['Name','Text','Act']

class Section(models.Model):
	Section_No=models.IntegerField(primary_key=True,max_length=6);
	Name=models.CharField(max_length=100);
	Text=models.TextField(blank=False);
	Chapter=models.ForeignKey('Chapter');
	def __unicode__(self):
		return  '%s' %(self.Name);

class SectionForm(ModelForm):
	class Meta:
		model=Section
		fields=['Section_No','Name','Text','Chapter']

class SectionEditForm(ModelForm):
	class Meta:
		model=Section
		fields=['Name','Text','Chapter']

			
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
	Chapter_No=models.IntegerField(max_length=6);
	Name=models.CharField(max_length=100);
	Text=models.TextField(blank=False);
	Act=models.IntegerField(max_length=6);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return str(self.Chapter_No);

class SectionHistory(models.Model):
	Section_No=models.IntegerField(max_length=6);
	Name=models.CharField(max_length=100);	
	Text=models.TextField(blank=False);
	Chapter=models.IntegerField(max_length=6);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return str(self.Section_No);

class Appointment(models.Model):
	No=models.AutoField(primary_key=True);
	Text=models.TextField(blank=False);
	Section=models.ForeignKey('Section');
	Chapter=models.ForeignKey('Chapter');
	Act=models.ForeignKey('Act');
	Order=models.FileField(upload_to='./media/files/',blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class AppointmentForm(ModelForm):
	class Meta:
		model=Appointment
		fields=['Text','Section','Chapter','Act','Order']


class AppointmentHistory(models.Model):
	No=models.IntegerField(max_length=20);
	Text=models.TextField(blank=False);
	Section=models.IntegerField(max_length=20);
	Chapter=models.IntegerField(max_length=20);
	Act=models.IntegerField(max_length=20);
	Order=models.FileField(upload_to='./media/files/',blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);


class Duration(models.Model):
	No=models.AutoField(primary_key=True);
	Text=models.TextField(blank=False);
	Section=models.ForeignKey('Section');
	Chapter=models.ForeignKey('Chapter');
	Act=models.ForeignKey('Act');
	Order=models.FileField(upload_to='./media/files/',blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class DurationForm(ModelForm):
	class Meta:
		model=Duration
		fields=['Text','Section','Chapter','Act','Order']


class DurationHistory(models.Model):
	No=models.IntegerField(max_length=20);
	Text=models.TextField(blank=False);
	Section=models.IntegerField(max_length=20);
	Chapter=models.IntegerField(max_length=20);
	Act=models.IntegerField(max_length=20);
	Order=models.FileField(upload_to='./media/files/',blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class PowersAndDuties(models.Model):
	No=models.AutoField(primary_key=True);
	Text=models.TextField(blank=False);
	Section=models.ForeignKey('Section');
	Chapter=models.ForeignKey('Chapter');
	Act=models.ForeignKey('Act');
	Order=models.FileField(upload_to='./media/files/',blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class PowersAndDutiesForm(ModelForm):
	class Meta:
		model=PowersAndDuties
		fields=['Text','Section','Chapter','Act','Order']


class PowersAndDutiesHistory(models.Model):
	No=models.IntegerField(max_length=20);
	Text=models.TextField(blank=False);
	Section=models.IntegerField(max_length=20);
	Chapter=models.IntegerField(max_length=20);
	Act=models.IntegerField(max_length=20);
	Order=models.FileField(upload_to='./media/files/',blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class Removal(models.Model):
	No=models.AutoField(primary_key=True);
	Text=models.TextField(blank=False);
	Section=models.ForeignKey('Section');
	Chapter=models.ForeignKey('Chapter');
	Act=models.ForeignKey('Act');
	Order=models.FileField(upload_to='./media/files/',blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);

class RemovalForm(ModelForm):
	class Meta:
		model=Removal
		fields=['Text','Section','Chapter','Act','Order']


class RemovalHistory(models.Model):
	No=models.IntegerField(max_length=20);
	Text=models.TextField(blank=False);
	Section=models.IntegerField(max_length=20);
	Chapter=models.IntegerField(max_length=20);
	Act=models.IntegerField(max_length=20);
	Order=models.FileField(upload_to='./media/files/',blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return '%s' %(self.Text);
	

class Designation(models.Model):
	Designation_No=models.AutoField(primary_key=True);
	Designation_Name=models.CharField(max_length=100);	
	Appointment=models.ForeignKey('Appointment');
	Duration=models.ForeignKey('Duration');
	Powers_And_Duties=models.ForeignKey('PowersAndDuties');
	Removal=models.ForeignKey('Removal');
	Order=models.FileField(upload_to='./media/files/',blank=True);
	def __unicode__(self):
		return '%s' %(self.Designation_Name);

class DesignationForm(ModelForm):
	class Meta:
		model=Designation
		fields=['Designation_Name','Appointment','Duration','Powers_And_Duties','Removal','Order']


class DesignationHistory(models.Model):
	Designation_No=models.IntegerField(max_length=20);
	Designation_Name=models.CharField(max_length=100);	
	Appointment=models.IntegerField(max_length=20);
	Duration=models.IntegerField(max_length=20);
	Powers_And_Duties=models.IntegerField(max_length=20);
	Removal=models.IntegerField(max_length=20);
	Order=models.FileField(upload_to='./media/files/',blank=True);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return '%s' %(self.Designation_Name);



class Organization(models.Model):
	ID=models.AutoField(primary_key=True);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Mission=models.TextField(blank=False);
	Web_Url=models.URLField(max_length=200);
	def __unicode__(self):
		return  '%s' % ( self.Name )

class OrganizationForm(ModelForm):
 class Meta:
	model=Organization
	fields=['Name','Address','Contact_No','Mission','Web_Url']


class Organizationhistory(models.Model):
	Org_ID=models.IntegerField(max_length=20);
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
	Organization=models.ForeignKey('Organization');
	def __unicode__(self):
		return  '%s' % ( self.Name )

class DepartmentForm(ModelForm):
 class Meta:
	model=Department
	fields=['Name','Address','Contact_No','Organization']


class Departmenthistory(models.Model):
	Dept_ID=models.IntegerField(max_length=20);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Contact_No=models.CharField(max_length=15);
	Organization=models.IntegerField(max_length=20);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);
	def __unicode__(self):
		return  '%d' % ( self.ID )



class Employeeall(models.Model):
	SSNNO=  models.IntegerField(primary_key=True,max_length=20);
	Title = models.CharField(max_length=3, choices=TITLE_CHOICES);    
	Name = models.CharField(max_length=100);
	Email_ID = models. EmailField(max_length=254);
	Fax_No=  models.IntegerField(max_length=15);    
	Home_Phone_No = models.CharField(max_length=100);
	Office_Phone_No = models.CharField(max_length=100);
	Designation=models.ForeignKey('Designation');
	Address_Line =models.TextField(blank=False);
	Order=models.FileField(upload_to='./media/files/',blank=True);
        Date_Added=models.DateField(auto_now=True,editable=True,blank=True);
	Added_By=models.CharField(max_length=100);
	Comment=models.TextField(blank=True);
	Department=models.ForeignKey('Department');
	def __unicode__(self):
		return   (self.Name )

class EmployeeForm(ModelForm):
 class Meta:
	model=Employeeall
	fields=['SSNNO','Title','Name','Email_ID','Fax_No','Home_Phone_No','Office_Phone_No','Designation','Address_Line','Order','Department']

class EditEmployeeForm(ModelForm):
 class Meta:
	model=Employeeall
	fields=['Title','Name','Email_ID','Fax_No','Home_Phone_No','Office_Phone_No','Designation','Address_Line','Order','Comment','Department']




class Employeehistory(models.Model):
	SSNNO=  models.IntegerField(max_length=20);
	Department=models.CharField(max_length=100);
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
	Order=models.FileField(upload_to='./media/files/',blank=False);
	Comment=models.TextField(blank=True);
	def __unicode__(self):	
		return str(self.SSNNO)

class ThirdParty(models.Model):
	Reg_No=models.IntegerField(primary_key=True,max_length=20);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Established_Year=models.IntegerField(max_length=4);
	Kind_Of_Company=models.TextField(blank=False);
	Director_Name=models.CharField(max_length=100);
	Din_No=models.IntegerField(max_length=6);
	def __unicode__(self):
		return '%s' %(self.Name);

class ThirdPartyForm(ModelForm):
 class Meta:
	model=ThirdParty
	fields=['Reg_No','Name','Address','Established_Year','Kind_Of_Company','Director_Name','Din_No']

class EditThirdPartyForm(ModelForm):
 class Meta:
	model=ThirdParty
	fields=['Name','Address','Established_Year','Kind_Of_Company','Director_Name','Din_No']


class ThirdPartyHistory(models.Model):
	Reg_No=models.IntegerField(max_length=20);
	Name=models.CharField(max_length=100);
	Address=models.TextField(blank=False);
	Established_Year=models.IntegerField(max_length=4);
	Kind_Of_Company=models.TextField(blank=False);
	Director_Name=models.CharField(max_length=100);
	Din_No=models.IntegerField(max_length=6);
	Modified_By=models.CharField(max_length=100);
	Modified_On=models.DateField(auto_now=True,editable=True,blank=True);

	def __unicode__(self):
		return '%s' %(self.Name);


class Project(models.Model):
	Project_ID=models.AutoField(primary_key=True);
	Project_Name=models.CharField(max_length=100);
	Start_Date=models.DateField(editable=True);
	End_Date=models.DateField(editable=True);
	Amt_Proposed=models.DecimalField(max_digits=13, decimal_places=3);
	Amt_Sanctioned=models.DecimalField(max_digits=13, decimal_places=3);
	Expenditure_Last_Year=models.DecimalField(max_digits=13, decimal_places=3);
	No_of_Installment=models.IntegerField(max_length=6);
	Officer_In_Charge=models.ForeignKey('Employeeall');
	Tender_Notice=models.FileField(upload_to='./media/files/',blank=True);
	Tender_Submitted=models.FileField(upload_to='./media/files/',blank=True);
	Contract=models.FileField(upload_to='./media/files/',blank=True);
	Third_Party=models.ForeignKey('ThirdParty',blank=True,null=True);
	def __unicode__(self):	
		return '%s' %(self.Project_Name)


class ProjectForm(ModelForm):
	class Meta:
		model=Project
		fields=['Project_Name','Start_Date','End_Date','Amt_Proposed','Amt_Sanctioned','Expenditure_Last_Year','No_of_Installment','Officer_In_Charge','Tender_Notice','Tender_Submitted','Contract','Third_Party']


class ProjectFormAll(ModelForm):
	class Meta:
		model=Project
		fields=['Project_Name','Start_Date','End_Date','Amt_Proposed','Amt_Sanctioned','Expenditure_Last_Year','No_of_Installment','Officer_In_Charge','Tender_Notice','Tender_Submitted','Contract','Third_Party']


class Projecthistory(models.Model):
	Project_ID=models.IntegerField(max_length=20);
	Project_Name=models.CharField(max_length=100);
	Start_Date=models.DateField(editable=True);
	End_Date=models.DateField(editable=True);
	Amt_Proposed=models.DecimalField(max_digits=13, decimal_places=3);
	Amt_Sanctioned=models.DecimalField(max_digits=13, decimal_places=3);
	Expenditure_Last_Year=models.DecimalField(max_digits=13, decimal_places=3);
	No_of_Installment=models.IntegerField(max_length=6);
	Officer_In_Charge=models.CharField(max_length=100);
	Tender_Notice=models.FileField(upload_to='./media/files/',blank=True);
	Tender_Submitted=models.FileField(upload_to='./media/files/',blank=True);
	Contract=models.FileField(upload_to='./media/files/',blank=True);
	Third_Party=models.CharField(max_length=100,blank=True,null=True);
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




