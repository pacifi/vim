!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
Category	/home/abel/proyectos/django/crud/people/models.py	/^class Category(models.Model):$/;"	c
Meta	/home/abel/proyectos/django/crud/people/models.py	/^    class Meta:$/;"	c	class:Category
Meta	/home/abel/proyectos/django/crud/people/models.py	/^    class Meta:$/;"	c	class:Person
PROXIMITY_LIST	/home/abel/proyectos/django/crud/people/models.py	/^    PROXIMITY_LIST = ($/;"	v	class:Person
Person	/home/abel/proyectos/django/crud/people/models.py	/^class Person(models.Model):$/;"	c
__unicode__	/home/abel/proyectos/django/crud/people/models.py	/^    def __unicode__(self):$/;"	m	class:Category	file:
__unicode__	/home/abel/proyectos/django/crud/people/models.py	/^    def __unicode__(self):$/;"	m	class:Person	file:
added_on	/home/abel/proyectos/django/crud/people/models.py	/^    added_on = models.DateField(auto_now_add=True)$/;"	v	class:Person
category	/home/abel/proyectos/django/crud/people/models.py	/^    category = models.ForeignKey(Category, blank=True, null=True, help_text='File this person where?')$/;"	v	class:Person
cell_phone	/home/abel/proyectos/django/crud/people/models.py	/^    cell_phone = PhoneNumberField(blank=True)$/;"	v	class:Person
email	/home/abel/proyectos/django/crud/people/models.py	/^    email = models.EmailField(blank=True, help_text='Do they have an Email address?')$/;"	v	class:Person
first_name	/home/abel/proyectos/django/crud/people/models.py	/^    first_name = models.CharField(max_length=60, help_text='Their first name')$/;"	v	class:Person
full_name	/home/abel/proyectos/django/crud/people/models.py	/^    def full_name(self):$/;"	m	class:Person
get_absolute_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_absolute_url(self):$/;"	m	class:Category
get_absolute_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_absolute_url(self):$/;"	m	class:Person
get_delete_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_delete_url(self):$/;"	m	class:Category
get_delete_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_delete_url(self):$/;"	m	class:Person
get_update_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_update_url(self):$/;"	m	class:Category
get_update_url	/home/abel/proyectos/django/crud/people/models.py	/^    def get_update_url(self):$/;"	m	class:Person
home_phone	/home/abel/proyectos/django/crud/people/models.py	/^    home_phone = PhoneNumberField(blank=True)$/;"	v	class:Person
last_name	/home/abel/proyectos/django/crud/people/models.py	/^    last_name = models.CharField(max_length=80, blank=True, help_text='Do you know it?')$/;"	v	class:Person
ordering	/home/abel/proyectos/django/crud/people/models.py	/^        ordering = ['last_name']$/;"	v	class:Person.Meta
proximity	/home/abel/proyectos/django/crud/people/models.py	/^    proximity = models.PositiveSmallIntegerField(choices=PROXIMITY_LIST, help_text='How much of a distance to keep?')$/;"	v	class:Person
save	/home/abel/proyectos/django/crud/people/models.py	/^    def save(self, *args, **kwargs):$/;"	m	class:Category
save	/home/abel/proyectos/django/crud/people/models.py	/^    def save(self, *args, **kwargs):$/;"	m	class:Person
slug	/home/abel/proyectos/django/crud/people/models.py	/^    slug = models.SlugField(blank=True)$/;"	v	class:Category
slug	/home/abel/proyectos/django/crud/people/models.py	/^    slug = models.SlugField(blank=True)$/;"	v	class:Person
title	/home/abel/proyectos/django/crud/people/models.py	/^    title = models.CharField(max_length=80)$/;"	v	class:Category
verbose_name_plural	/home/abel/proyectos/django/crud/people/models.py	/^        verbose_name_plural = 'categories'$/;"	v	class:Category.Meta
verbose_name_plural	/home/abel/proyectos/django/crud/people/models.py	/^        verbose_name_plural = 'people'$/;"	v	class:Person.Meta
