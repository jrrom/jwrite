import sys
import os
# PySide6 imports
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore    import Slot
# To load QUi files used by PySide6
loader   = QUiLoader()
dir_name = os.path.dirname(os.path.realpath(__file__))

# About class to wrap About.ui
class About():
  # To create class
  def __init__(self):
    # Cross platform support for different file path types
    # Windows
    if sys.platform == "win32":
      self.window = loader.load(dir_name + "\\views\\About.ui")
    # Linux and others
    else:
      self.window = loader.load(dir_name + "/views/About.ui", None)

  # Function that can be called by the GUI
  @Slot()
  # To display
  def show(self):
    self.window.show()