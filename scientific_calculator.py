
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt
import math

class ScientificCalculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project 1 Scientific Calculator")
        self.setGeometry(200, 200, 650, 440)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.display = QLineEdit()
        self.display.setFont(QFont('Arial', 24))
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.display)

        self.buttons_layout = QGridLayout()
        self.layout.addLayout(self.buttons_layout)

        self.expression = ""

        
        buttons = [
            ('7', 0, 0, QColor(220, 220, 220)),  # Light gray
            ('8', 0, 1, QColor(220, 220, 220)),
            ('9', 0, 2, QColor(220, 220, 220)),
            ('/', 0, 3, QColor(255, 165, 0)),    # Orange 
            ('Clr/Del', 0, 4, QColor(255, 0, 0)),

            ('4', 1, 0, QColor(220, 220, 220)),
            ('5', 1, 1, QColor(220, 220, 220)),
            ('6', 1, 2, QColor(220, 220, 220)),
            ('*', 1, 3, QColor(255, 165, 0)),
            ('(', 1, 4, QColor(220, 220, 220)),  # Light gray 

            ('1', 2, 0, QColor(220, 220, 220)),
            ('2', 2, 1, QColor(220, 220, 220)),
            ('3', 2, 2, QColor(220, 220, 220)),
            ('-', 2, 3, QColor(255, 165, 0)),
            (')', 2, 4, QColor(220, 220, 220)),

            ('0', 3, 0, QColor(220, 220, 220)),
            ('.', 3, 1, QColor(220, 220, 220)),
            ('+', 3, 2, QColor(255, 165, 0)),
            ('%', 3, 3, QColor(255, 165, 0)),
            ('=', 3, 4, QColor(0, 174, 239)), # Blue 

            ('sin', 4, 0, QColor(153, 102, 255)),  # Purple 
            ('cos', 4, 1, QColor(153, 102, 255)),
            ('tan', 4, 2, QColor(153, 102, 255)),
            ('log', 4, 3, QColor(153, 102, 255)),
            ('ln', 4, 4, QColor(153, 102, 255)),
            ('π', 5, 0,QColor(153, 102, 255)), 

            
            ('e', 5, 1,QColor(153, 102, 255)), 
            ('sqrt', 5, 2,QColor(153, 102, 255)), 
            ('x^2', 5, 3,QColor(153, 102, 255)), 
            ('x^y', 5, 4,QColor(153, 102, 255))]
        

        for (text, row, col,color) in buttons:
            button = QPushButton(text)
            button.setFont(QFont('Arial', 18))
            button.setStyleSheet("background-color: Black; color: White; border: none; padding: 10px;")
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))
            self.buttons_layout.addWidget(button, row, col)
            
            button.setStyleSheet(f"background-color: {color.name()}; color: White; border: none; padding: 10px;")

    def on_button_click(self, char):
        if char == "=":
            self.calculate()
        elif char == "C":
            self.expression = ""
            self.display.setText("")
        elif char in ["sin", "cos", "tan", "log", "ln", "sqrt", "x^2", "x^y", "π", "e"]:
            self.handle_advanced_functions(char)
        elif char == "Clr/Del":
            self.clear_or_delete()
        else:
            self.expression += str(char)
            self.display.setText(self.expression)
    def clear_or_delete(self):
        
        if self.expression == "":
            
            self.expression = ""
            self.display.setText("")
        else:
           
            self.expression = self.expression[:-1]
            self.display.setText(self.expression)

    def handle_advanced_functions(self, func):
        try:
            if func == "sin":
                self.expression = str(math.sin(math.radians(float(self.expression))))
            elif func == "cos":
                self.expression = str(math.cos(math.radians(float(self.expression))))
            elif func == "tan":
                self.expression = str(math.tan(math.radians(float(self.expression))))
            elif func == "log":
                self.expression = str(math.log10(float(self.expression)))
            elif func == "ln":
                self.expression = str(math.log(float(self.expression)))
            elif func == "sqrt":
                self.expression = str(math.sqrt(float(self.expression)))
            elif func == "x^2":
                self.expression = str(float(self.expression) ** 2)
            elif func == "x^y":
                self.expression += "**"
            elif func == "π":
                self.expression = str(math.pi)
            elif func == "e":
                self.expression = str(math.e)
            self.display.setText(self.expression)
        except:
            self.expression = "Error"
            self.display.setText(self.expression)

    def calculate(self):
        try:
            self.expression = str(eval(self.expression))
            self.display.setText(self.expression)
        except:
            self.expression = "Error"
            self.display.setText(self.expression)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScientificCalculator()
    window.show()
    sys.exit(app.exec_())
