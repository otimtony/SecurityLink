from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Testimonial(models.Model):
	name=models.CharField(max_length=100)
	img_profile=models.FileField(upload_to='media/gallery/profile',blank=True)
	occupation=models.CharField(max_length=100)
	testimonial_desc=models.TextField()
	testmnl_date=models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Job(models.Model):
	
	jobTitle=models.CharField(max_length=1000, verbose_name='Job title')
	location=models.CharField(max_length=1000, verbose_name='Country')
	workers=models.PositiveIntegerField(default=0, verbose_name='No. of workers')
	city=models.CharField(max_length=1000, verbose_name='City')
	wage=models.PositiveIntegerField(default=0, verbose_name='Wage')
	work_hours=models.PositiveIntegerField(default=0, verbose_name='No. of working hours')
	overtime=models.PositiveIntegerField(default=0, verbose_name='Overtime')
	accomodation=models.CharField(max_length=1000, verbose_name='Accomodation')
	medical=models.CharField(max_length=1000, verbose_name='Medical insurance')
	transport=models.CharField(max_length=1000, verbose_name='Tansport')
	age_male_min=models.PositiveIntegerField(default=18, verbose_name='Male minimum age',validators=[MinValueValidator(18)])
	age_male_max=models.PositiveIntegerField(default=0, verbose_name='Male maximum age')
	age_female_min=models.PositiveIntegerField(default=18, verbose_name='Female minimum age',validators=[MinValueValidator(18)])
	age_female_max=models.PositiveIntegerField(default=0, verbose_name='Female maximum age')
	educ_level=models.CharField(max_length=1000, verbose_name='Minimum educ_level')
	job_desc=models.TextField(max_length=2000, default='Job Description', verbose_name='Job description')
	pub_date=models.DateTimeField(auto_now_add=True,null=True)
	job_exp_date=models.DateTimeField(null=True)


	class Meta:
		verbose_name='Job'
		verbose_name_plural='Jobs'
		
	def expiration(self):
		return self.job_exp_date.strftime('%B %d %Y')

	def __str__(self):
		return self.jobTitle + self.location + str(self.workers)

class Photo(models.Model):
	ALBUM_CHOICES=(
		('Interviews','Interviews'),
		('Departures','Departures'),
		('Briefings','Briefings'),
		('At work', 'At work'),
		)	
	picture =models.ImageField(upload_to='gallery')
	album = models.CharField(choices=ALBUM_CHOICES, max_length=10)
	timestamp=models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return str(self.picture) + self.album

class Register(models.Model):
	SEX_CHOICES=(
		('Male','Male'),
		('Female','Female'),
		)

	MARITAL_CHOICES=(
		('Single','Single'),
		('Married','Married')
		)
	TITLE_CHOICES=(
		('Mr','Mr'),
		('Mrs','Mrs'),
		('Ms', 'Ms')
		)
	
	title=models.CharField(max_length=5, choices=TITLE_CHOICES)
	firstName=models.CharField(max_length=100)
	surName=models.CharField(max_length=100)
	sex=models.CharField(choices=SEX_CHOICES, max_length=10)
	maritalStatus=models.CharField(choices=MARITAL_CHOICES, max_length=10)
	age=models.PositiveIntegerField()
	passportNo=models.PositiveIntegerField()
	tel=models.PositiveIntegerField()
	email=models.EmailField(blank=True)
	birthPlace=models.CharField(max_length=200, verbose_name='District of birth')
	county=models.CharField(max_length=100)
	subCounty=models.CharField(max_length=100)
	village=models.CharField(max_length=100)
	residence=models.CharField(max_length=100)
	profession=models.CharField(max_length=200)
	academic=models.CharField(max_length=500)
	spouse=models.CharField(max_length=100, blank=True)
	children=models.PositiveIntegerField( blank=True)
	fathersName=models.CharField(max_length=100)
	mothersName=models.CharField(max_length=100)
	parentsDistrict=models.CharField(max_length=100)
	parentsTel=models.PositiveIntegerField(blank=True)
	kin=models.CharField(max_length=100)
	kinDistrict=models.CharField(max_length=100)
	kinTel=models.PositiveIntegerField()
	reg_date=models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return str(self.age) + self.title + self.firstName + self.surName

class YouTube(models.Model):

	vidurl = models.URLField(max_length=200)
	date=models.DateTimeField(auto_now_add=True, null=True)

class Services(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return str(self.name)

class Branch(models.Model):
	name = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)

	def __str__(self):
		return str(self.name)

class Message(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(blank=True)
	subject = models.CharField(max_length=100)
	message = models.TextField()

class Client(models.Model):
	name = models.CharField(max_length=100)
	logo = models.ImageField(blank=True)

	def __str__(self):
		return str(self.name)




