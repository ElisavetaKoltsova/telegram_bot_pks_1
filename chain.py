class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle(self, request):
        handled = self._process(request)
        if not handled and self._successor:
            return self._successor.handle(request)
        return handled

    def _process(self, request):
        raise NotImplementedError("Нужно переопределить _process")

class ComplexityHandler(Handler):
    def _process(self, request):
        if "сложность" in request.lower():
            return "Оцениваю сложность проекта... уровень: средний 🧠"
        return None

class DeveloperHandler(Handler):
    def _process(self, request):
        if "разработчик" in request.lower():
            return "Подбираю подходящих разработчиков 👩‍💻"
        return None

class DefaultHandler(Handler):
    def _process(self, request):
        return "Не понял запрос, попробуй уточнить."
