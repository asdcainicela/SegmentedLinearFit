#open_csv.py
from PySide6.QtCore import QObject, Slot, Signal, Property
import pandas as pd
from .table_model import DataFrameModel

class AppLogic_csv(QObject):
    dataLoaded = Signal(str)  # Para confirmar carga o error
    previewUpdated = Signal(str, str, str)  # index, content, total

    def __init__(self):
        super().__init__()
        self.df = None
        self.current_row = 0
        self._model = None  # <--- NECESARIO para inicializar

    @Slot(str)
    def load_csv(self, filepath):
        """ Carga el archivo CSV y actualiza la vista previa """
        try:
            self.df = pd.read_csv(filepath)
            self._model = DataFrameModel(self.df)  # <--- Instanciar modelo para tabla
            self.current_row = 0
            self.update_preview()
            self.dataLoaded.emit("CSV cargado correctamente.")
        except Exception as e:
            self.dataLoaded.emit(f"Error al cargar: {str(e)}")

    def update_preview(self):
        """ Actualiza la vista previa mostrando la fila actual """
        if self.df is not None:
            row = self.df.iloc[self.current_row]
            preview = f"Fila {self.current_row + 1}:\n" + "\n".join([f"{col}: {row[col]}" for col in self.df.columns])
            self.previewUpdated.emit(str(self.current_row + 1), preview, str(len(self.df)))

    @Slot()
    def next_row(self):
        if self.df is not None and self.current_row < len(self.df) - 1:
            self.current_row += 1
            self.update_preview()

    @Slot()
    def previous_row(self):
        if self.df is not None and self.current_row > 0:
            self.current_row -= 1
            self.update_preview()

    @Property(QObject, constant=True)
    def tableModel(self):
        return self._model
