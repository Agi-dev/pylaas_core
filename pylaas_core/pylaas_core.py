"""
This module implements the alfred core system.

"""
import abc
from pylaas_core.technical.container import Container


class PylaasCore(abc.ABC):
    """
    Attributes:
        _container (Container) : unique instance
    """
    _container = None

    def __new__(cls):
        """Prevent instantiation
        """
        raise TypeError("PylaasCore class may not be instantiated")

    @abc.abstractclassmethod
    def init(cls):  # pragma: no cover
        """Init AlfredCore

        init default Container with definitions
        """
        pass

    @classmethod
    def _init(cls, definitions):
        """Init AlfredCore

        init default Container with definitions

        Args:
            definitions (dict|string): container definitions
        """
        cls._container = Container()
        cls._container.add_definition(definitions)

    @classmethod
    def get_container(cls):
        """Get current container

        Returns:
            container (ContainerInterface): current container

        """
        return cls._container

    @classmethod
    def get_service(cls, service_id):
        """Get service

        Args:
            service_id (string): service id to instantiate from container

        Returns:
            service (ServiceInterface): service instance (singletons)

        """
        return cls.get_container().get(service_id)
