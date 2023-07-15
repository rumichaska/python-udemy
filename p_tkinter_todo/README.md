# Convertir a ejecutable

## Requerimientos

```python
pip3 install pyinstaller
```

## Resultados

Al ejecutar el comando `pyinstaller --onefile {nombre_aplicativo.py}` se crean
los archivos y directorios involucrados en crear un ejecutable del proyecto
elaborado con `TKinter`. El ejecutable se encuentra en la carpeta `dist/` y
tiene el mismo nombre que el archivo `.py`.
