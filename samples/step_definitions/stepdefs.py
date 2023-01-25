import json


def my_sample_step_definition1(__step_def__="my sample step definition1", step=None, context=None):
    print('Step is:', str(step.name))
    print('Context is:', str(json.dumps(context)))
    print('Test data passed is ', str(json.dumps(step.test_data)))
    context['var1'] = 1


def my_sample_step_definition2(__step_def__="my sample step definition2", step=None, context=None):
    print('Step is:', str(step.name))
    print('Context is:', str(json.dumps(context)))
    print('Test data passed is ', str(json.dumps(step.test_data)))
    context['var2'] = 2
