<div align="right">
  <img src="https://img.shields.io/badge/PJ-Pablo%20Jim%C3%A9nez-black?style=for-the-badge" alt="PJ"/>
</div>

# Detector de Objetos con YOLOv8

![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square&logo=python)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-purple?style=flat-square)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0-green?style=flat-square)
![Gradio](https://img.shields.io/badge/Gradio-UI-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

Detector de objetos en tiempo real usando YOLOv8, con soporte para camara en vivo, imagenes estaticas y videos. Incluye interfaz web con Gradio para clasificar desde el navegador sin instalar nada.


## Que resuelve

Detecta y clasifica automaticamente objetos en tiempo real desde la camara, en imagenes o en videos, dibujando recuadros con etiquetas y niveles de confianza sobre cada objeto detectado.

---

## Modos de uso

Camara en tiempo real: detecta objetos desde la webcam en vivo
Imagen: sube una imagen y detecta todos los objetos presentes
Video: procesa un video completo y genera uno nuevo con las detecciones

---

## Tecnologias

Python 3.12: Lenguaje principal — https://python.org
YOLOv8: Modelo de deteccion de objetos — https://ultralytics.com
OpenCV: Procesamiento de imagenes y video — https://opencv.org
Gradio: Interfaz web — https://gradio.app
Pillow: Manejo de imagenes — https://python-pillow.org

## Instalacion

Clona el repositorio con: 'git clone https://github.com/pablojimenez23/detector-objetos.git'

Entra a la carpeta con: 'cd detector-objetos'

Instala las dependencias con: 'pip install -r requirements.txt'


## Ejemplos de uso

Deteccion en tiempo real con la camara: `python detectar_camara.py`

Presiona Q para salir.

Deteccion en una imagen: 'python detectar_imagen.py ruta/imagen.jpg'

Imagen: ruta/imagen.jpg
Objetos detectados: 3
  person: 98.2%
  car: 94.5%
  dog: 87.3%

Resultado guardado en: resultado_imagen.jpg

Deteccion en un video: 'python detectar_video.py ruta/video.mp4'

Procesando video: ruta/video.mp4
Total de fotogramas: 300
Fotograma 30/300
Fotograma 60/300
---
Video guardado en: resultado_video.mp4

Interfaz web: 'python app.py'

Abre el navegador en: http://localhost:7860

---

## Decisiones de diseno

YOLOv8n: Se uso la version nano por su velocidad en tiempo real. Para mayor precision se puede cambiar a yolov8s, yolov8m o yolov8l.

Gradio: Permite crear una interfaz web funcional en pocas lineas de codigo, ideal para demostraciones rapidas sin necesidad de frontend separado.

---

## Proximas mejoras

Despliegue en AWS EC2
Soporte para deteccion en streams de video online
Entrenamiento con clases personalizadas
Integracion con el clasificador de residuos

---

## Como contribuir

Haz fork del repositorio, crea una rama con: 'git checkout -b feature/nombre-mejora', realiza tus cambios y abre un Pull Request describiendo lo que hiciste.


## Autor

Pablo Jimenez — Ingeniero en Informatica
GitHub: https://github.com/pablojimenez23
Kaggle: https://www.kaggle.com/pablandjf
