# El recetario

## Instalación
- instalar `poetry` ([poetry](https://python-poetry.org)). Poetry es el gestor de
  dependencias que usa este proyecto. Se encargará de instalar los programas
  necesarios. En nuestro caso, Pelican
  ([pelican](https://docs.getpelican.com/en/latest/)).
- Con poetry instalado, instalar las dependencias: `poetry install`.
- para ejectura comandos usar `poetry run python`, donde `python` es el comando
  de ejemplo. 

## Agregar nuevo contenido
- Crear un nuevo archivo en la carpeta `content/`
- Basarse en archivos existentes
- El formato de los archivos es markdown. Revisar [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) para más detalles.

## Revisar antes de publicar
- En la carpeta del proyecto ejecutar: `poetry run pelican -rl`
- Abrir el navegador para mirar el [sitio](http://localhost:8000).
- Mientras esté corriendo el comando, cualquier cambio se compilará
  automáticamente.

## Publicar
- `git pull` para obtener la última version del sitio
- Para agregar cambios (suponiendo que solo se agregaron cosas a `content/`:
  `git add content`
- `git commit -m "Agregar nueva receta <bla>"`. El texto entre comillas es el
  comentario del commit. Siempre agregar un comentario corto con el resumen de
  lo que se hizo.
- Finalmente: `git push`. Esto subirá los cambios, automáticamente el sitio se
  actualizará.

# TODO
1. páginas estáticas para autores
2. pensar en cómo darle una sección especial a completos
3. cómo publicar secciones generales? Guille tiene consideraciones generales
   para grupos de recetas.
