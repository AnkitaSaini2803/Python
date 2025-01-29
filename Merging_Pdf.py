'''23/1/205'''
from pypdf import PdfWriter
import os 
merger=PdfWriter()

files= [file for file in os.listdir() if file.endswith(".pdf")]

for pdf in files:
             merger.append(pdf)

merger.write('Merdged-Pdf')
merger.close()

