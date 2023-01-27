import inspect
import os
from copy import deepcopy

import yaml

from framework.core.models.TestFeature import TestFeature
from framework.core.runner import step_definition_mapping, test_properties
from framework.core.utils import FileUtil, ImportUtil


def init_framework(step_def_package='step_definitions', properties_folder='properties'):
    # Load properties
    test_properties.load_properties(properties_folder)

    # Search for python modules in step definitions folder
    step_definition_module_python_files = FileUtil.get_python_files(step_def_package)

    # Scan for each python module if it has step definitions, add them to step definition mapping
    for py_file in step_definition_module_python_files:
        module_name = os.path.split(py_file)[-1].strip(".py")
        imported_step_def_module = ImportUtil.dynamic_import(module_name, py_file)
        for importedObjectName in dir(imported_step_def_module):
            import_object = imported_step_def_module.__dict__[importedObjectName]
            if callable(import_object):
                signature = inspect.signature(import_object)
                for k, v in signature.parameters.items():
                    if k == "__step_def__" and (v.default is not inspect.Parameter.empty):
                        step_def_name = v.default
                        if isinstance(step_def_name, str):
                            step_definition_mapping[step_def_name] = import_object


def run_feature_file(feature_file):
    # Load the feature file to run
    feature = FileUtil.load_yaml_file_into_object_type(feature_file, TestFeature)

    context = {}
    print('Running feature ', str(feature.name))
    for scenario in feature.scenarios:
        print('Running scenario ', str(scenario.name))
        for step in scenario.steps:
            print('Running step ', str(step.name))
            step_to_call = step.name.strip()
            if step_to_call in step_definition_mapping.keys():
                context['__feature__'] = feature.name
                context['__scenario__'] = scenario.name
                context['__properties__'] = test_properties.properties_dict
                # TODO: Check if better way. Doing deep copy to avoid step definition editing step object.
                step_definition_mapping[step_to_call](step=deepcopy(step), context=context)
            else:
                print("Step definition mapping for %s could not be found", step_to_call)
