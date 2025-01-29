import shutil                          #24/1/2025
import os
shutil.copy('Class_Methods.py','CopyOFClassMethods.py')

os.remove('CopyOFClassMethods.py')

shutil.move('Dunder/Magic_Methods.py','Magic_Methods.py')

os.remove('Magic_Methods.py')

shutil.copytree("Dunder","Dunder_Copy")

shutil.rmtree('Dunder_Copy')