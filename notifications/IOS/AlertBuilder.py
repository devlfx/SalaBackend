from abc import ABC,abstractmethod

class AlertBuilder(ABC):

    @abstractmethod
    def build_body(self,data:dict = None, title:str = "", body:str = "", sound:str = "default",thread_id:str = None):
        """Method for creating the json body"""

    def build_headers(self,token:str,bundle:str, data:dict = None):
        """Method for creating the json headers"""