import json
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import utils
from barreviews.models import Bar, User, Drink, Brewery, ReviewBar, LikesBeer, Serves, Comment
from django.contrib.auth.models import User

#errors
Serves.objects.all().delete()
Comment.objects.all().delete()
LikesBeer.objects.all().delete()
ReviewBar.objects.all().delete()
Bar.objects.all().delete()
User.objects.all().delete()
Drink.objects.all().delete()
Brewery.objects.all().delete()


with open('bars.json') as f:
	bars_doc = json.load(f)
	
for bar in bars_doc:
	
	bar = Bar(name = bar.get('name'),
	address = bar.get('address'),
	phone = bar.get('phone'),
	email = bar.get('email'),
	website = bar.get('website'),
	yearEstablished = bar.get('yearEstablished'),
	description = bar.get('description')
	)
	bar.full_clean()
	bar.save()

with open('drinks.json') as f:
	drinks_doc = json.load(f)

for drink in drinks_doc:
	#drink_exist = Drink.objects.get
	try:
		brew = Brewery.objects.get(name=drink.get('brewery'))

	except Brewery.DoesNotExist:

		brewery = Brewery(name=drink.get('brewery'))
		brewery.full_clean()
		brewery.save()
		
	#if not Brewery.objects.get(name=drink.get('brewery')):
	#	brewery = Brewery(name=drink.get('brewery'))
	#	brewery.fulll_clean()
	#	brewery.save()
		
	drink = Drink(brewery=Brewery.objects.get(name=drink.get('brewery')),
				  dType=drink.get('type'),
				  name = drink.get('name')
				  )
	
	drink.full_clean()
	drink.save()

with open('serves.json') as f:
	serves_doc = json.load(f)

for serve in serves_doc:
	try:

		nbar = Bar.objects.get(name=serve.get('bID'))

	except Bar.DoesNotExist:
		nbar = None

	try:
		ndrink = Drink.objects.get(name=serve.get('dID'))

	except Drink.DoesNotExist:

		ndrink = None

	serve = Serves(bar = nbar,
				   drink = ndrink,
				   onTap = serve.get('onTap'),
				   price = serve.get('Price')
				   )
	serve.full_clean()
	serve.save()

with open('users.json') as f:
	users_doc = json.load(f)
	
for user in users_doc:
	
	new_user = User.objects.create_user(user.get('username'),
					user.get('email'),
					user.get('password')
					)
	new_user.first_name = user.get('firstName') #can do this!!!!!!!
	new_user.last_name = user.get('lastName')

	if user.get('dateRegistered'):
		new_user.date_joined = datetime.strptime(user.get('dateRegistered'), "%d %B %Y" ) 
	else:
		new.user.date_joined = None

	new_user.save()
	#difficult to set more fields
					
with open('review_bar.json') as f:
	review_doc = json.load(f)

for review in review_doc:
	
	try:

		this_user = User.objects.get(username=review.get('user'))

	except User.DoesNotExist:
		this_user = None

	try:

		this_bar = Bar.objects.get(name=review.get('bar'))

	except Bar.DoesNotExist:
		this_bar = None

	review = ReviewBar(user =this_user,
				bar =this_bar,
				rating = review.get('rating'),
				date = datetime.strptime(review.get('date'),"%d %B %Y" ) if review.get('date') else None,
				comment = review.get('comment')
				)	

	review.full_clean()
	review.save()

with open('likesbeer.json') as f:
	likes_doc = json.load(f)

for like in likes_doc:

	try:

		this_user = User.objects.get(username = like.get('username'))

	except User.DoesNotExist:
		this_user = None

	try:

		this_drink = Drink.objects.get(name = like.get('drink'))

	except Drink.DoesNotExist:
		this_drink = None

	like = LikesBeer(user = this_user,
				drink = this_drink 
			)
	like.full_clean()
	like.save()

with open('comments.json') as f:
	comments_doc = json.load(f)

for comment in comments_doc:
	
	try:
		first_user = User.objects.get(username = comment.get('user1'))

	except User.DoesNotExist:
		first_user = None
	
	try:
		second_user = User.objects.get(username = comment.get('user2'))

	except User.DoesNotExist:
		second_user = None

	new_comment = Comment(user1 = first_user,
				user2 = second_user,
				date = datetime.strptime(comment.get('date'),"%d %B %Y" ) if comment.get('date') else None,
				comment = comment.get('comment')
				)
	new_comment.full_clean()
	new_comment.save()

	
