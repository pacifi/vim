!_TAG_FILE_FORMAT	2	/extended format; --format=1 will not append ;" to lines/
!_TAG_FILE_SORTED	1	/0=unsorted, 1=sorted, 2=foldcase/
!_TAG_PROGRAM_AUTHOR	Darren Hiebert	/dhiebert@users.sourceforge.net/
!_TAG_PROGRAM_NAME	Exuberant Ctags	//
!_TAG_PROGRAM_URL	http://ctags.sourceforge.net	/official site/
!_TAG_PROGRAM_VERSION	5.9~svn20110310	//
Categoria	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^class Categoria(models.Model):$/;"	c
Item	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^class Item(models.Model):$/;"	c
LISTADO_TIPOS	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^LISTADO_TIPOS = ($/;"	v
categoria	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    categoria = models.ForeignKey(Categoria)$/;"	v	class:Item
default	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^                               default='T')$/;"	v	class:Item
departamento	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    departamento = models.CharField(max_length=255)$/;"	v	class:Item
descripcion	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    descripcion = models.TextField()$/;"	v	class:Item
listado	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    listado = models.CharField(max_length=1, choices=LISTADO_TIPOS,$/;"	v	class:Item
nombre	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    nombre = models.CharField(max_length=255)$/;"	v	class:Categoria
nombre	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    nombre = models.CharField(max_length=255)$/;"	v	class:Item
publicado_en	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    publicado_en = models.DateTimeField(auto_now_add=True)$/;"	v	class:Item
slug	/home/abel/proyectos/django/ut_tutorial/bevolist/models.py	/^    slug = models.SlugField(max_length=255, unique=True)$/;"	v	class:Categoria
