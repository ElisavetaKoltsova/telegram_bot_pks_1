from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def execute(self):
        pass

class BackendTask(Task):
    def execute(self):
        return "Проверка backend-части интернет-магазина."

class FrontendTask(Task):
    def execute(self):
        return "Проверка интерфейса и клиентской логики."

class TaskFactory:
    @staticmethod
    def create_task(task_type):
        if task_type == "frontend":
            return FrontendTask()
        elif task_type == "backend":
            return BackendTask()
        else:
            raise ValueError("Неизвестный тип задачи.")
