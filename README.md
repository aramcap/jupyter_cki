# jupyter_cki
## Jupyter Custom Kernel Installer

### English

This software can install more kernels in Jupyter (notebook, lab or hub).

Using the `ipykernel` utility, this software install a new kernel and after replace the path to correct Python environment. The major benefit of this is that you can have multiple Python environments (hand-managed or by software like Conda) with distinct libraries or packages, not merging the environments. It's very important that all environments has installed the Python package `ipykernel`.

#### Requirements:
- Python 2 or 3.
- Environments with package `ipykernel` installed.

#### Example:
We have a Conda installation on `/opt/conda` with three environments: 
- tools (environment where it has installed Jupyter)
- python35 (environment where it has installed packages that needs this version of Python)
- python36 (environment where it has installed packages that needs this version of Python)

/opt/conda/envs
|-- python35/
|-- python36/
`-- tools/

```bash
[root@vm /root/jupyter_cki] ll
-rw-r--r-- 1 root root 2334 Jan 18 00:00 jupyter_cki.py

[root@vm /root/jupyter_cki] python jupyter_cki.py /opt/conda/envs/tools python36 /opt/conda/envs/python36
Installed kernelspec python36 in /opt/conda/envs/tools/share/jupyter/kernels/python36

[root@vm /root/jupyter_cki] python jupyter_cki.py /opt/conda/envs/tools python35 /opt/conda/envs/python35
Installed kernelspec python35 in /opt/conda/envs/tools/share/jupyter/kernels/python35
```

You can check if it's working correctly: first open Jupyter, select a custom kernel and execute this to check the Python version running.
```py
import sys
print(sys.version)
```

#### Bug report:
If you have found a bug, please let me know with the [Issues tool](https://github.com/aramcap/jupyter_cki/issues) from GitHub.

#### License:
This software is distributed under GNU GPL v3. You can read the terms [here](https://github.com/aramcap/jupyter_cki/blob/master/LICENSE).

---

### Español

Este software permite instalar más kernels en Jupyter (notebook, lab o hub).

Usando la utilidad `ipykernel`, este software instala un nuevo kernel y luego reemplaza la ruta para corregir el entorno Python. El principal beneficio de esto es que puede tener múltiples entornos de Python (administrados manualmente o por software como Conda) con distintas bibliotecas o paquetes, sin fusionar los entornos. Es muy importante que todos los entornos tengan instalado el paquete Python `ipykernel`.

#### Requisitos:
- Python 2 o 3.
- Entornos con paquete `ipykernel` instalado.

#### Ejemplo:
Tenemos una instalación de Conda en `/opt/conda` con tres entornos:
- tools (entorno donde se ha instalado Jupyter).
- python35 (entorno donde han instalado paquetes que necesitan esta versión de Python)
- python36 (entorno donde han instalado paquetes que necesitan esta versión de Python)

/opt/conda/envs
|-- python35/
|-- python36/
`-- tools/

```bash
[root@vm /root/jupyter_cki] ll
-rw-r--r-- 1 root root 2334 Jan 18 00:00 jupyter_cki.py

[root@vm /root/jupyter_cki] python jupyter_cki.py /opt/conda/envs/tools python36 /opt/conda/envs/python36
Installed kernelspec python36 in /opt/conda/envs/tools/share/jupyter/kernels/python36

[root@vm /root/jupyter_cki] python jupyter_cki.py /opt/conda/envs/tools python35 /opt/conda/envs/python35
Installed kernelspec python35 in /opt/conda/envs/tools/share/jupyter/kernels/python35
```

Puedes verificar si está funcionando correctamente: primero abre Jupyter, selecciona un kernel personalizado y ejecuta esto para verificar la versión de Python que se está ejecutando.
```py
import sys
print(sys.version)
```

#### Reporte de errores:
Si has encontrado un error, házmelo saber con la [herramienta de errores](https://github.com/aramcap/jupyter_cki/issues) de GitHub.

#### Licencia:
Este software se distribuye bajo GNU GPL v3. Puedes leer los términos [aquí](https://github.com/aramcap/jupyter_cki/blob/master/LICENSE).