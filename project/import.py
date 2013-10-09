import json
from datetime import datetime
from django.core.exceptions import ValidationError
from django.db import utils
from barreviews.models import Bar, User, Drink, Brewery, ReviewBar, LikesBeer, Serves, Comment

Bar.objects.all().delete()
User.objects.all().delete()
Drink.objects.all().delete()
Brewery.objects.all().delete()
ReviewBar.objects.all().delete()
LikesBeer.objects.all().delete()
Serves.objects.all().delete()
Commet.objects.all().delete()

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
	
	drink = Drink(brewery=drink.get('brewery'),
				  dType=drink.get('type'),
				  name = drink.get('name'))
	
	drink.full_clean()
	drink.save()

with open('serves.json') as f:
	serves_doc = json.load(f)

for serve in serves_doc:

	serve = Serves(barName = serve.get('bID'),
				   drinkName = serve.get('dID'),
				   onTap = serve.get('onTap'),
				   price = serve.get('Price'))
	serve.full_clean()
	serve.save()


	

	
	

	