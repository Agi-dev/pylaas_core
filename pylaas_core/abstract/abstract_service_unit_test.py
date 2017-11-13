from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.abstract.service_mock import ServiceMock
from pylaas_core.pylaas_core import PylaasCore


class AbstractServiceUnitTest(AbstractTestCase):
    _service = None
    _service_id = None

    def setup_method(self, method):
        if not self._service_id:
            raise RuntimeError('Attribute _service_id cannot be empty')

        self._service = PylaasCore().get_service(self._service_id)

        # init adapter as a mock if necessary
        if self._service.has_adapter():
            self._service.set_adapter(ServiceMock())

    def get_service(self):
        return self._service
