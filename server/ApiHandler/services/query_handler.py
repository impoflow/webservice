from abc import ABC, abstractmethod

class QueryHandler(ABC):
    """
    Clase base (interfaz) para distintos tipos de QueryHandlers.
    """

    @abstractmethod
    def call(self, payload: str) -> str:
        """
        Método abstracto para invocar la lógica correspondiente.
        Debe retornar un string con la respuesta (generalmente JSON).
        """
        pass
