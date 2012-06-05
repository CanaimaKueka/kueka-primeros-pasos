#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup

files = ["data/*"]

setup(name = "canaima_primeros_pasos",
    version = "1.0",
    description = "Primeros pasos con Canaima GNU/Linux",
    author = "William Cabrera",
    author_email = "william@linux.es",
    url = "http://willicab.gnu.org.ve",
    license="GPLv3",
    packages = ['canaima_primeros_pasos'],
    package_data = {'canaima_primeros_pasos' : files },
    long_description = """Configura y asiste al usuario en sus primeras actividades con su distribución Canaima GNU/Linux, de acuerdo a ciertas reglas y condiciones, usa tasksel para instalar aplicaciones.""", 
    scripts = ["c-p-p"],
#    entry_points={
#      'console_scripts': [
#          'pasos = canaima_primeros_pasos.main:main'
#      ],
#    },
) 
