from django.views import generic
from barreviews.models import *
from django.contrib.auth import authenticate

def login_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		return HttpResponseRedirect("/account/loggedin/")
	else:
		# Show an error page
		return HttpResponseRedirect("/account/invalid/")

def logout_view(request):
	auth.logout(request)
	# Redirect to a success page.
	return HttpResponseRedirect("/account/loggedout/")

class IndexView(generic.ListView):
	template_name = 'barreviews/index.html'
	context_object_name = 'index'

	
	
	
	def get_queryset(self):
		return (x for x in range(0,1))

class BarsView(generic.ListView):
	template_name = 'barreviews/bars.html'
	context_object_name = 'bars'
	
	def get_queryset(self):
		return (x for x in range(0,1)) #Bar.objects.all()

class UsersView(generic.ListView):
	template_name = 'barreviews/users.html'
	context_object_name = 'users'
	
	def logout_view(request):
		auth.logout(request)
		# Redirect to a success page.
		return HttpResponseRedirect("/account/loggedout/")
	
	def get_queryset(self):
		return (x for x in range(0,1)) #User.objects.all()

class DrinksView(generic.ListView):
	template_name = 'barreviews/drinks.html'
	context_object_name = 'drinks'
	
	def get_queryset(self):
		return (x for x in range(0,1)) #Drink.objects.all()

class ReviewsView(generic.ListView):
	template_name = 'barreviews/reviews.html'
	context_object_name = 'reviews'
	
	def get_queryset(self):
		return (x for x in range(0,1)) #Review.objects.all()
		
#More specific views below
		
class BarView(generic.DetailView):
	model = Bar
	template_name = 'barreviwes/bar.html'

def bar_add(request):
	if request.method == "POST":
		form = BarForm(request.POST)
		if form.is_valid():
			bar = form.save()
			return redirect('barreviews:bar', pk=bar.id)
	else:
		form = BarForm()
	return render(request, 'barreviews/bar_add.html', {'form': form})

def bar_edit(request, pk):
	instance = Bar.objects.get(pk=pk)
	if request.method == "POST":
		form = BarForm(request.POST, instance = instance)
		if form.is_valid():
			car = form.save()
			return redirect('barreviews:bar', pk=bar.id)
	else:
		form = BarForm(instance = instance)
	return render(request, 'barreviews/bar_edit.html', {'form': form})

def bar_delete(request, pk):
	instance = Bar.objects.get(pk=pk)
	instance.delete()
	return redirect('laptimes:bars')

class DrinkView(generic.DetailView):
	model = Drink
	template_name = 'barreviwes/drink.html'

def drink_add(request):
	if request.method == "POST":
		form = DrinkForm(request.POST)
		if form.is_valid():
			drink = form.save()
			return redirect('barreviews:drink', pk=drink.id)
	else:
		form = DrinkForm()
	return render(request, 'barreviews/drink_add.html', {'form': form})

def drink_edit(request, pk):
	instance = Drink.objects.get(pk=pk)
	if request.method == "POST":
		form = DrinkForm(request.POST, instance = instance)
		if form.is_valid():
			drink = form.save()
			return redirect('barreviews:drink', pk=drink.id)
	else:
		form = DrinkForm(instance = instance)
	return render(request, 'barreviews/drink_edit.html', {'form': form})

def drink_delete(request, pk):
	instance = Drink.objects.get(pk=pk)
	instance.delete()
	return redirect('laptimes:drinks')

class UserView(generic.DetailView):
	model = User
	template_name = 'barreviwes/user.html'

def user_add(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			return redirect('barreviews:user', pk=user.id)
	else:
		form = UserForm()
	return render(request, 'barreviews/user_add.html', {'form': form})

def user_edit(request, pk):
	instance = User.objects.get(pk=pk)
	if request.method == "POST":
		form = UserForm(request.POST, instance = instance)
		if form.is_valid():
			user = form.save()
			return redirect('barreviews:user', pk=user.id)
	else:
		form = UserForm(instance = instance)
	return render(request, 'barreviews/user_edit.html', {'form': form})

def user_delete(request, pk):
	instance = User.objects.get(pk=pk)
	instance.delete()
	return redirect('laptimes:users')
