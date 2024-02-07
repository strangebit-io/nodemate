import json
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from .tasks import Task

class NodeBook(object):
    def __init__(self):
        pass
    def load(self, filename):
        """
        Loads the nodebook the memory
        """
        if not filename:
            raise Exception("File does not exist")
        with open(filename) as f:
            self.nodebook = json.loads("".join(f.readlines()))
        self.validate();
    
    def validate(self):
        """
        Validates tasks
        """
        if not self.nodebook.get("nodebook", None):
            raise Exception("Invalid root element")
        tasks = self.nodebook["nodebook"].get("tasks", None)
        if not tasks:
            raise Exception("Invalid tasks element")
        self.tasks = []
        for task in tasks:
            self.tasks.append(Task(task))
        self.nodes = self.nodebook["nodebook"].get("nodes", None)
        if not self.nodes:
            raise Exception("No nodes are given")
        self.comment = self.nodebook.get("comment", None)
    
    def get_tasks(self):
        """
        Returns list of tasks
        """
        return self.tasks
