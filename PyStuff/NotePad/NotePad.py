from PyQt6.QtWidgets import  QInputDialog, QMainWindow,QApplication,QMenuBar,QMenu,QFileDialog,QTextEdit,QHBoxLayout
from PyQt6.QtGui import QAction, QTextCursor,QColor
from PyQt6.QtCore import Qt
 
import sys
class Window(QMainWindow):
 
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0,0,700,500)
        self.current_file = None
 
          #Adding the text field for our notepad
        self.edit_field = QTextEdit(self)
 
        #Create a layout
        self.setCentralWidget(self.edit_field)
 
        #creating a menubar
        menubar = QMenuBar(self)
        self.setMenuBar(menubar)
 
        #creating menu items
        fileMenu = QMenu("File",self)
        menubar.addMenu(fileMenu)
 
        #Creating actions
        new_action = QAction("New",self)
        fileMenu.addAction(new_action)
        new_action.triggered.connect(self.new_file)
 
        open_action = QAction("Open",self)
        fileMenu.addAction(open_action)
        open_action.triggered.connect(self.open_file)
        
        save_as_action = QAction("Save As",self)
        fileMenu.addAction(save_as_action)
        save_as_action.triggered.connect(self.save_file_as)
 
        save_action = QAction("Save",self)
        fileMenu.addAction(save_action)
        save_action.triggered.connect(self.save_file)
 
        #creating the edit menu
        editmenu = QMenu("Edit",self)
        menubar.addMenu(editmenu)
 
        undo_action = QAction("Undo",self)
        editmenu.addAction(undo_action)
        undo_action.triggered.connect(self.edit_field.undo)
 
        redo_action = QAction("Redo",self)
        editmenu.addAction(redo_action)
        redo_action.triggered.connect(self.edit_field.redo)
 
        cut_action = QAction("Cut",self)
        editmenu.addAction(cut_action)
        cut_action.triggered.connect(self.edit_field.cut)
 
        copy_action = QAction("Copy",self)
        editmenu.addAction(copy_action)
        copy_action.triggered.connect(self.edit_field.copy)
 
        paste_action = QAction("Paste",self)
        editmenu.addAction(paste_action)
        paste_action.triggered.connect(self.edit_field.paste)
 
        find_action = QAction("Find",self)
        editmenu.addAction(find_action)
        find_action.triggered.connect(self.find_text)
 
      
 
    def open_file(self):
        file_path,_ = QFileDialog.getOpenFileName(self,"Open File","","All Files (*);; Python Files (*.py)")
        with open(file_path,"r") as fp:
            self.current_file=file_path
            text = fp.read()
            self.edit_field.setText(text)
        
        print(file_path)
       
    def new_file(self):
        self.edit_field.clear()
        self.current_file=None
 
    def save_file_as(self):
        file_path,_=QFileDialog.getSaveFileName(self,"Save File","","All Files(*);; Python Files(*.py)")
        if file_path:
            with open(file_path,"w")as file:
                file.write(self.edit_field.toPlainText())
            self.current_file=file_path
 
    def save_file(self):
        if self.current_file:
            with open(self.current_file,"w") as file:
                file.write(self.edit_field.toPlainText())
        else:
            self.save_file_as()
 
    def find_text(self):
        #first display the input dialouge and get the search text from it
        search_text, ok= QInputDialog.getText(self,"Find Text","Search for")
        #if user clicks ok, begin the search
        if ok:
            #this list is used to store inofrmation about the selected text for highliting
            all_words = []
            # set the cursor to the beignning of the edit field, this ensures the search
            # starts from beginning
            self.edit_field.moveCursor(QTextCursor.MoveOperation.Start)
            #set the highlught color
            highlight_color = QColor(Qt.GlobalColor.yellow)
 
            #Loop through all the edit field text and find the search_text
            while(self.edit_field.find(search_text)):
                # This creates instance of QTextEdit.Extraselection which is used to define
                # the formatting and location of highligted text
                selection = QTextEdit.ExtraSelection()
                # Sets background color of selection
                selection.format.setBackground(highlight_color)
 
                # adds selection to text
                selection.cursor = self.edit_field.textCursor()
                all_words.append(selection)
 
            self.edit_field.setExtraSelections(all_words)
 
    
 
app = QApplication(sys.argv)
window = Window()
window.show()
app.exec()