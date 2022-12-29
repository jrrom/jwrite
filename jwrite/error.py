import sys
# PySide6 imports
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore    import Slot
# To load QUi files used by PySide6
loader = QUiLoader()

# Error class to wrap Error.ui
class Error():
  # To create class
  def __init__(self, exception):
    # Cross platform support for different file path types
    # Windows
    if sys.platform == "win32":
      self.window = loader.load("jwrite\\views\\Error.ui")
    # Linux and others
    else:
      self.window = loader.load("jwrite/views/Error.ui", None)
    # To save error to be displayed
    self.exception = exception
    # To display error
    self.window.label.setText(exception)
  
  # Function that can be called by the GUI
  @Slot()
  # To display
  def show(self):
    self.window.show()