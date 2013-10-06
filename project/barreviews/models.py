from django.db import models

# Create your models here.
class Bar(models.Model):

	name = models.CharField(max_length=100) # bar name is not null and is not empty
	address = models.CharField(max_length=100,blank = True,null = True) # address can be empty or null
	phone = models.CharField(max_length=100) # unsure if this is right?????????!!!!!
	email = models.CharField(max_length=100,blank = True,null = True)
	website = models.CharField(max_length=100,blank = True,null = True)
	yearEstablished = models.DateField(blank=True,null=True)
	description = models.CharField(max_length=300,blank = True,null = True)
	
class User(models.Model):

	username = models.CharField(max_length=100) # username compulsory
	password = models.CharField(max_length=100) # password compulsory
	fname = models.CharField(max_length=100) # fname compulsory
	lname = models.CharField(max_length=100) # lname compulsory
	email = models.CharField(max_length=100) # email compulsory
	register_date = models.DateField(blank=True,null=True) 
	user_type = models.CharField(max_length=100) #compulsory
	
class Drink(models.Model):

	dID = models.IntegerField() 
	brewery = models.CharField(max_length=100) 
	type = models.CharField(max_length=100) 
	name = models.CharField(max_length=100) 

class Brewery(models.Model):

	name = models.CharField(max_length=100) #not sure
	
class ReviewBar(models.Model):

	username = models.ForeignKey('User') # ? constraints
	barName = models.ForeignKey('Bar') # ? constraints
	rating = models.IntegerField() #?
	date = models.DateField()
	comment = models.CharField(max_length=300)
	#unable to make a multifield primary key in django

class LikesBeer(models.Model):
	
	username = models.CharField(max_length=100) 
	drinkName = models.ForeignKey('Drink')
	
class Serves(models.Model):
	
	barName = models.ForeignKey('Bar')
	drinkName = models.ForeignKey('Drink')
	onTap = models.BooleanField()
	price = models.DecimalField(5,2) #max 5 digit number and 2 decimal places
	
class Comment(models.Model):

	user1 = models.ForeignKey('User')
	user2 = models.ForeignKey('User')
	date = models.DateField()
	comment = models.CharField(max_length=300)
	

	
	