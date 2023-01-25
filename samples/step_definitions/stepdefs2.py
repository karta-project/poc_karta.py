import json


def my_sample_step_definition3(__step_def__="my sample step definition3", step=None, context=None):
    print('Step is:', str(step.name))
    print('Context is:', str(json.dumps(context)))
    print('Test data passed is ', str(json.dumps(step.test_data)))
    context['var3'] = 3


def my_sample_step_definition4(__step_def__="my sample step definition4", step=None, context=None):
    print('Step is:', str(step.name))
    print('Context is:', str(json.dumps(context)))
    print('Test data passed is ', str(json.dumps(step.test_data)))
    context['var4'] = 4
