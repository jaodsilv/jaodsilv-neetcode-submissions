import threading

class Singleton:
    __lock = threading.Lock()
    __instance = None


    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(Singleton, cls).__new__(cls)
                cls.__instance.setValue("")
            return cls.__instance


    def getValue(self) -> str:
        return self.__value


    def setValue(self, value: str):
        self.__value = value