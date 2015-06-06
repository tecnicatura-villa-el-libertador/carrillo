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

$pip install -r requirements.txt

Ahora debemos clonar el proyecto, pero antes debemos crear un fork en github:

git clone "mi fork"

