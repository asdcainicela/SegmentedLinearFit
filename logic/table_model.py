import logging
from PySide6.QtCore import QAbstractTableModel, Qt, QModelIndex, Slot

# Configuración de logging
logging.basicConfig(level=logging.DEBUG)  # Cambiar a logging.INFO o logging.ERROR para menos detalle

class DataFrameModel(QAbstractTableModel):
    def __init__(self, df, parent=None):
        super().__init__(parent)
        self._df = df
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
            logging.debug(f"Valor solicitado en ({index.row()}, {index.column()}): {value}")  # Registra el valor accedido
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
            # Es importante usar exactamente el mismo método de acceso que en data()
            value = self._df.iloc[int(row), int(column)]
            logging.debug(f"Llamado a value con: fila={row}, columna={column}. Valor: {value}")
            return str(value)
        except Exception as e:
            logging.error(f"Error accediendo a valor ({row}, {column}): {e}")
            return ""