import os
import yaml


def get_files_of_extension(src, extension):
    """Gets a list of file with specified extension in the direction specified."""
    cwd = os.getcwd()
    matching_files = []
    for root, dirs, files in os.walk(src):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(cwd, root, file))
    return matching_files


def get_python_files(src="."):
    """Get a list of python files in a module directory"""
    return get_files_of_extension(src, ".py")


def load_yaml_file(yaml_file):
    """Loads a yaml file into a dictionary object."""
    with open(yaml_file, "r") as stream:
        try:
            loaded_object = yaml.safe_load(stream)
            return loaded_object
        except yaml.YAMLError as exc:
            print(exc)


def load_yaml_file_into_object_type(yaml_file, object_type):
    """# Loads a yaml into an object of specified type. Needs contractor with all arguments"""
    return object_type(**load_yaml_file(yaml_file))
