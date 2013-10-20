from django.views import generic
from barreviews.models import *
from barreviews.forms import *
from django.contrib import auth
from django.shortcuts import *
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf

# Login views

def login(request):
	if request.user.username == '':
		c = {}
		c.update(csrf(request))
		return render_to_response('login.html',c)
	else:
		return HttpResponseRedirect("/users/")

def auth_view(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_active:
		# Correct password, and the user is marked "active"
		auth.login(request, user)
		# Redirect to a success page.
		print request.user.username, 'is staff?', request.user.is_staff
		return HttpResponseRedirect("/accounts/loggedin/")
	else:
		# Show an error page
		return HttpResponseRedirect("/accounts/invalid/")

def drink_like(request, pk):
	instance = Drink.objects.get(pk=pk)
	existing = LikesBeer.objects.filter(drink=instance, user=request.user).count()
	if request.user.is_authenticated() and existing==0:
		like = LikesBeer.objects.create_like(request.user, instance)
		return redirect('barreviews:drink', pk=instance.id)
	else:
		return redirect('barreviews:drink', pk=instance.id)

def drink_unlike(request, pk):
	instance = Drink.objects.get(pk=pk)
	existing = LikesBeer.objects.filter(drink=instance, user=request.user).count()
	if request.user.is_authenticated() and existing==1:
		like = LikesBeer.objects.get(drink=instance.pk, user=request.user)
		like.delete()
		return redirect('barreviews:drink', pk=instance.id)
	else:
		return redirect('barreviews:drink', pk=instance.id)

def loggedin(request):
    return render_to_response('loggedin.html',
                              {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
	auth.logout(request)
	# Redirect to a success page.
	return render_to_response('logout.html')

class IndexView(generic.ListView):
	template_name = 'barreviews/index.html'
	context_object_name = 'index'

	def get_queryset(self):
		return (x for x in range(0,1))

class BarsView(generic.ListView):
	template_name = 'barreviews/bars.html'
	context_object_name = 'bars'
	
	def get_queryset(self):
		#return (x for x in range(0,1)) 
		return Bar.objects.all()

class UsersView(generic.ListView):
	template_name = 'barreviews/users.html'
	context_object_name = 'users'
	
	def get_queryset(self):
		return User.objects.exclude(is_superuser=True)

class DrinksView(generic.ListView):
	template_name = 'barreviews/drinks.html'
	context_object_name = 'drinks'
	
	def get_queryset(self):
		#return (x for x in range(0,1)) #
		return Drink.objects.all().order_by('brewery__name')


class ReviewsView(generic.ListView):
	template_name = 'barreviews/reviews.html'
	context_object_name = 'reviews'
	
	def get_queryset(self):
		#return (x for x in range(0,1)) 
		return ReviewBar.objects.all()
		
class CommentsView(generic.ListView):
	template_name = 'barreviews/comments.html'
	context_object_name = 'comments'
	
	def get_queryset(self):
		#return (x for x in range(0,1)) 
		return Comment.objects.all()
#More specific views below
		
class BarView(generic.DetailView):
	model = Bar
	template_name = 'barreviews/bar.html'

def bar_add(request):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	if request.method == "POST":
		form = BarForm(request.POST)
		if form.is_valid():
			bar = form.save()
			return redirect('barreviews:bar', pk=bar.id)
	else:
		form = BarForm()
	return render(request, 'barreviews/bar_add.html', {'form': form})

def bar_edit(request, pk):
	print request.user.username, 'is staff?', request.user.is_staff
	if not request.user.is_staff:
		return redirect('barreviews:bars')
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
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	instance = Bar.objects.get(pk=pk)
	instance.delete()
	return redirect('barreviews:bars')

class DrinkView(generic.DetailView):
	model = Drink
	template_name = 'barreviews/drink.html'

def drink_add(request):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	if request.method == "POST":
		form = DrinkForm(request.POST)
		if form.is_valid():
			drink = form.save()
			return redirect('barreviews:drink', pk=drink.id)
	else:
		form = DrinkForm()
	return render(request, 'barreviews/drink_add.html', {'form': form})

def drink_edit(request, pk):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	instance = Drink.objects.get(pk=pk)
	if request.method == "POST":
		form = DrinkForm(request.POST, instance = instance)
		if form.is_valid():
			drink = form.save()
			return redirect('barreviews:drink', pk=pid)
	else:
		form = DrinkForm(instance = instance)
	return render(request, 'barreviews/drink_edit.html', {'form': form})

def drink_delete(request, pk):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	instance = Drink.objects.get(pk=pk)
	instance.delete()
	return redirect('barreviews:drinks')

class UserView(generic.DetailView):
	model = User
	template_name = 'barreviews/user.html'
	context_object_name = 'usertemp'

def user_add(request):
	if request.method == "POST":
		form = UserForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()
			return redirect('barreviews:user', pk=user.id)
	else:
		form = UserForm()
	return render(request, 'barreviews/user_add.html', {'form': form})

def user_edit(request, pk):
	instance = User.objects.get(pk=pk)
	if not request.user.pk == instance.pk and not request.user.is_staff:
		return redirect('barreviews:user', pk=instance.pk)
	if request.method == "POST":
		form = UserForm(request.POST, instance = instance)
		if form.is_valid():
			user = form.save()
			return redirect('barreviews:user', pk=user.id)
	else:
		form = UserForm(instance = instance)
	return render(request, 'barreviews/user_edit.html', {'form': form})

def user_delete(request, pk):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	if int(request.user.id) == int(pk):
		instance = User.objects.get(pk=pk)
		instance.delete()
	return redirect('barreviews:users')

class ReviewView(generic.DetailView):
	model = ReviewBar
	context_object_name = 'review'
	template_name = 'barreviews/review.html'

def review_add(request):
	if request.method == "POST":
		form = ReviewForm(request.POST)
		if form.is_valid():
			review = form.save()
			return redirect('barreviews:review', pk=review.id)
	else:
		form = ReviewForm()
	return render(request, 'barreviews/review_add.html', {'form': form})

def review_auth(request, pk):
	comment = request.POST.get('comment', '')
	rating = request.POST.get('rating', '')
	bar_temp = Bar.objects.get(pk=pk)
	if comment is not None and rating is not None and request.user.is_active:
		new_review = ReviewBar.objects.create_review(request.user, bar_temp, rating, comment)
		return redirect('barreviews:bar', pk=pk)
	else:
		# Show an error page
		return redirect('barreviews:bar', pk=pk)

def review_edit(request, pk):
	instance = ReviewBar.objects.get(pk=pk)
	if not request.user.pk == instance.user.pk and not request.user.is_staff:
		return redirect('barreviews:bar', pk=instance.bar.id)
	if request.method == "POST":
		form = ReviewForm(request.POST, instance = instance)
		if form.is_valid():
			review = form.save()
			return redirect('barreviews:review', pk=review.id)
	else:
		form = ReviewForm(instance = instance)
	return render(request, 'barreviews/review_edit.html', {'form': form})

def review_delete(request, pk):
	instance = ReviewBar.objects.get(pk=pk)
	temp = instance
	if request.user.pk == instance.user.pk or request.user.is_staff:
		instance.delete()
	return redirect('barreviews:bar', pk=temp.bar.id)
	
class BreweriesView(generic.ListView):
	template_name = 'barreviews/breweries.html'
	context_object_name = 'breweries'
	
	def get_queryset(self):
		#return (x for x in range(0,1)) #
		return Brewery.objects.all()

class BreweryView(generic.DetailView):
	model = Brewery
	template_name = 'barreviews/brewery.html'

def brewery_add(request):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	if request.method == "POST":
		form = BreweryForm(request.POST)
		if form.is_valid():
			brewery = form.save()
			return redirect('barreviews:brewery', pk=brewery.id)
	else:
		form = BreweryForm()
	return render(request, 'barreviews/brewery_add.html', {'form': form})

def brewery_edit(request, pk):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	instance = Brewery.objects.get(pk=pk)
	if request.method == "POST":
		form = BreweryForm(request.POST, instance = instance)
		if form.is_valid():
			brewery = form.save()
			return redirect('barreviews:brewery', pk=brewery.id)
	else:
		form = BreweryForm(instance = instance)
	return render(request, 'barreviews/brewery_edit.html', {'form': form})

def brewery_delete(request, pk):
	if not request.user.is_staff:
		return redirect('barreviews:bars')
	instance = Brewery.objects.get(pk=pk)
	instance.delete()
	return redirect('barreviews:breweries')

def comment_add(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			new_comment = form.save()
			return redirect('barreviews:comment', pk=new_comment.id)
	else:
		form = CommentForm()
	return render(request,'barreviews/comment_add.html', {'form': form})

def comment_edit(request, pk):
	instance = Comment.objects.get(pk=pk)
	if not request.user.pk == instance.user1.pk and not request.user.is_staff:
		return redirect('barreviews:user', pk=instance.user2.id)
	if request.method == "POST":
		form = CommentForm(request.POST, instance = instance)
		if form.is_valid():
			comment = form.save()
			return redirect('barreviews:user', pk=comment.user2.pk)
	else:
		form = CommentForm(instance = instance)
	return render(request, 'barreviews/comment_edit.html', {'form': form})

def comment_delete(request, pk):
	instance = Comment.objects.get(pk=pk)
	temp = instance
	if request.user.pk == instance.user1.pk or request.user.is_staff:
		instance.delete()
	return redirect('barreviews:user', pk=temp.user2.pk)

def comment_auth(request, pk):
	comment = request.POST.get('comment', '')
	user_temp = User.objects.get(pk=pk)
	if comment is not None and request.user.is_active:
		new_comment = Comment.objects.create_comment(request.user, user_temp, comment)
		return redirect('barreviews:user', pk=pk)
	else:
		# Show an error page
		return redirect('barreviews:user', pk=pk)


