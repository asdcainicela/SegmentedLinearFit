import sys
import os
from pathlib import Path
from PySide6.QtCore import QUrl, QResource
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

# Importar el módulo de lógica
from logic.open_csv import AppLogic_csv
from logic.table_model import DataFrameModel

import qml_rc   
def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Crear una instancia de la lógica de la aplicación
    app_logic_csv = AppLogic_csv()

    # Ruta al archivo CSV (ajústala a la ubicación correcta)
    csv_file_path = "ruta/a/tu/archivo.csv"  # Asegúrate de que sea la ruta correcta

    # Cargar el CSV pasando la ruta al método
    app_logic_csv.load_csv(csv_file_path)  # Pasa la ruta del archivo CSV

    # Conectar la lógica de la aplicación al motor QML
    engine.rootContext().setContextProperty("appLogic_csv", app_logic_csv)
    engine.rootContext().setContextProperty("tableModel", app_logic_csv.tableModel)  # Usar tableModel de appLogic_csv

    # Conectar señales de la lógica a funciones QML
    app_logic_csv.dataLoaded.connect(lambda msg: print(f"Mensaje desde lógica: {msg}"))
    app_logic_csv.previewUpdated.connect(lambda row, preview, total: print(f"Vista previa actualizada: {row}, {preview}, Total: {total}"))

    # Obtener la ruta absoluta al directorio actual
    current_dir = Path(__file__).resolve().parent

    # Importante: Registrar los recursos QML empaquetados si estamos ejecutando desde el ejecutable
    if getattr(sys, 'frozen', False):  # Si el script se está ejecutando desde un ejecutable generado por PyInstaller
        QResource.registerResource('qml_rc.py')  # Registra los recursos empaquetados
        main_qml_path = ':/main.qml'  # Ruta de los recursos empaquetados
    else:
        main_qml_path = os.path.join(current_dir, "main.qml")  # Ruta relativa para desarrollo

    print(f"Intentando cargar: {main_qml_path}")
    print(f"El archivo existe: {os.path.exists(main_qml_path)}")

    # Cargar el archivo QML
    engine.load(QUrl.fromLocalFile(main_qml_path))

    if not engine.rootObjects():
        print("Error crítico: No se pudo cargar main.qml")
        return -1

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
