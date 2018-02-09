import pytest
from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.technical.container import *
from tests.fixtures.data_sets.service.dummy.dummy import Dummy
from tests.fixtures.data_sets.service.dummy.dummy_configurable import DummyConfigurable


class TestContainer(AbstractTestCase):
    def s(self):
        return self.container

    def setup_method(self, method):
        self.container = Container()

    def _init_container(self):
        self.s().add_definitions(self.datasets_path + '/container/definitions.yml')

    """
    add_definition
    """

    def test_add_definitions_with_dict_return_cls(self):
        self.s().add_definitions({'services': {'service': [1, 2, 3]}}) \
            .add_definitions({'configurations': {'data': [4, 5]}}) \
            .add_definitions({'configurations': {'data': [2], 'data2': 'val2'}}) \
            .add_definitions({'services': {'service2': 'a values'}})
        self.assert_equals_resultset(self.s().get_definitions())

    def test_add_definitions_with_unknown_file_raise_exception(self):
        with pytest.raises(FileExistsError):
            self.s().add_definitions('unknownFile')

    def test_add_definitions_with_file_return_cls(self):
        self.s().add_definitions(self.datasets_path + '/container/simple_definitions.yml')
        self.assert_equals_resultset(self.s().get_definitions())

    """
    get_definitions
    """

    def test_get_definitions_with_no_definitions_return_empty_dict(self):
        assert {} == self.s().get_definitions()

    def test_get_definitions_with_definitions_return_dict(self):
        definitions = {'configurations': {'some data1': [4, 5]}, 'services': {'service1': 'data'}}
        self.s().add_definitions(definitions)
        assert definitions == self.s().get_definitions()

    """
    has
    """

    def test_has_with_unknown_service_return_false(self):
        self._init_container()
        assert not self.s().has("unknownService")

    def test_has_with_unknown_service_return_true(self):
        self._init_container()
        assert self.s().has("dummy")

    """
    get
    """

    def test_get_with_unknown_service_raise_exception(self):
        self._init_container()
        with pytest.raises(RuntimeError, match="service id 'serviceUnknown' does not exists"):
            self.s().get('serviceUnknown')

    def test_get_with_success_return_singleton_service(self):
        self._init_container()
        service = self.s().get('dummy')
        assert isinstance(service, Dummy)
        service2 = self.s().get('dummy')
        assert service == service2

    def test_get_with_configurable_service_return_service(self):
        self._init_container()
        service = self.s().get('dummy_configurable')
        assert isinstance(service, DummyConfigurable)
        self.assert_equals_resultset(service._configs)

    """
    clear
    """

    def test_clear_success(self):
        self._init_container()
        self.s().clear('dummy')
        service = self.s().get('dummy')
        assert isinstance(service, Dummy)
        self.s().clear('dummy')
        service2 = self.s().get('dummy')
        assert service != service2
