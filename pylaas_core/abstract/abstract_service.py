import sys
from os import path
from pylaas_core.interface.core.service_interface import ServiceInterface
from pylaas_core.pylaas_core import PylaasCore


class AbstractService(ServiceInterface):
    """Abstract service class

    Attributes:
        _adapter: service adapter if needed
    """

    def __init__(self) -> None:
        """ Init service """
        module_name = self.__module__
        filename = sys.modules[module_name].__file__
        if path.exists(filename.replace('.py', '_adapter.py')):
            module_name += "_adapter"
            class_name = "{}Adapter".format(self.__class__.__name__)
            __import__(module_name)
            adapter = getattr(sys.modules[module_name], class_name)
            adapter = adapter()
            self._adapter = adapter
        else:
            self._adapter = None
        list_services = PylaasCore.get_container().get_definitions()['services']
        for service in list_services:
            setattr(self, '{}_service'.format(service), self._make_service_method(service))

    def set_adapter(self, adapter):
        """Set service adapter

        Args:
            adapter:

        Returns:
            cls
        """
        self._adapter = adapter
        return self

    def get_adapter(self):
        """Get current adapter
        Returns:
            adapter
        """
        return self._adapter

    def has_adapter(self):
        """Check if an adapter exists
        Returns:
            bool
        """
        return self._adapter is not None

    @staticmethod
    def _make_service_method(service_id):
        def get_service():
            return PylaasCore.get_service(service_id)
        return get_service

    @staticmethod
    def get_service(service_id) -> ServiceInterface:
        """
        Get service

        Args:
            service_id (string): service id to instantiate from container

        Returns:
            ServiceInterface
        """
        return PylaasCore.get_service(service_id)
