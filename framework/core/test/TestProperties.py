import yaml
from mergedeep import merge

from framework.core.utils import FileUtil


class TestProperties:
    def __init__(self):
        self.properties_dict = {}

    def merge_properties(self, to_merge):
        if to_merge is not None:
            merge(self.properties_dict, to_merge)

    def load_properties(self, properties_folder='properties'):
        # Merge YAML property files into configurator.
        for property_file in FileUtil.get_files_of_extension(properties_folder, ".yaml"):
            with open(property_file, "r") as stream:
                try:
                    object_dict = yaml.safe_load(stream)
                    self.merge_properties(object_dict)
                except yaml.YAMLError as exc:
                    print(exc)
