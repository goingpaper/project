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
	description = bar.get('description')

	