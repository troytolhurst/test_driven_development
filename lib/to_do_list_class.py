
class ToDoList():
    def __init__(self):
        self._to_do_list = {}

    def to_do_list_add(self, task_name, task):
        self._to_do_list[task_name] = task

    def to_do_list_return(self):
        return self._to_do_list
    
    def to_do_list_remove(self, task_name):
        if task_name in self._to_do_list:
            del self._to_do_list[task_name]
    