import pathtrans
import sys

def _process_arguments(translator):
    if len(sys.argv) > 1:
        for path in sys.argv[1:]:
            print(translator(path))
    else:
        for path in sys.stdin:
            print(translator(path.strip()))

def windows_to_unix():    
    _process_arguments(pathtrans.convert_windows_to_unix)

def unix_to_windows():
    _process_arguments(pathtrans.convert_unix_to_windows)
