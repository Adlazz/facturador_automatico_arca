#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script de entrada para ejecutar el facturador automático AFIP.
"""
import sys
import os

# Agregar el directorio src al path de Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.main import main

if __name__ == "__main__":
    main()
