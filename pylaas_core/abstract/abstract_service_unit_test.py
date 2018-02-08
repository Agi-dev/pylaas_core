from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.abstract.service_mock import ServiceMock
from pylaas_core.interface.core.service_interface import ServiceInterface
from pylaas_core.pylaas_core import PylaasCore


class AbstractServiceUnitTest(AbstractTestCase):
    _service = None
    _service_id = None

    def setup_method(self, method) -> None:
        """
        setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        Args:
            method (string): test method name
        Returns:
            None
        """
        if not self._service_id:
            raise RuntimeError('Attribute _service_id cannot be empty')

        self._service = PylaasCore.get_service(self._service_id)

        # init adapter as a mock if necessary
        if self._service.has_adapter():
            self._service.set_adapter(ServiceMock())

    def get_service(self) -> ServiceInterface:
        """
            get tested service
        Returns:
            ServiceInterface
        """
        return self._service

    def mockAdapter(self, method, return_value=None) -> None:
        """
        mock adapter method call

        Args:
            method (string): method name
            return_value (mixed): value method should return (None by default)

        Returns:
            None
        """
        if not return_value: return

        if isinstance(return_value, Exception):
            getattr(self.get_service().get_adapter(), method).side_effect = return_value

    def assert_adapter_method_call_args(self, expected, method, index_method_call=0):
        """
        assert adapter method call args is equal to expected

        Args:
            expected (mixed)        :
            method (string)         :
            index_method_call (int) :

        Returns:
            None
        """
        actual = self.get_adapter_method_call_args(method, index_method_call)
        try:
            assert expected == actual
        except AssertionError as e:
            if len(e.args) > 0:
                raise e
            self.assertEqual(expected, actual)

    def get_adapter_method_call_args(self, method, index_method_call=0):
        """
        get adapter method call args

        Args:
            method (string)         :
            index_method_call (int) :

        Returns:
            Mixed
        """
        mock_method = self.get_service().get_adapter()  # type: ServiceMock
        return mock_method.get_method_call_args(method, index_method_call)
