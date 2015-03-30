# coding=utf-8
from vulyk.models.task_types import AbstractTaskType
from vulyk.tasks.dummy import DummyTask, DummyAnswer


class DummyTaskType(AbstractTaskType):
    """
    DummyTaskType as a sample to create new Task types
    """
    answer_model = DummyAnswer
    task_model = DummyTask
    template = "dummy_template.html"
    type_name = "dummy_task"

    redundancy = 3

    readable_name = "Dummy Task"
    description = "Example of creation of new tasks"
    logo = "logo.png"

    CSS_ASSETS = []
    JS_ASSETS = []
