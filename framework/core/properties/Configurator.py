from mergedeep import merge


class Configurator:
    def __init__(self):
        self.properties_store = {}

    def merge_properties(self, to_merge):
        if to_merge is not None:
            merge(self.properties_store, to_merge)
