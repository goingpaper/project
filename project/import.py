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
	description = bar.get('description'))
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
				  name = drink.get('name'))
	
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
				   price = serve.get('Price'))
	serve.full_clean()
	serve.save()

with open('users.json') as f:
	users_doc = json.load(f)
	
for user in users_doc:
	
	new_user = User.objects.create_user(user.get('username'),
					user.get('email'),
					user.get('password'))
	new_user.first_name = user.get('firstName') #can do this!!!!!!!
	new_user.last_name = user.get('lastName')
	#new_user.date_joined = datetime.str
	new_user.save()
	#difficult to set more fields
					
	

	
	

	
