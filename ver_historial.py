import csv
import os
from collections import Counter
from datetime import datetime

# Archivo de historial
ARCHIVO_HISTORIAL = 'historial_detecciones.csv'

def ver_historial():
    if not os.path.exists(ARCHIVO_HISTORIAL):
        print('No hay historial de detecciones todavia.')
        print('Ejecuta detectar_camara.py para generar el historial.')
        return

    detecciones = []
    with open(ARCHIVO_HISTORIAL, 'r', encoding='utf-8') as f:
        lector = csv.DictReader(f)
        for fila in lector:
            detecciones.append(fila)

    if not detecciones:
        print('El historial esta vacio.')
        return

    print(f'\nTotal de registros: {len(detecciones)}')
    print(f'Primer registro: {detecciones[0]["fecha"]} {detecciones[0]["hora"]}')
    print(f'Ultimo registro: {detecciones[-1]["fecha"]} {detecciones[-1]["hora"]}')

    # Conteo total por objeto
    conteo = Counter([d['objeto'] for d in detecciones])
    print('\nObjetos mas detectados:')
    for objeto, cantidad in conteo.most_common(10):
        print(f'  {objeto}: {cantidad} veces')

    # Detecciones por fecha
    fechas = Counter([d['fecha'] for d in detecciones])
    print('\nDetecciones por fecha:')
    for fecha, cantidad in sorted(fechas.items()):
        print(f'  {fecha}: {cantidad} registros')

if __name__ == '__main__':
    ver_historial()