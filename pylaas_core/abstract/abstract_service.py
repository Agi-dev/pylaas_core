import sys
from os import path
from pylaas_core.interface.core.service_interface import ServiceInterface


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
