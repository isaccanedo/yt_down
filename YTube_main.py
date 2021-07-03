# -*- coding: utf-8 -*-
"""
@author: Isac Canedo
"""

if __name__ == '__main__':
      import sys
      from YTube_GUI import Window
      from PyQt5.QtWidgets import QApplication
      
      app = QApplication(sys.argv)
    
      windowObject = Window()
    
      sys.exit(app.exec_())