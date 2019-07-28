from django.http import Http404
from django.shortcuts import render, get_object_or_404
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .forms import regForm, jobForm, testForm, VideoForm, photoForm, clientForm, serviceForm, branchForm
from .models import Job, Photo, Register, Testimonial, YouTube, Services, Branch, Client
from django.core.mail import send_mail
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def profile(request):
	work=Job.objects.order_by('-pub_date')[:4]
	pics=Photo.objects.all()[:12]
	pics_interview=Photo.objects.filter(album='Interviews')
	pics_briefing=Photo.objects.filter(album='Briefings')
	pics_departures=Photo.objects.filter(album='Departures')
	pics_work=Photo.objects.filter(album='At work')
	tst=Testimonial.objects.order_by('-testmnl_date')
	services = Services.objects.all()
	branches = Branch.objects.all()
	clients = Client.objects.all()
# <<<<------Contact form ------>>>> 
	full_name=request.POST.get('name')
	email=request.POST.get('email')
	subject=request.POST.get('subject')
	text=request.POST.get('message')

	# send_mail(
 #    	'subject',
 #    	'text',
 #    	'email',
 #    	['____@____.com'],
 #    	fail_silently=False,
	# )
	

	for p in work:
		print('<<<<<<<,....SPEEEDING>>>>>.',p.id)
	context={
		'work':work,
		'pics':pics,
		'pics_interview':pics_interview,
		'pics_briefing':pics_briefing,
		'pics_departures':pics_departures,
		'pics_work':pics_work,
		'tst':tst,
		'services': services,
		'branches': branches,
		'clients': clients,
	}
	
	
	return render (request, 'base.html', context)

def client(request):
	if request.method =='POST':
		form =regForm(request.POST)
		if form.is_valid():
			print('<<<<<<<<.....VALID.....>>>>>>>>')
			form.save()

	form = regForm()

	return render(request, 'hm/register.html', {'form': form})

def jobMart(request):
	jobs=Job.objects.order_by('-pub_date')
	dt=date.today()
	print('<<<<<<<<<<<<>>>>>>> vegas', date)
	return render(request, 'hm/all_jobs.html', {'jobs':jobs, 'dt':dt})

def gallery(request):
	image=Photo.objects.all()

	return render(request, 'hm/gallery.html', {'image':image})

def jdetail(request, id):
	job = get_object_or_404(Job, id=id)
	dt = date.today()
	status=''
	if (dt > job.job_exp_date.date()):
		status=1
		
	else:
		status=0
		
	context={'job':job, 'status':status}
	return render(request, "hm/job_detail.html", context)

@login_required()
def dash(request):
	j=Job.objects.order_by('-pub_date')[:7]
	r=Register.objects.order_by('-reg_date')[:7]
	
	for rg in r:
		rgstn=rg.title +' '+ rg.firstName +' '+ rg.surName

	context={
		'j':j,
		'r':r,
		'rgstn':rgstn,
	}

	return render(request, 'hm/dash.html', context)

@login_required()	
def JobListView(request):
	jobs = Job.objects.order_by('-pub_date')
	context = {
		'jobs': jobs,
		'job_sidebar': 'job',
	}
	return render(request, 'hm/dash_jobs.html', context)


class JobDetailView(DetailView):
	model=Job
	slug_field=id
	context_object_name='jobdtl'
	template_name='hm/dashJobDetail.html'

	def get_context_data(self, **kwargs):
		context=super(JobDetailView,self).get_context_data(**kwargs)
		context['job']=Job.objects.get(id=self.kwargs['pk'])
		return context


class JobUpdateView(UpdateView):
	model=Job
	form=jobForm()
	fields=['jobTitle','location','workers','city','wage','work_hours','overtime',
	'accomodation','medical','transport','age_male_min','age_male_max','age_female_min',
	'age_female_max','educ_level','job_desc','job_exp_date']
	
	context_object_name='jobUpdate'
	
	template_name='hm/dashJobEdit.html'

	def get_context_data(self, **kwargs):
		context=super(JobUpdateView, self).get_context_data(**kwargs)
		context['job']=Job.objects.get(id=self.kwargs['pk'])
		form=jobForm(instance=Job.objects.get(id=self.kwargs['pk']))
		return context

	def get_success_url(self):
		return reverse_lazy('home:jobs')


class JobDeleteView(DeleteView):
	model=Job
	template_name='hm/dashJobDel.html'
	success_url=reverse_lazy('jobs')

	def get_context_date(self, **kwargs):
		context=super(JobDeleteView, self).get_context_data(**kwargs)
		context['job']=Job.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:jobs')

@login_required()
def JobCreateView(request):
	if request.method=='POST':
		form = jobForm(request.POST)
		if form.is_valid:
			form.save()
			messages.success(request, 'Job was added successfully!')
			return HttpResponseRedirect('/dashboard/job_sidebar/')
	form=jobForm()

	return render(request, 'hm/dashJobAdd.html', {'form':form})

@login_required()
def testimonial(request):
	t=Testimonial.objects.order_by('-testmnl_date')

	for x in t:
		print('<<<<<testimonial>>>>>>>>', x.img_profile)

	return render(request, 'hm/dash_test.html', {'t':t})

def add_testimonial(request):
	if request.method=='POST':
		form = testForm(request.POST)
		if form.is_valid:	
			form.save()
	form=testForm()

	return render(request, 'hm/add_test.html', {'form':form})

class testDeleteView(DeleteView):
	model=Testimonial
	template_name='hm/dashtestDel.html'
	success_url=reverse_lazy('testimonial')

	def get_context_date(self, **kwargs):
		context=super(testDeleteView, self).get_context_data(**kwargs)
		context['test']=Testimonial.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:testimonial')

def dash_gallery(request):
	img=Photo.objects.all()
	img_interview=Photo.objects.filter(album='Interviews')
	img_briefing=Photo.objects.filter(album='Briefings')
	img_departures=Photo.objects.filter(album='Departures')
	img_work=Photo.objects.filter(album='At work')

	context={
		'img':img,
		'img_work':img_work,
		'img_departures':img_departures,
		'img_interview':img_interview,
		'img_briefing':img_briefing
	}

	return render(request, 'hm/dash_gallery.html',context)

def add_photo(request):
	if request.method=='POST':
		form = photoForm(request.POST, request.FILES)
		if form.is_valid:	
			form.save()
			messages.success(request, 'Photo was added successfully!')
			return HttpResponseRedirect('/dashboard/gallery/')
	form=photoForm()

	return render(request, 'hm/add_photo.html', {'form':form})

class PhotoUpdateView(UpdateView):
	model=Photo
	form=photoForm()
	fields=[
			'picture',
			'album',	
		]
	
	context_object_name='picUpdate'
	
	template_name='hm/dashphotoEdit.html'

	def get_context_data(self, **kwargs):
		context=super(PhotoUpdateView, self).get_context_data(**kwargs)
		context['pic']=Photo.objects.get(id=self.kwargs['pk'])
		form=photoForm(instance=Photo.objects.get(id=self.kwargs['pk']))
		return context

	def get_success_url(self):
		return reverse_lazy('home:dash_gallery')

class PhotoDeleteView(DeleteView):
	model=Photo
	template_name='hm/dashphotoDel.html'
	success_url=reverse_lazy('dash_gallery')

	def get_context_date(self, **kwargs):
		context=super(PhotoDeleteView, self).get_context_data(**kwargs)
		context['pic']=Photo.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:dash_gallery')

# class clientListView(ListView):
# 	model=Register
# 	ordering=['-reg_date']
# 	context_object_name='client'
# 	template_name='hm/dash_reg.html'

@login_required()
def clientListView(request):
	r=Register.objects.order_by('-reg_date')

	return render(request, 'hm/dash_reg.html', {'client':r})

class clientDeleteView(DeleteView):
	model=Register
	template_name='hm/dashClientDel.html'
	success_url=reverse_lazy('clientelle')

	def get_context_date(self, **kwargs):
		context=super(clientDeleteView, self).get_context_data(**kwargs)
		context['client']=Register.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:clientelle')

class clientDetailView(DetailView):
	model=Register
	context_object_name='clientdtl'
	template_name='hm/dashClientDetail.html'

	def get_context_data(self, **kwargs):
		context=super(clientDetailView,self).get_context_data(**kwargs)
		context['client']=Register.objects.get(id=self.kwargs['pk'])
		return context

def yutbe(request):
	videos = []
	vids=YouTube.objects.order_by('-date')
	for v in vids:
		videos.append(v.vidurl[-11:])
		print ("<<<<<<<<,...........>>>>>>>", videos )

	return render(request, 'hm/vid_gallery.html', {'vids':videos })

@login_required()
def VidListView(request):
	videos = []

	vidz=YouTube.objects.order_by('-date')

	for q in vidz:
		videos.append(q.vidurl[-11:])

		print("<<<<<<<<,....alooooo.......>>>>>>>", videos )
		
	return render(request, 'hm/dash_videos.html', {'vidz':videos})

@login_required()
def add_video(request):
	if request.method=='POST':
		form = VideoForm(request.POST)
		if form.is_valid:	
			form.save()
			messages.success(request, 'Video was added successfully!')
			return HttpResponseRedirect('/dashboard/videos')
	form=VideoForm()

	return render(request, 'hm/add_vid.html', {'form':form})

@login_required()
def employer(request):
	employ =Client.objects.all()

	return render(request, 'hm/dash_employer.html', {'emp':employ})	

@login_required()
def add_employer(request):
	if request.method=='POST':
		form = clientForm(request.POST, request.FILES)
		if form.is_valid:	
			form.save()
			messages.success(request, 'Client was added successfully!')
			return HttpResponseRedirect('/dashboard/employers/')
	form=clientForm()

	return render(request, 'hm/add_employer.html', {'form':form})

class employerDeleteView(DeleteView):
	model=Client
	template_name='hm/dashemployerDel.html'
	success_url=reverse_lazy('employers')

	def get_context_date(self, **kwargs):
		context=super(employerDeleteView, self).get_context_data(**kwargs)
		context['emp']=Client.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:employers')

@login_required()
def services(request):
	task=Services.objects.all()

	return render(request, 'hm/dash_services.html', {'task':task})

@login_required()
def add_service(request):
	if request.method=='POST':
		form = serviceForm(request.POST, request.FILES)
		if form.is_valid:	
			form.save()
			messages.success(request, 'Service was added successfully!')
			return HttpResponseRedirect('/dashboard/services/')
	form=serviceForm()

	return render(request, 'hm/add_service.html', {'form':form})

class serviceDeleteView(DeleteView):
	model=Services
	template_name='hm/dashserviceDel.html'
	success_url=reverse_lazy('services')

	def get_context_date(self, **kwargs):
		context=super(serviceDeleteView, self).get_context_data(**kwargs)
		context['serve']=Services.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:services')

class serviceUpdateView(UpdateView):
	model=Services
	form=serviceForm()
	fields=[
			'name',
			'description',	
		]
	
	context_object_name='taskUpdate'
	
	template_name='hm/dashserviceEdit.html'

	def get_context_data(self, **kwargs):
		context=super(serviceUpdateView, self).get_context_data(**kwargs)
		context['task']=Services.objects.get(id=self.kwargs['pk'])
		form=serviceForm(instance=Services.objects.get(id=self.kwargs['pk']))
		return context

	def get_success_url(self):
		return reverse_lazy('home:services')

@login_required()
def branches(request):
	brnch=Branch.objects.all()

	return render(request, 'hm/dash_branch.html', {'brnch':brnch})

@login_required()
def add_branch(request):
	if request.method=='POST':
		form = branchForm(request.POST, request.FILES)
		if form.is_valid:	
			form.save()
			messages.success(request, 'Branch was added successfully!')
			return HttpResponseRedirect('/dashboard/branch/')
	form=branchForm()

	return render(request, 'hm/add_branch.html', {'form':form})

class branchDeleteView(DeleteView):
	model=Branch
	template_name='hm/dashbranchDel.html'
	success_url=reverse_lazy('branches')

	def get_context_date(self, **kwargs):
		context=super(branchDeleteView, self).get_context_data(**kwargs)
		context['brnc']=Branch.objects.get(id=self.kwargs['pk'])
		return context

	def get_success_url(self):
		return reverse_lazy('home:branches')

class branchUpdateView(UpdateView):
	model=Branch
	form=branchForm()
	fields=[
			'name',
			'location',
			'contact'	
		]
	
	context_object_name='branchUpdate'
	
	template_name='hm/dashbranchEdit.html'

	def get_context_data(self, **kwargs):
		context=super(branchUpdateView, self).get_context_data(**kwargs)
		context['brnch']=Branch.objects.get(id=self.kwargs['pk'])
		form=branchForm(instance=Branch.objects.get(id=self.kwargs['pk']))
		return context

	def get_success_url(self):
		return reverse_lazy('home:branch')

# class PasswordResetView(PasswordResetView):
#     template_name = 'registration/password_reset.html'
#     success_url = reverse_lazy('home:password_reset_done')
#     subject_template_name = 'registration/password_reset_subject.txt'
#     email_template_name = 'registration/password_reset_email.html'



# class PasswordResetDone(PasswordResetDoneView):
# 	template_name='registration/password_reset_done.html'


# class PasswordResetConfirm(PasswordResetConfirmView):
# 	template_name = 'registration/password_reset_confirm.html'
# 	success_url = reverse_lazy('home:password_reset_complete')
# 	form_valid_message = ("Your password was changed!")

# 	def form_valid(self, form):
# 		form.save()
# 		return super().form_valid(form)


# class PasswordResetComplete(PasswordResetCompleteView):
# 	template_name='registration/password_reset_complete.html'
# 	print('<<<<<<<<<<<<<<<<+++++>>>>>>>>>>>> all of the lights')
