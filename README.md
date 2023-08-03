# H1 Universidad Nacional de San Luis

## H2 Argentina Programa

### H3 Sistema de Inscripción a Exámenes

## H2 Narrativa

Una institución educativa de nivel medio requiere automatizar las inscripciones de los alumnos que
tienen que rendir materias previas, libres y equivalencias. Los exámenes están dirigidos a aquellos
estudiantes que no aprobaron una materia de años anteriores, no tuvieron la materia dado provienen
de otra institución o tuvieron la materia pero con contenido diferente. Las fechas de los exámenes
son establecidas por el Ministerio de Educación. Los alumnos que deseen rendir una materia deben
realizar la inscripción correspondiente. Una vez que los estudiantes rinden los profesores colocan
las notas en un acta de alumnos previos libres y equivalentes.
Luego de explicada la realidad se pide construir un sistema que permita:

1. Que los encargados de realizar las inscripciones de los alumnos que rinden materias previas,
   libres o una equivalencias puedan inscribir estudiantes. Los inscriptos se almacenan en un
   archivo de texto cuyo nombre es Inscripciones.txt. La inscripción registra fecha, nombre del
   estudiante, nombre de la materia, nombre del profesor, curso, división y la nota obtenida
   (este valor inicialmente es -1). Cada campo está separado por una coma. A modo de ejemplo
   se presentan dos líneas del archivo de texto antes mencionado:
   3/04/23, Juan Perez,Educación Tecnológica, Humberto Fidalgo, 4,A,-1
   3/04/23, Carlos Quiroga,Geografía, Felipe Nievas, 3,A,-1
2. Que el profesor cargue las notas de los estudiantes que rindieron el examen de la/s materia/s
   que dicta.

### H3 Características del Sistema

3. Solo los profesores y encargados institucionales pueden acceder al sistema. El ingreso se
   realiza de la siguiente manera:
4. Profesores: coloca el nombre del profesor, materia, curso y división.
5. Encargados: coloca nombre y dni.
   En ambos casos cuando la validación de datos no es exitosa el sistema muestra un error y
   vuelve a pedir los datos.
6. Los profesores de la institución se encuentran almacenados en un archivo de texto
   Profesores.txt. Dicho archivo registra el nombre del profesor, la materia que dicta, el curso y
   la división. Todos los campos están separados por coma. Este archivo es proporcionado por
   la institución y se utiliza para permitir el acceso al sistema a los profesores.
7. Los encargados institucionales de realizar las inscripciones a los exámenes se encuentran
   almacenados en el archivo Encargados.txt. El archivo registra el nombre del empleado y el
   dni. Todos los campos están separados por coma. Este archivo es proporcionado por la
   institución y se utiliza para permitir el acceso a los encargados.
8. Tanto para las inscripciones como para la carga de notas se debe dar la posibilidad de
   eliminar y modificar los datos.
9. El sistema debe presentar las diferentes tareas a través de un menú de opciones
