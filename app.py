import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Carga el modelo preentrenado YOLOv8
modelo = YOLO('yolov8n.pt')

def detectar_imagen(imagen):
    # Convierte la imagen de PIL a formato OpenCV
    imagen_cv = cv2.cvtColor(np.array(imagen), cv2.COLOR_RGB2BGR)

    # Ejecuta la deteccion
    resultados = modelo(imagen_cv, verbose=False)
    fotograma_anotado = resultados[0].plot()

    # Genera el resumen de detecciones
    detecciones = []
    for caja in resultados[0].boxes:
        clase = modelo.names[int(caja.cls)]
        confianza = float(caja.conf) * 100
        detecciones.append(f'{clase}: {confianza:.1f}%')

    resumen = '\n'.join(detecciones) if detecciones else 'No se detectaron objetos'

    # Convierte de vuelta a PIL para Gradio
    imagen_resultado = Image.fromarray(
        cv2.cvtColor(fotograma_anotado, cv2.COLOR_BGR2RGB)
    )

    return imagen_resultado, resumen

def detectar_video(ruta_video):
    if ruta_video is None:
        return None, 'No se subio ningun video'

    video = cv2.VideoCapture(ruta_video)
    ancho  = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    alto   = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps    = int(video.get(cv2.CAP_PROP_FPS))

    salida = 'resultado_video.mp4'
    escritor = cv2.VideoWriter(
        salida,
        cv2.VideoWriter_fourcc(*'mp4v'),
        fps,
        (ancho, alto)
    )

    total_detecciones = 0
    while True:
        ret, fotograma = video.read()
        if not ret:
            break
        resultados = modelo(fotograma, verbose=False)
        fotograma_anotado = resultados[0].plot()
        escritor.write(fotograma_anotado)
        total_detecciones += len(resultados[0].boxes)

    video.release()
    escritor.release()

    return salida, f'Total de detecciones en el video: {total_detecciones}'

# Interfaz Gradio
with gr.Blocks(title='Detector de Objetos') as interfaz:
    gr.Markdown('# Detector de Objetos con YOLOv8')
    gr.Markdown('Sube una imagen o video para detectar objetos automaticamente')

    with gr.Tab('Imagen'):
        with gr.Row():
            entrada_imagen = gr.Image(type='pil', label='Imagen de entrada')
            salida_imagen  = gr.Image(type='pil', label='Resultado')
        salida_texto = gr.Textbox(label='Objetos detectados')
        boton_imagen = gr.Button('Detectar')
        boton_imagen.click(
            fn=detectar_imagen,
            inputs=entrada_imagen,
            outputs=[salida_imagen, salida_texto]
        )

    with gr.Tab('Video'):
        entrada_video = gr.Video(label='Video de entrada')
        salida_video  = gr.Video(label='Resultado')
        salida_texto_video = gr.Textbox(label='Resumen')
        boton_video = gr.Button('Detectar')
        boton_video.click(
            fn=detectar_video,
            inputs=entrada_video,
            outputs=[salida_video, salida_texto_video]
        )

interfaz.launch()