from django.db import models

class Author(models.Model):
	first_name = models.CharField(max_length=100)

	last_name = models.CharField(max_length=100)

	date_birth = models.DateField(blank=True, null=True)

	date_death = models.DateField(blank=True, null=True)

	GENDER = [
		('M', 'Male'),
		('F', 'Female'),
		('UK', 'Unknown')
	]

	gender = models.CharField(max_length=15,default='UK', choices=GENDER)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Translator(models.Model):
	first_name = models.CharField(max_length=100)

	last_name = models.CharField(max_length=100)

	def __str__(self):
		return self.first_name + ' ' + self.last_name

class Text(models.Model):

	title = models.CharField(max_length=100)

	author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='texts', blank=True, null=True)

	publication_date = models.DateField(blank=True, null=True)

	GENRE = [
		('P', 'Poetry'),
		('F', 'Fiction'),
		('NF', 'Non-Fiction'),
	]

	TIME_PERIOD = [
		('CLS', "The Classical Period (1200 BCE-455 CE)"),
		('MED', "The Medieval Period (455-1485 CE)"),
		('REN', "The Renaissance and Reformation (1485-1660)"),
		("ENL", "The Englightenment (1660-1790)"),
		("ROM", 'The Romantic Period (1790-1830)'),
		("VIC", "The Victorian Period (1832-1901"),
		('MOD', "The Modern Period (1914-1945)"),
		("PM", "The PostModern Period (1945-Present Day)"),
		('UNK', 'Unknown')

	]

	time_period = models.CharField(max_length=50, choices=TIME_PERIOD, default='UNK')

	genre = models.CharField(max_length=100, choices=GENRE, default='F')

	translation = models.BooleanField(default=False)

	translator = models.ManyToManyField(Translator, blank=True, related_name='texts')

	txt_file = models.FileField(upload_to='text_files', blank=True, null=True)

	def __str__(self):
		return self.title
