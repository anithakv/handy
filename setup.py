from cx_Freeze import setup, Executable

base = None    

executables = [Executable("handy.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Handy",
    options = options,
    version = "1.1.8",
    description = 'Detect gestures to execute applications',
    executables = executables
)
