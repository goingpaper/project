from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Bar(models.Model):
	name = models.CharField(max_length=100,unique=True)
	address = models.CharField(max_length=100,unique=True)
	phone = models.CharField(max_length=100,blank = True,null = True,unique=True)
	email = models.CharField(max_length=100,blank = True,null = True,unique=True)
	website = models.CharField(max_length=100,blank = True,null = True)
	yearEstablished = models.IntegerField(blank=True,null=True)
	description = models.CharField(max_length=300,blank = True,null = True)
	
	def __unicode__(self):
		return self.name
	
#<<<<<<< HEAD
class Brewery(models.Model):
	name = models.CharField(max_length=100,unique=True) #not sure
	
	def __unicode__(self):
		return self.name
	
#=======
#>>>>>>> 66c74678ea10f6d96cb5b822b777f6f1699b622f
class Drink(models.Model):
	brewery = models.ForeignKey(Brewery)
	dType = models.CharField(max_length=100)
	name = models.CharField(max_length=100,unique=True)
	
	def __unicode__(self):
		return self.name


	
class ReviewBar(models.Model):
	user = models.ForeignKey(User) # ? constraints
	bar = models.ForeignKey(Bar) # ? constraints #?
	RATING_CHOICES = (
		(1,1),
		(2,2),
		(3,3),
		(4,4),
		(5,5)
		)
	rating = models.IntegerField(choices=RATING_CHOICES)
	date = models.DateField(auto_now_add=True)
	comment = models.CharField(max_length=300)
#unable to make a multifield primary key in django
	def __unicode__(self):
		return '%s reviews %s' % (self.user , self.bar)

	class Meta:
		unique_together = ('user', 'bar', 'date')

class LikesBeer(models.Model):
	user = models.ForeignKey(User)#changed
	drink = models.ForeignKey(Drink)

	class Meta:
		unique_together = ('user', 'drink')
    
	def __unicode__(self):
		return '%s likes %s' % (self.user , self.drink)

class Serves(models.Model):
	bar = models.ForeignKey(Bar)
	drink = models.ForeignKey(Drink)
	onTap = models.BooleanField()
	price = models.DecimalField(max_digits=5,decimal_places=2)

	def __unicode__(self):
		return '%s serves %s' % (self.bar , self.drink)

	class Meta:
		unique_together = ('bar', 'drink')

	
class Comment(models.Model):
	user1 = models.ForeignKey(User,related_name = 'source')
	user2 = models.ForeignKey(User,related_name = 'target')
	date = models.DateField(auto_now_add=True)
	comment = models.CharField(max_length=300)
    
	def __unicode__(self):
		return '%s comments on %s' % (self.user1, self.user2)

	class Meta:
		unique_together = ('user1', 'user2','date')
#max 5 digit number and 2 decimal places

	

	
	
