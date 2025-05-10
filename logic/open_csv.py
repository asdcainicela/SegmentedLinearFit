from PySide6.QtCore import QObject, Slot, Signal
import pandas as pd

class AppLogic_csv(QObject):
    dataLoaded = Signal(str)  # Para confirmar carga o error
    previewUpdated = Signal(str, str, str)  # Para actualizar la vista previa de datos

    def __init__(self):
        super().__init__()
        self.df = None
        self.current_row = 0

    @Slot(str)
    def load_csv(self, filepath):
        """ Carga el archivo CSV y actualiza la vista previa """
        try:
            self.df = pd.read_csv(filepath)
            self.current_row = 0  # Resetear al inicio
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
        """ Navegar a la siguiente fila """
        if self.df is not None and self.current_row < len(self.df) - 1:
            self.current_row += 1
            self.update_preview()

    @Slot()
    def previous_row(self):
        """ Navegar a la fila anterior """
        if self.df is not None and self.current_row > 0:
            self.current_row -= 1
            self.update_preview()
