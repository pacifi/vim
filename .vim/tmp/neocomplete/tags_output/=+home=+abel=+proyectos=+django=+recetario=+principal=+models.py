!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
Bebida	/home/abel/proyectos/django/recetario/principal/models.py	/^class Bebida(models.Model):$/;"	c
Comentario	/home/abel/proyectos/django/recetario/principal/models.py	/^class Comentario(models.Model):$/;"	c
Receta	/home/abel/proyectos/django/recetario/principal/models.py	/^class Receta(models.Model):$/;"	c
__unicode__	/home/abel/proyectos/django/recetario/principal/models.py	/^    def __unicode__(self):$/;"	m	class:Bebida	file:
__unicode__	/home/abel/proyectos/django/recetario/principal/models.py	/^    def __unicode__(self):$/;"	m	class:Comentario	file:
__unicode__	/home/abel/proyectos/django/recetario/principal/models.py	/^    def __unicode__(self):$/;"	m	class:Receta	file:
imagen	/home/abel/proyectos/django/recetario/principal/models.py	/^    imagen = models.ImageField(upload_to='recetas', verbose_name='Imagén')$/;"	v	class:Receta
ingredientes	/home/abel/proyectos/django/recetario/principal/models.py	/^    ingredientes = models.TextField()$/;"	v	class:Bebida
ingredientes	/home/abel/proyectos/django/recetario/principal/models.py	/^    ingredientes = models.TextField(help_text="Redacta los ingredientes")$/;"	v	class:Receta
nombre	/home/abel/proyectos/django/recetario/principal/models.py	/^    nombre = models.CharField(max_length=50)$/;"	v	class:Bebida
preparacion	/home/abel/proyectos/django/recetario/principal/models.py	/^    preparacion = models.TextField()$/;"	v	class:Bebida
preparacion	/home/abel/proyectos/django/recetario/principal/models.py	/^    preparacion = models.TextField(verbose_name='Preparación')$/;"	v	class:Receta
receta	/home/abel/proyectos/django/recetario/principal/models.py	/^    receta = models.ForeignKey(Receta)$/;"	v	class:Comentario
texto	/home/abel/proyectos/django/recetario/principal/models.py	/^    texto = models.TextField(help_text="Poner un comentario", verbose_name='Comentario')$/;"	v	class:Comentario
tiempo_registro	/home/abel/proyectos/django/recetario/principal/models.py	/^    tiempo_registro = models.DateTimeField(auto_now=True)$/;"	v	class:Receta
titulo	/home/abel/proyectos/django/recetario/principal/models.py	/^    titulo = models.CharField(max_length=100, unique=True)$/;"	v	class:Receta
usuario	/home/abel/proyectos/django/recetario/principal/models.py	/^    usuario = models.ForeignKey(User) # relacion de muchos a unoi$/;"	v	class:Receta
