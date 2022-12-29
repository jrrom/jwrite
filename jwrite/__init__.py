import sys
# PySide6 imports
from PySide6.QtWidgets import QApplication
from PySide6.QtCore    import QCoreApplication, Qt
# To import main window class
from .main_window       import MainWindow 
 
# Starting point of program 
def main(): 
  # To disable errors
  QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

  # To initialise application class
  app         = QApplication(sys.argv)
  #Initialise main window class
  main_window = MainWindow()
  main_window.show()
  # To start the application
  app.exec()

# If run as a program
if __name__ == "__main__":
    main()