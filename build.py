from cx_Freeze import setup, Executable

base = None

executables = [Executable("main.py", base=base)]

packages = ["idna", "pynput", "pathlib", "json", "defs", "queue"]
options = {
    'build_exe': {
        'packages': packages,
        'include_msvcr': True
    },
}

setup(
    name="Dautonav",
    options=options,
    version="0.1",
    description='Simple utility to navigate in Dofus with a keyboard.',
    executables=executables
)
