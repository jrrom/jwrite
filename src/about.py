import sys
# PySide6 imports
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore    import Slot
# To load QUi files used by PySide6
loader = QUiLoader()

# About class to wrap About.ui
class About():
  # To create class
  def __init__(self):
    # Cross platform support for different file path types
    # Windows
    if sys.platform == "win32":
      self.window = loader.load("jwrite\\views\\About.ui")
    # Linux and others
    else:
      self.window = loader.load("jwrite/views/About.ui", None)

  # Function that can be called by the GUI
  @Slot()
  # To display
  def show(self):
    self.window.show()