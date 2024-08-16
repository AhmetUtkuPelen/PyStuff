#create a basic window
import sys
from PyQt6.QtWidgets import QWidget,QApplication,QGridLayout,QLabel,QPushButton
from PyQt6.QtCore import Qt
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Calculator")
        
        #Create a label to display the result
        self.display = QLabel()
        self.display.setText("0")
        self.display.setAlignment(Qt.AlignmentFlag.AlignRight)
        # Now this widget is created, we need to add it to the layout given below
        
        
        #Create number buttons and store those buttons inside an array
        self.buttons = [QPushButton(str(i)) for i in range(10)]
        #Now add these buttons to the layout below
        #Loop through every button and attach the number button clicked method to it
        for button in self.buttons:
            button.clicked.connect(self.number_button_clicked)
        
        # Create the operator buttons
        self.operators = ["+","-","*","/"]
        self.operator_buttons = [QPushButton(op) for op in self.operators]
        # Now add these oeperator buttons to the layout below
        for button in self.operator_buttons:
            button.clicked.connect(self.operator_button_clicked)
        
        # Create clear and equals button
        self.equals_button = QPushButton("=")
        self.equals_button.clicked.connect(self.calculate)
        self.clear_button = QPushButton("C")
        
        
        #Create a layout and add it to the window
        layout = QGridLayout()
        
        #Add the display wudget to the layout
        layout.addWidget(self.display,0,0,1,4)
        #addWidget(widget,row,col,rowSpan,colSpan)  
        
        #adding the number buttons to the layout
        #loop through each button first
        # i gives the index value of a button
        for i,button in enumerate(self.buttons):
            #divmod gives back the quotient and remainder
            row,col = divmod(i,3)
            # we divide the index of a button with 3 as we want to span 3 columns for button.
            # if we want buttons to span 4 columns we divide by 4 in above divmod
            layout.addWidget(button,row+1,col)
            
        #Adding operator buttons
        for i,op_button in enumerate(self.operator_buttons):
            layout.addWidget(op_button,i+1,3)
            
        #Add = and C button
        layout.addWidget(self.clear_button,4,2)
        layout.addWidget(self.equals_button,4,1)
              
        self.setLayout(layout)
        
        
        # Create three variables, current input, previous input and current operator
        self.current_input = "0"
        self.current_operator =""
        self.previous_operator=""
        
        #create a method for number button clicked
    def number_button_clicked(self):
        # get the text from the button being clicked
        digit = self.sender().text()
            
        if self.current_input=="0":
            self.current_input=digit
        else:
            self.current_input += digit
        self.display.setText(self.current_input)
            
            
    def operator_button_clicked(self):
        # get the text from operator button
        operator = self.sender().text()
        if self.current_operator=="":
            self.previous_input = self.current_input
            self.current_input="0"
            self.current_operator = operator 
            print("current operator empty")
        else:
            # call the calculate method here
            print("current operator NOT empty")
            self.calculate()
            #Same as above
            self.previous_input = self.current_input
            self.current_operator = operator
            self.current_input = "0"        
    
    def calculate(self):
        if self.current_operator=="+":
            result = str(float(self.previous_input)+float(self.current_input))
        elif self.current_operator=="-":
            result = str(float(self.previous_input)-float(self.current_input))
        elif self.current_operator=="*":
            result = str(float(self.previous_input)*float(self.current_input))
        elif self.current_operator=="/":
            if self.current_input=="0":
                result="Error"
            else:
                result = str(float(self.previous_input)/float(self.current_input))
        else:
            result=self.current_input
        self.display.setText(result)
        self.current_input=result
        self.current_operator=""
 
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())