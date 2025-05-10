import sys
import os
from pathlib import Path
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

#Importar el módulo de lógica
from logic.open_csv import AppLogic_csv

def main():
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()

    # Crear una instancia de la lógica de la aplicación
    app_logic_csv = AppLogic_csv()
    # Conectar la lógica de la aplicación al motor QML
    engine.rootContext().setContextProperty("appLogic_csv", app_logic_csv)
    # Conectar señales de la lógica a funciones QML
    app_logic_csv.dataLoaded.connect(lambda msg: print(f"Mensaje desde lógica: {msg}"))
    app_logic_csv.previewUpdated.connect(lambda row, preview, total: print(f"Vista previa actualizada: {row}, {preview}, Total: {total}"))

    # Obtener la ruta absoluta al directorio actual
    current_dir = Path(__file__).resolve().parent

    # Importante: Registrar el directorio actual como ruta de importación QML
    engine.addImportPath(str(current_dir))

    # Cargar el archivo QML directamente desde el sistema de archivos
    main_qml_path = os.path.join(current_dir, "main.qml")
    print(f"Intentando cargar: {main_qml_path}")
    print(f"El archivo existe: {os.path.exists(main_qml_path)}")

    engine.load(QUrl.fromLocalFile(main_qml_path))

    if not engine.rootObjects():
        print("Error crítico: No se pudo cargar main.qml")
        return -1

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
