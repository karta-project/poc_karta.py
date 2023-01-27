from mergedeep import merge


class KartaConfiguration:
    def __init__(self, step_def_mapping_files=None, test_catalog_files=None, test_property_files=None, ):
        self.step_def_mapping_files = step_def_mapping_files if step_def_mapping_files is not None else []
        self.test_catalog_files = test_catalog_files if test_catalog_files is not None else []
        self.test_property_files = test_property_files if test_property_files is not None else []

    def read_configuration(self):
        pass
