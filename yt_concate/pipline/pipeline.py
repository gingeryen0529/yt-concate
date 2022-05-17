from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for steps in self.steps:
            try:
                data = steps.process(data, inputs, utils)
            except StepException as e:
                print('Exception happen', e)
                break
