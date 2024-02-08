
class Task():
    """
    Task instance
    """
    def __init__(self, task):
        """
        Initializes the task
        """
        self.task = task
        self.validate();
    
    def validate(self):
        """
        Validates the task
        """
        if not self.task:
            raise Exception("Invalid task");
        if not self.task.get("name", None):
            raise Exception("No task name is given");
        if not self.task.get("platform", None):
            raise Exception("No platform was given")
        if not self.task.get("module", None):
            raise Exception("No module was given")
        if not self.task.get("command", None):
            raise Exception("No command was given")
    def get_command(self):
        return self.task["command"]
    def execute(self, client):
        """
        Executes command on remote device
        """
        stdin, stdout, stderr = client.exec_command(self.task.get("command"))
        print(stdout.readlines())
        