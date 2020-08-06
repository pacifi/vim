!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
Categoria	/home/abel/proyectos/django/proyecto/ads/models.py	/^class Categoria(models.Model):$/;"	c
Elemento	/home/abel/proyectos/django/proyecto/ads/models.py	/^class Elemento(models.Model):$/;"	c
Fotografia	/home/abel/proyectos/django/proyecto/ads/models.py	/^class Fotografia(models.Model):$/;"	c
TIPO_ANUNCIO	/home/abel/proyectos/django/proyecto/ads/models.py	/^TIPO_ANUNCIO =($/;"	v
anuncio	/home/abel/proyectos/django/proyecto/ads/models.py	/^    anuncio = models.CharField(max_length=1, choices=TIPO_ANUNCIO, default='O')$/;"	v	class:Elemento
categoria	/home/abel/proyectos/django/proyecto/ads/models.py	/^    categoria = models.ForeignKey(Categoria)$/;"	v	class:Elemento
descripcion	/home/abel/proyectos/django/proyecto/ads/models.py	/^    descripcion = models.TextField()$/;"	v	class:Elemento
elemento	/home/abel/proyectos/django/proyecto/ads/models.py	/^    elemento = models.ForeignKey(Elemento)$/;"	v	class:Fotografia
nombre	/home/abel/proyectos/django/proyecto/ads/models.py	/^    nombre = models.CharField(max_length=255)$/;"	v	class:Categoria
nombre	/home/abel/proyectos/django/proyecto/ads/models.py	/^    nombre = models.CharField(max_length=255)$/;"	v	class:Elemento
publicado_en	/home/abel/proyectos/django/proyecto/ads/models.py	/^    publicado_en = models.DateTimeField(auto_now_add=True)$/;"	v	class:Elemento
seccion	/home/abel/proyectos/django/proyecto/ads/models.py	/^    seccion = models.CharField(max_length=255)$/;"	v	class:Elemento
slug	/home/abel/proyectos/django/proyecto/ads/models.py	/^    slug = models.SlugField(max_length=255, unique=True)$/;"	v	class:Categoria
url	/home/abel/proyectos/django/proyecto/ads/models.py	/^    url = models.CharField(max_length=255)$/;"	v	class:Fotografia
