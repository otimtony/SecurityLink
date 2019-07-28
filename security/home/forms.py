from django import forms
from .models import Register, Job,Testimonial, Photo, YouTube, Client, Services, Branch
from django.utils.translation import ugettext_lazy as _


class regForm(forms.ModelForm):
	
	class Meta:
		model=Register

		fields=[
			'title',
			'surName',
			'firstName',
			'sex',
			'maritalStatus',
			'age',
			'passportNo',
			'tel',
			'email',
			'birthPlace',
			'county',
			'subCounty',
			'village',
			'residence',
			'profession',
			'academic',
			'spouse',
			'children',
			'mothersName',
			'fathersName',
			'parentsDistrict',
			'parentsTel',
			'kin',
			'kinDistrict',
			'kinTel',
		]	

		labels={
			'title':_(''),
			'email':_(''),
			'district':_(''),
			'county':_(''),
			'village':_(''),
			'profession':_(''),
			'parentsDistrict':_(''),
			'sex':_(''),
			'age':_(''),
			'surName': _(''),
			'firstName':_(''),
			'maritalStatus':_(''),
			'passportNo':_(''),
			'tel':_(''),
			'birthPlace':_(''),
			'subCounty':_(''),
			'residence':_(''),
			'academic':_(''),
			'spouse':_(''),
			'children':_(''),
			'fathersName':_(''),
			'mothersName':_(''),
			'parentsTel':_(''),
			'kin':_(''),
			'kinDistrict':_(''),
			'kinTel':_('')
		}
		widgets={
			'title':forms.Select(),
			'tel':forms.NumberInput(attrs={'placeholder':'Phone number'}),
			'surName':forms.TextInput(attrs={'placeholder':'Surname'}),
			'firstName':forms.TextInput(attrs={'placeholder':'First name'}),
			'age':forms.NumberInput(attrs={'placeholder':'Your age'}),
			'email':forms.TextInput(attrs={'placeholder':'Email'}),
			'passportNo':forms.NumberInput(attrs={'placeholder':'Passport number'}),
			'birthPlace':forms.TextInput(attrs={'placeholder':'District of birth '}),
			'county':forms.TextInput(attrs={'placeholder':'County'}),
			'subCounty':forms.TextInput(attrs={'placeholder':'Subcounty'}),
			'village':forms.TextInput(attrs={'placeholder':'Village'}),
			'residence':forms.TextInput(attrs={'placeholder':'Residence'}),
			'profession':forms.TextInput(attrs={'placeholder':'Profession'}),
			'academic':forms.TextInput(attrs={'placeholder':'Academic Qualification'}),
			'spouse':forms.TextInput(attrs={'placeholder':'Name of spouse'}),
			'children':forms.NumberInput(attrs={'placeholder':'Number of children'}),
			'mothersName':forms.TextInput(attrs={'placeholder':'Mothers name'}),
			'fathersName':forms.TextInput(attrs={'placeholder':'Fathers name'}),
			'parentsDistrict':forms.TextInput(attrs={'placeholder':'Parents district'}),
			'parentsTel':forms.TextInput(attrs={'placeholder':'Parents Tel.'}),
			'kin':forms.TextInput(attrs={'placeholder':'Next of Kin'}),
			'kinDistrict':forms.TextInput(attrs={'placeholder':'District'}),
			'kinTel':forms.NumberInput(attrs={'placeholder':'Phone number'})
		}

class jobForm(forms.ModelForm):
	
	class Meta:
		model=Job	
		fields=[
			'jobTitle',
			'location',
			'workers',
			'city',
			'wage',
			'work_hours',
			'overtime',
			'accomodation',
			'medical',
			'transport',
			'age_male_min',
			'age_male_max',
			'age_female_min',
			'age_female_max',
			'educ_level',
			'job_desc',
			'job_exp_date',
		]
		widgets={
			'job_exp_date':forms.DateTimeInput()
		}
class testForm(forms.ModelForm):
	class Meta:
		model=Testimonial

		fields=[
			'name',
			'img_profile',
			'occupation',
			'testimonial_desc',
		]

		labels={
			'img_profile':_('Picture'),
			'name':_('Name'),
			'testimonial_desc':_('Description'),
			'occupation':_('Occupation')
			}
class photoForm(forms.ModelForm):
	
	class Meta:
		model=Photo

		fields=[
			'picture',
			'album',	
		]

class VideoForm(forms.ModelForm):
	class Meta:
		model=YouTube

		fields=[
			'vidurl',
		]
		labels={
			'vidurl':_('Video Url')
		}

class clientForm(forms.ModelForm):
	class Meta:
		model=Client

		fields=[
			'name',
			'logo'
		]
		
class serviceForm(forms.ModelForm):
	class Meta:
		model=Services

		fields=[
			'name',
			'description',
		]

class branchForm(forms.ModelForm):
	class Meta:
		model=Branch

		fields=[
			'name',
			'location',
			'contact'
		]