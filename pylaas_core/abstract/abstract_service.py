# import re

from pylaas_core.interface.core.service_interface import ServiceInterface


# from pylaas_core.pylaas_core import PylaasCore


class AbstractService(ServiceInterface):
    pass
    # def __getattr__(self, name, *args):
    #     def missing_method(*args):
    #         result = re.search("^(?P<service_id>[a-z0-9._-]*)_service$", name)
    #         if result:
    #             return PylaasCore.get_service(result.group('service_id'))
    #         raise RuntimeError("service method '{}' missing from class".format(name))
    #
    #     return missing_method
