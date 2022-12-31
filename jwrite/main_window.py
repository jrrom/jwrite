import sys
import os
# PySide6 imports
from PySide6.QtUiTools import QUiLoader 
from PySide6.QtCore    import Slot
from PySide6.QtWidgets import QFileDialog
# To import components
from .about import About
from .error import Error
# To load QUi files used by PySide6
loader = QUiLoader()
dir_name = os.path.dirname(os.path.realpath(__file__))

# Main window class to wrap MainWindow.ui
class MainWindow():
  # To create class
  def __init__(self):
    # Initialising variable for future use
    self.file_path  = None
    # Cross platform support for different file path types
    # Windows
    if sys.platform == "win32":
      self.window = loader.load(dir_name + "\\views\\MainWindow.ui")
    # Linux
    else:
      self.window = loader.load(dir_name + "/views/MainWindow.ui", None)

    # To connect GUI to Python functions, see corresponding class 
    # methods for more information

    self.window.textEdit.textChanged.connect(self.unsaved)

    self.window.actionNew.triggered.connect(self.new)
    self.window.actionOpen.triggered.connect(self.open)
    self.window.actionSave.triggered.connect(self.save)
    self.window.actionSave_As.triggered.connect(self.save_as)

    self.window.actionUndo.triggered.connect(self.undo)
    self.window.actionRedo.triggered.connect(self.redo)
    self.window.actionCut.triggered.connect(self.cut)
    self.window.actionCopy.triggered.connect(self.copy)
    self.window.actionPaste.triggered.connect(self.paste)

    self.about = About()
    self.window.menuAbout.aboutToShow.connect(self.about.show)

  # To display
  def show(self):
    self.window.show()

  # To show error
  def error(self, exception):
    self.window.hide()
    # To turn exception into string
    self.error = Error(f"{exception}")
    self.error.show()

  # File actions

  # To add "*" to window title on text change
  @Slot()
  def unsaved(self):
    if self.window.windowTitle()[-1] != "*":
      self.window.setWindowTitle(self.window.windowTitle() + "*")

  # To create a new untitled file
  @Slot()
  def new(self):
    self.window.setWindowTitle("Untitled*")
    self.window.textEdit.clear()
    self.file_path = None

  # To open a new file
  @Slot()
  def open(self):
    # To open file dialog menu
    filename = QFileDialog.getOpenFileName()
    # If there is a filename then proceed else do not proceed
    if filename[0]:
      # Exception handling
      try:
        # To open file
        with open(filename[0], "r") as file:
          # To save file information to editor
          self.window.textEdit.setText(file.read())
          self.file_path = file.name
          # Cross platform support for different file path types
          # Windows
          if sys.platform == "win32":
            self.window.setWindowTitle(file.name.split("\\")[-1])
          # Linux and others
          else:
            # To set filename to window title
            self.window.setWindowTitle(file.name.split("/")[-1])
      except Exception as exception:
        # To forward exception
        self.error(exception)

  # To save the file
  @Slot()
  def save(self):
    # If file is untitled then do not proceed, else proceed
    if self.file_path and self.window.windowTitle().strip() != "Untitled*":
      # Exception handling
      try:
        # To write to file
        with open(self.file_path, "w") as file:
          # To write editor text into file
          file.write(self.window.textEdit.toPlainText())
          # To remove "*" from end of filename, signifies no changes with saved file
          if self.window.windowTitle()[-1] == "*":
            self.window.setWindowTitle(self.window.windowTitle()[:-1])
      except Exception as exception:
        # To forward exception
        self.error(exception)
    # If file does not have name then open dialog to save it with a name
    else:
      self.save_as()

  # To save the file with a name
  @Slot()
  def save_as(self):
    # To create file under a name 
    filename = QFileDialog.getSaveFileName(self.window)
    # If file given name then proceed else if dialog is cancelled then do not proceed 
    if filename[0]:
      # Exception handling
      try:
        # To write to newly created file
        with open(filename[0], "w") as file:
          # Writes editor text into file
          file.write(self.window.textEdit.toPlainText())
          # Cross platform support for different file path types
          # Windows
          if sys.platform == "win32":
            self.window.setWindowTitle(file.name.split("\\")[-1])
          # Linux
          else:
            self.window.setWindowTitle(file.name.split("/")[-1])
      except Exception as exception:
        # To forward exception
        self.error(exception)

  # Edit actions

  @Slot()
  def undo(self):
    self.window.textEdit.undo()

  @Slot()
  def redo(self):
    self.window.textEdit.redo()

  @Slot()
  def cut(self):
    self.window.textEdit.cut()

  @Slot()
  def copy(self):
    self.window.textEdit.copy()

  @Slot()
  def paste(self):
    self.window.textEdit.paste()