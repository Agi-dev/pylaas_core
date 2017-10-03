"""
This module implements the alfred core system.

Pylaas(<config: file|{}>)
"""
from pylaas_core.technical.container import Container


class PylaasCore:
    """
    Attributes:
        _container (Container) : unique instance
    """
    _container = None

    def __new__(cls):
        """Prevent instantiation
        """
        raise TypeError("PylaasCore class may not be instantiated")

    def init(cls, definitions):
        cls._container = Container()
        cls._container.add_definition(definitions)

    def get_container(cls):
        return cls._container

    def get_service(cls, service_id):
        return cls.get_container().get(service_id)

    init = classmethod(init)
    get_container = classmethod(get_container)
    get_service = classmethod(get_service)
