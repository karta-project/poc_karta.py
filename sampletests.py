from framework.core.runner.main import *

init_framework('samples/step_definitions', 'samples/properties')

run_feature_file('samples/features/test.yaml')
run_feature_file('samples/features/test2.yaml')
