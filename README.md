# Introducción a la Visualización Científica con Python

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/nicoguaro/taller_scivis-2025/HEAD)

Este es el repositorio del taller de visualización científica para los
estudiantes del grupo de investigación en Aplicaciones Matemáticas en Ciencia
e Ingeniería de la Universidad EAFIT de 2025.

<img src="./img/heat_smiley.gif"
    alt="Solución de la ecuación de calor."
    width=400>

La animación anterior presenta una visualización de la transferencia de calor
en una placa con una temperatura fija en los bordes a cero grados y una
distribución de temperatura inicial con forma de carita feliz. Si esperamos lo
suficiente, la solución debería converger a un estado estacionario de cero
grados en todo el dominio. La animación se puede reproducir ejecutando el
ejemplo proporcionado en
``./code/heat_iteration.py``, por ejemplo

    python heat_iteration.py


**Contenido**

 1. [Instalación](#instrucciones-de-instalación)
 2. [Instalación opcional](#instalación-opcional)
 3. [Verificando la installación](#verificando-la-instalación)
 4. [Licencia](#licencia)


## Instrucciones de instalación

Recomendamos usar ``conda`` para instalar los paquetes necesarios para este
taller. Se requieren dependencias ajenas a Python, lo que hace que la
instalación manual o con ``pip`` un poco compleja.


Cree un entorno conda usando el archivo ``environment.yml`` en la raíz del
repositorio usando

```console
conda env create -f environment.yml
```

Esto creará un ambiente de conda llamado `scivis-2025` con todos los paquetes
necesarios.

Puedes activar el ambiente con

```console
conda activate scivis-2025
```

## Instalación opcional

### ParaView

También hablaremos de ParaView como plataforma de visualización. El método de
instalación sugerido es descargar el paquete para su sistema operativo desde
el sitio web oficial (https://www.paraview.org/download/).

## Verificando la instalación

Tras la instalación, puede comprobar si todo está instalado.

```console
python check_install.py
```

Para comprobar si todo funciona, ejecute las demostraciones con

```console
python demo.py
```

## Licencia

Todo el código está bajo la licencia MIT y los medios de comunicación bajo la
licencia Creative Commons Attribution.

El contenido de este repositorio está bajo la licencia
[Creative Commons Attribution 4.0](http://choosealicense.com/licenses/cc-by-4.0/),
y el código fuente que lo acompaña está bajo la
[licencia MIT](https://opensource.org/licenses/mit-license.php).
