from abc import ABC ,abstractmethod
from datetime import date
class DigitalAsset(ABC):
    def __init__(self,name:str, registration_date:date,cost:float):
        self.__name = name
        self.__registration_date = registration_date
        self.__cost = cost

    @property
    def get_function(self):
        return self.__cost ,self.__name ,self.__registration_date

    @get_function.getter
    def get_name(self):
        return self.__name

    @get_function.getter
    def get_cost(self):
        return self.__cost
    @get_function.getter
    def get_registration_date(self):
        return self.__registration_date.isoformat()

    @abstractmethod
    def calculate_value(self):
        return float
    @abstractmethod
    def asset_type(self):
        return str



