Proyecto Carrillo
==================

Médicas y médicos de la ciudad de Córdoba realizan cada año un trabajo de relevamiento de campo en el marco de su residencias en el Hospital Príncipe de Asturias del barrio Villa del Libertador, bajo la tutela de la cátedra de Salud Pública de la carrera de Medicina de la UNC.

Este relevamiento, realizado a través de encuestas en los hogares de la zona objetivo (a priori, la zona sur de córdoba), permite recabar métricas sobre la salud de la población, correlacionarlos con índices de calidad habitacional, nivel educativo, y muchos otros indicadores que permiten diseñar intervenciones y campañas especiales desde los centros de salud de la zona.

Actualmente utilizan un sistema muy precario de base de datos, que luego personal técnico exporta a formato excel para realizar el ánalisis cuantitativo, introduciendo muchos errores de análisis en el proceso y dificultando comparaciones pre y post intervención.

Desde la cátedra Práctica Profesionalizante II de la carrera de Técnico Superior en Desarrollo de Software (Instituto Superior Córdoba) que funciona en el propio barrio, asumimos este desafío como nuestro proyecto anual, incluyendo el rediseño y mejora de este sistema, facilitando no sólo la carga de datos sino la generación de reportes automatizados.

Aprovechamos la jornada del "Hackatong" no sólo para utilizarla como una jornada de trabajo intensivo (e invitando a cualquiera que quiera colaborar con este loable proyecto), sino para conocer y vincularnos, como docentes y estudiantes de la tecnicatura en software, con el resto de la activa comunidad IT de nuestra ciudad.

Instalar
---------

En windows, usar Conda


Para comenzar a usar el sistema debe crear un entorno virtual. Pero primero debe ejecutar:

$ sudo apt-get install python3.4-dev

despues crear la carpeta:

$mkdir carrillo
$cd carrillo

Despues para crear el esntorno:

$pyvenv-3.4 --without-pip .

$source bin/activate

$curl https://bootstrap.pypa.io/get-pip.py | python

$deactivate

$source bin/activate

Despues para instalar los necesario:

$ pip install -r requirements.txt

Ahora debemos clonar el proyecto, pero antes debemos crear un fork en github:

`git clone "mi fork"`



