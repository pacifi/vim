[{'word': 'Bebida', 'menu': '[I]', 'kind': 'c', 'abbr': 'Bebida(models.Model): <class>'}, {'word': 'Comentario', 'menu': '[I]', 'kind': 'c', 'abbr': 'Comentario(models.Model): <class>'}, {'word': 'Receta', 'menu': '[I]', 'kind': 'c', 'abbr': 'Receta(models.Model): <class>'}, {'word': 'imagen', 'menu': 'Receta', 'kind': 'v', 'abbr': 'imagen = models.ImageField(upload_to=''recetas'', verbose_name=''Imagén'')'}, {'word': 'ingredientes', 'menu': 'Bebida', 'kind': 'v', 'abbr': 'ingredientes = models.TextField()'}, {'word': 'nombre', 'menu': 'Bebida', 'kind': 'v', 'abbr': 'nombre'}, {'word': 'preparacion', 'menu': 'Bebida', 'kind': 'v', 'abbr': 'preparacion = models.TextField()'}, {'word': 'receta', 'menu': 'Comentario', 'kind': 'v', 'abbr': 'receta = models.ForeignKey(Receta)'}, {'word': 'texto', 'menu': 'Comentario', 'kind': 'v', 'abbr': 'texto = models.TextField(help_text="Poner un comentario", verbose_name=''Comentario'')'}, {'word': 'tiempo_registro', 'menu': 'Receta', 'kind': 'v', 'abbr': 'tiempo_registro = models.DateTimeField(auto_now=True)'}, {'word': 'titulo', 'menu': 'Receta', 'kind': 'v', 'abbr': 'titulo'}, {'word': 'usuario', 'menu': 'Receta', 'kind': 'v', 'abbr': 'usuario = models.ForeignKey(User) # relacion de muchos a unoi'}]
