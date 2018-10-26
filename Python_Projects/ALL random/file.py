x=raw_input ("Enter Filename:")
filehandle=open(x,'r')
try:
  print ("This file has been opened=" + (x))
except:
  print "File not found"
# below are the excerpts from the GUI, currently my program does everything it needs to do but opening the file from the input on the fields below.
# Form Constructor
  self.pbutton0 = QPushButton("Open Input File")
  self.lineedit0 = QLineEdit("Input File Name")
# Form Methods
 def button0Pressed(self):
    self.lineedit0.setText("FileOpened="+(x))