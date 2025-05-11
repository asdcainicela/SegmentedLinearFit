# logic/analyzer.py
import numpy as np
import pandas as pd
from scipy.stats import linregress

def prioridadErr(secuencia):
    max_consecutivos = 0
    consecutivos_actuales = 0
    for elemento in secuencia:
        if elemento == 1:
            consecutivos_actuales += 1
            max_consecutivos = max(max_consecutivos, consecutivos_actuales)
        else:
            consecutivos_actuales = 0
    return max_consecutivos

def analizar_csv(filepath):
    # 1. Cargar el CSV
    df = pd.read_csv(filepath)

    if df.shape[1] < 2:
        raise ValueError("El archivo debe tener al menos dos columnas.")

    # Tomar la primera y segunda columna sin importar sus nombres
    x_datos = df.iloc[:, 0].tolist()  # primera columna → input
    y_datos = df.iloc[:, 1].tolist()  # segunda columna → output

    x_datos_ = np.copy(x_datos)
    y_datos_ = np.copy(y_datos)

    # 2. Configuración de errores
    errAbsMax = 0.01 * np.abs(np.max(y_datos)) / 100
    errAbsMax_Comprobar = 0.2 * np.abs(np.max(y_datos)) / 100

    minPoint = 3
    despValores = []
    errAcumuladoAbs = []

    while len(x_datos_) > minPoint:
        errAcumuladoSecuencia = []
        r_cuadrado = []
        for i in range(minPoint, len(x_datos_) + 1):
            pendiente, intercepto, r_valor, _, _ = linregress(x_datos_[0:i], y_datos_[0:i])
            for ii in range(0, i):
                pred = pendiente * x_datos_[ii] + intercepto
                error = np.abs(pred - y_datos_[ii])
                errAcumuladoAbs.append(1 if error < errAbsMax else 0)
            errAcumuladoSecuencia.append(errAcumuladoAbs)
            r_cuadrado.append(r_valor ** 2)
            errAcumuladoAbs = []

        mejor_pos, secuencia = max(enumerate(errAcumuladoSecuencia), key=lambda x: prioridadErr(x[1]))
        pos_r2 = np.argmax(r_cuadrado) + minPoint - 1
        mejor_pos = mejor_pos + minPoint - 1

        posicionFinal = pos_r2 if pos_r2 < mejor_pos else mejor_pos
        despValores.append(posicionFinal)

        x_datos_ = np.roll(x_datos_, shift=-posicionFinal)[:len(x_datos_) - posicionFinal]
        y_datos_ = np.roll(y_datos_, shift=-posicionFinal)[:len(y_datos_) - posicionFinal]

        if 1 < len(x_datos_) <= minPoint:
            despValores.append(len(x_datos_))
            break

    # 3. Construcción de segmentos y regresiones
    x_Nuevo = []
    y_Nuevo = []
    m_val_ = []
    b_val_ = []
    eqs = []

    despMin = 0
    despMax = 0

    for i in range(len(despValores)):
        despMax += despValores[i]
        x_seg = x_datos[despMin:despMax+1]
        y_seg = y_datos[despMin:despMax+1]

        if len(x_seg) < 2:
            continue

        m, b, _, _, _ = linregress(x_seg, y_seg)
        m_val_.append(m)
        b_val_.append(b)
        x_Nuevo.append(x_seg)
        y_Nuevo.append(y_seg)

        # Crear la ecuación en string con 7 decimales
        eq_str = f"y = {m:.7f} * x + {b:.7f}"
        eqs.append(eq_str)

        despMin = despMax + 1

    eqs_plain  = []
    eqs_latex  = []

    for i in range(len(despValores)):
        ...
        eq_plain  = f"OUT = {m:.7f} · IN + {b:.7f}"
        eq_latex  = f"\\(\\text{{OUT}} = {m:.7f}\\,\\text{{IN}} + {b:.7f}\\)"
        eqs_plain.append(eq_plain)
        eqs_latex.append(eq_latex)

    return {
        "tramos"     : len(eqs_plain),
        "ecuaciones" : eqs_plain,
        "ecuacionesLatex": eqs_latex
    }

