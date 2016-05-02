from sniffer.api import *
import os

watch_paths = ['.', 'tests/']

@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

@runnable
def execute_koans(*args):
    #os.system('python -B contemplate_koans.py')
    os.system('taskkill /F /IM cricket-unittest.exe /T')
    os.system('cricket-unittest')
