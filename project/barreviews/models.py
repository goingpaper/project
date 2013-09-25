from django.db import models

# Create your models here.
class Bar(models.Model):
	bID = models.IntegerField() # possibly obselete
	name = models.CharField(max_length=100) # bar name is not null and is not empty
	address = models.CharField(max_length=100,blank = True,null = True) # address can be empty or null
	phone = models.CharField(max_length=100) # unsure if this is right?????????!!!!!
	email = models.CharField(max_length=100,blank = True,null = True)
	website = models.CharField(max_length=100,blank = True,null = True)
	yearmade = models.DateField(blank=True,null=True)
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
	dtype = models.CharField(max_length=100) 
	name = models.CharField(max_length=100) 
