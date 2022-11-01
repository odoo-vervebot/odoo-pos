# import win32print
# filepath = r'Product labels 57x35mm.pdf'
# myprinter = win32print.OpenPrinter(win32print.GetDefaultPrinter(), None)
# with open(filepath, mode='rb') as file:
#    buf = file.read()
# win32print.StartDocPrinter(myprinter, 1, ("Product labels 57x35mm.pdf", None, "raw"))
# win32print.StartPagePrinter(myprinter)
# win32print.WritePrinter(myprinter, buf)
# win32print.EndPagePrinter(myprinter)
# win32print.EndDocPrinter(myprinter)
# win32print.ClosePrinter(myprinter)

# filename = "test_print.txt"
filename = "Product_labels_57x35mm.pdf"

# import subprocess
# subprocess.Popen(filename,shell=True)
# command = "{} {}".format('PDFtoPrinter.exe',filename)
# subprocess.call(command,shell=True)

# import os
# os.startfile(filename, 'print')

# import win32ui
# dc = win32ui.CreateDC()
# dc.CreatePrinterDC()
# dc.StartDoc('My Python Document')
# dc.StartPage()
# dc.TextOut(100,100, 'Python Prints!')
# dc.MoveTo(100, 102)
# dc.LineTo(200, 102)
# dc.EndPage()
# dc.EndDoc()

import win32print
import win32ui

x = 0
y = 50
printer_name = win32print.GetDefaultPrinter()
# if your printer is standard, replace the printer_name:
# win32print.GetDefaultPrinter()

# fd = open(filename, "r", encoding = "utf-8")
# input_string = fd.read()
# multi_line_string = input_string.splitlines()

# hDC = win32ui.CreateDC()
# hDC.CreatePrinterDC()
# hDC.StartDoc("Printing...")
# hDC.StartPage()
# for line in multi_line_string:
#     hDC.TextOut(x, y, line)
#     y+=50
# hDC.EndPage()
# hDC.EndDoc()
# fd.close()

import os
import time
import glob
try:
    os.startfile(filename, 'print')
except Exception as a:
    print(a)