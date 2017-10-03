import re

from pylaas_core.interface.core.service_interface import ServiceInterface
from pylaas_core.pylaas_core import PylaasCore


class AbstractService(ServiceInterface):
    def __getattr__(self, name):
        """Inject service from container

        name must be equal to : <id service>_service

        Args:
            name: method name

        Returns:
            ServiceInterface

        Raises:
            RuntimeError: service method missing
        """
        result = re.search("^(?P<service_id>[a-z0-9._-]*)_service$", name)
        if result:
            return PylaasCore.get_service(result.group('service_id'))
        raise RuntimeError("service method '{}' missing from class".format(name))
