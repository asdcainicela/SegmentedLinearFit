import logging
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot
import time

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)  # Cambiar a logging.INFO o logging.ERROR para menos detalle

class DataFrameModel(QAbstractTableModel):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self._df = df
        self._logged_values = set()  # Para evitar logs repetidos
        self._last_log_time = 0  # Control de tiempo para logs
        self._log_interval = 1.0  # Intervalo mínimo entre logs (segundos)
        logging.debug(f"Datos cargados:\n{self._df}")  # Registra los datos, pero no lo muestra en la interfaz

    def rowCount(self, parent=QModelIndex()):
        return len(self._df)

    def columnCount(self, parent=QModelIndex()):
        return len(self._df.columns)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid():
            return None
        if role == Qt.DisplayRole:
            # Asegúrate de acceder correctamente a la celda
            value = str(self._df.iloc[index.row(), index.column()])
            
            # Loguear solo una vez por valor
            log_key = f"data({index.row()}, {index.column()}): {value}"
            if log_key not in self._logged_values:
                logging.debug(f"Valor solicitado en ({index.row()}, {index.column()}): {value}")
                self._logged_values.add(log_key)
            
            return value
        return None

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return self._df.columns[section]
            else:
                return str(section + 1)
        return None

    @Slot(result=int)
    def rowCountQml(self):
        return self.rowCount()

    @Slot(result=int)
    def columnCountQml(self):
        return self.columnCount()

    @Slot(int, int, result=str)
    def value(self, row, column):
        try:
            # Obtener el valor usando iloc
            value = self._df.iloc[int(row), int(column)]
            
            # Controlar la frecuencia de logs
            current_time = time.time()
            if current_time - self._last_log_time > self._log_interval:
                # Registrar solo si ha pasado suficiente tiempo desde el último log
                logging.debug(f"Llamado a value con: fila={row}, columna={column}. Valor: {value}")
                self._last_log_time = current_time
                
            return str(value)
        except Exception as e:
            logging.error(f"Error accediendo a valor ({row}, {column}): {e}")
            return ""

    # Método para limpiar el caché de logs si es necesario
    def clearLogCache(self):
        self._logged_values.clear()