# jupyter_cki
## Jupyter Custom Kernel Installer

### English

This software can install Python and R kernels in Jupyter (notebook, lab or hub).

This software, that uses the `ipykernel` utility for Python kernels and `r-irkernel` for R kernels, installs a new kernel for Jupyter. With this you can have multiple kernels (hand-managed or by software like Conda) with distinct libraries or packages, not merging the environments.

#### Requirements:
- Python 2 or 3.
- Environment with package `ipykernel` or `r-irkernel` installed.

#### Example:
We have a Conda installation on `/opt/conda` with three environments: 
- jupyterhub
- python35
- python36
- ir

```
/opt/conda/envs
|-- python35/
|-- python36/
|-- ir/
`-- jupyterhub/
```

```bash
[root@vm /root/jupyter_cki] python jupyter_cki.py python --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/python36 --kernel_name python36
Installed kernelspec python36 in /opt/conda/envs/tools/share/jupyter/kernels/python36
Kernel installed

[root@vm /root/jupyter_cki] python jupyter_cki.py python --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/python35 --kernel_name python35
Installed kernelspec python35 in /opt/conda/envs/tools/share/jupyter/kernels/python35
Kernel installed

[root@vm /root/jupyter_cki] python jupyter_cki.py ir --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/ir
Kernel installed
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

Este software permite instalar más kernels de Python o R en Jupyter (notebook, lab o hub).

Este software, que usa la utilidad `ipykernel` para núcleos Python y `r-irkernel` para núcleos R, instala un nuevo kernel para Jupyter. Con esto puede tener múltiples núcleos (administrados manualmente o por software como Conda) con distintas bibliotecas o paquetes, sin fusionar los entornos.

#### Requisitos:
- Python 2 o 3.
- Entorno con paquete `ipykernel`  o `r-irkernel` instalado.

#### Ejemplo:
Tenemos una instalación de Conda en `/opt/conda` con tres entornos:
- jupyterhub
- python35
- python36
- ir

```
/opt/conda/envs
|-- python35/
|-- python36/
|-- ir/
`-- jupyterhub/
```

```bash
[root@vm /root/jupyter_cki] python jupyter_cki.py python --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/python36 --kernel_name python36
Installed kernelspec python36 in /opt/conda/envs/tools/share/jupyter/kernels/python36
Kernel installed

[root@vm /root/jupyter_cki] python jupyter_cki.py python --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/python35 --kernel_name python35
Installed kernelspec python35 in /opt/conda/envs/tools/share/jupyter/kernels/python35
Kernel installed

[root@vm /root/jupyter_cki] python jupyter_cki.py ir --jupyter /opt/conda/envs/jupyterhub --kernel /opt/conda/envs/ir
Kernel installed
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