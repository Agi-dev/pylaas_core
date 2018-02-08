from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.pylaas_core import PylaasCore


class AbstractServiceIntegrationTest(AbstractTestCase):
    _service = None
    _service_id = None

    def setup_method(self, method):
        if not self._service_id:
            raise RuntimeError('Attribute _service_id cannot be empty')

        self._service = PylaasCore.get_service(self._service_id)

    def get_service(self):
        return self._service
