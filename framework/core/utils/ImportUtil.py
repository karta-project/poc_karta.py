import importlib
import importlib.util
import os

from framework.core.utils import FileUtil


def dynamic_import(module_name_to_import, py_path, execute=True):
    """ Dynamically imports a module with the specified name from a python file."""
    module_spec = importlib.util.spec_from_file_location(module_name_to_import, py_path)
    module = importlib.util.module_from_spec(module_spec)
    if execute:
        module_spec.loader.exec_module(module)
    return module


def dynamic_import_from_src(src, star_import=False):
    """ Dynamically imports modules into global() context from a specified folder. Module name is set to file name."""
    my_py_files = FileUtil.get_python_files(src)
    for py_file in my_py_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_module = dynamic_import(module_name, py_file)
        if star_import:
            for obj in dir(imported_module):
                globals()[obj] = imported_module.__dict__[obj]
        else:
            globals()[module_name] = imported_module
    return
