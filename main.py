from ui_MainWindow import Ui_MainWindow
import sys
import os

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import QtWidgets

from Save import *

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)

        # data
        # {
        #   key1: ['line1', 'line2', 'line3', ...,]
        #   key2: ['line1', 'line2', 'line3', ...,]
        #   ...
        #   keyn: ['line1', 'line2', 'line3', ...,]
        # }
        # 其中 line can be 'value' or 'value1 value2 ... valuen'
        # 没有想到更有效率的结构
        self.data = {}

        # Initialize the input_working_dir as the direction where program startup
        self.input_working_dir.setText(os.path.abspath(os.path.dirname(sys.executable)))

    def slot_runScrit(self):
        # change direction to input_working_dir
        os.chdir(self.input_working_dir.text())

        # delete the old data
        files = [f for f in os.listdir(self.input_working_dir.text()) if not os.path.isdir(f)]
        for file in files:
            if (file.split('.')[0] == self.input_inp.text().split('.')[0]
                    and file.split('.')[1] != 'inp' and file.split('.')[1] != 'for'):
                os.remove(file)

        # run abaqus script
        cmd_line = "abaqus job={job} user={forName} int".format(job=self.input_inp.text().split('.')[0],
                                                                forName=self.input_for.text())
        os.system(cmd_line)

    def slot_setWorkingDir(self):
        # select the working direction
        working_dir = os.path.abspath(QFileDialog.getExistingDirectory(self,
                                                                       "Select the working direction:",
                                                                       self.input_working_dir.text()))
        # update display
        self.input_working_dir.setText(working_dir)
        pass

    def slot_setInpName(self):
        inp_name = self.getFileName(".inp")
        # update display
        self.input_inp.setText(os.path.basename(inp_name))

    def slot_setForName(self):
        for_name = self.getFileName(".for")
        # update display
        self.input_for.setText(os.path.basename(for_name))

    def slot_input_inp_changed(self):
        self.input_data_file.setText(self.input_inp.text().split('.')[0] + '.dat')

    def slot_dataDealing(self):
        os.chdir(self.input_working_dir.text())
        # clear data before dataDealing
        self.data = {}
        self.comboBox_keyword.clear()
        self.plainTextEdit.clear()

        if os.path.exists(self.input_data_file.text()):
            with open(self.input_data_file.text(), 'r') as datafile:
                lines = datafile.readlines()
                for index, line in enumerate(lines):
                    # when line starts with the input_identifier, get the data
                    if line.startswith(' ' + self.input_identifier.text()):
                        key = line.strip().split()[1]
                        # then key is not in the data, new data[key], or append data[key]
                        if key not in self.data:
                            self.data[key] = [lines[index+1].strip()]
                        else:
                            self.data[key].append(lines[index+1].strip())
            self.comboBox_keyword.addItems(list(self.data.keys()))
        else:
            QtWidgets.QMessageBox.warning(self, "Warning!", "Data file does not exist.",
                                          QtWidgets.QMessageBox.Cancel)

    def slot_update(self):
        self.plainTextEdit.clear()
        keyword = self.comboBox_keyword.currentText()
        if keyword:
            for text in self.data[keyword]:
                self.plainTextEdit.appendPlainText(text)

    def getFileName(self, str):
        title = "Select the {str} file:".format(str=str)
        ftype = "{str1} File (*{str2})".format(str1=str, str2=str)
        filename, filetype = QFileDialog.getOpenFileName(self,
                                                         title,
                                                         self.input_working_dir.text(),
                                                         ftype)
        return filename

    def slot_txt(self):
        saveTXT(self.comboBox_keyword.currentText(), self.plainTextEdit.toPlainText())
        QtWidgets.QMessageBox.information(self, 'Info', 'Complete.', buttons=QtWidgets.QMessageBox.Ok)

    def slot_csv(self):
        saveCSV(self.data)
        QtWidgets.QMessageBox.information(self, 'Info', 'Complete.', buttons=QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
