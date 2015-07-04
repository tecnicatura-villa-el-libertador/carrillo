Para comenzar a usar el sistema debe crear un entorno virtual. Pero primero debe ejecutar:

$ sudo apt-get install python3.4-dev

Ahora debemos clonar el proyecto, pero antes debemos crear un fork en github:

git clone "link_mi_fork"

Posicionarse dentro del proyecto clonado
$cd carrillo

Despues para crear el entorno:

$pyvenv-3.4 --without-pip nombre_entorno
$cd nombre_entorno
$source bin/activate

$curl https://bootstrap.pypa.io/get-pip.py | python

$deactivate

$source bin/activate

Regresamos al directorio anterior
$cd ..

Despues para instalar lo necesario:

$pip install -r carrillo/requirements.txt

Por último, agregar el repositorio de la tecnicatura:

$git remote add tecnicatura "link_repo_tecnicatura"

Por último, posicionarse dentro de carrillo:

$cd carrillo

Listo!!


