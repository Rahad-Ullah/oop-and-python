# singleton -> one instance of a class in the whole program

class Singleton:
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            Singleton.__instance = self
        else:
            raise Exception("This class is a singleton! Already initialized an instance")

    @staticmethod
    def get_instance():
        if not Singleton.__instance:
            Singleton()
        return Singleton.__instance

first = Singleton.get_instance()
second = Singleton.get_instance()
print(first)
print(second)