import pytest
from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.technical.container import *
from tests.fixtures.data_sets.service.dummy.dummy import Dummy
from tests.fixtures.data_sets.service.dummy.dummy_configurable import DummyConfigurable


class TestContainer(AbstractTestCase):
    def _init_container(self):
        container = Container()
        container.add_definitions(self.datasets_path + '/container/definitions.yml')
        return container

    """
    add_definition
    """

    def test_add_definitions_with_dict_return_self(self):
        container = Container()
        container.add_definitions({'firstOne': {'some data1': [4, 5]}, 'secondOne': [1, 2, 3]})
        result = container.add_definitions({'secondOne': [2, 3], 'thirdOne': 'some values'})
        assert result == container
        self.assert_equals_resultset(container._definitions)

    def test_add_definitions_with_unknown_file_raise_exception(self):
        container = Container()
        with pytest.raises(FileExistsError):
            container.add_definitions('unknownFile')

    def test_add_definitions_with_file_return_self(self):
        container = Container()
        container.add_definitions(self.datasets_path + '/container/simple_definitions.yml')
        self.assert_equals_resultset(container._definitions)

    """
    get_definitions
    """

    def test_get_definitions_with_no_definitions_return_empty_dict(self):
        container = Container()
        assert {} == container.get_definitions()

    def test_get_definitions_with_definitions_return_dict(self):
        container = Container()
        definitions = {'firstOne': {'some data1': [4, 5]}, 'secondOne': [1, 2, 3]}
        container.add_definitions(definitions)
        assert definitions == container.get_definitions()

    """
    has
    """

    def test_has_with_unknown_service_return_false(self):
        container = self._init_container()
        assert not container.has("unknownService")

    def test_has_with_unknown_service_return_true(self):
        container = self._init_container()
        assert container.has("dummy")

    """
    get
    """

    def test_get_with_unknown_service_raise_exception(self):
        container = self._init_container()
        with pytest.raises(RuntimeError, match="service id 'serviceUnknown' does not exists"):
            container.get('serviceUnknown')

    def test_get_with_success_return_singleton_service(self):
        container = self._init_container()
        service = container.get('dummy')
        assert isinstance(service, Dummy)
        service2 = container.get('dummy')
        assert service == service2

    def test_get_with_configurable_service_return_service(self):
        container = self._init_container()
        service = container.get('dummy_configurable')
        assert isinstance(service, DummyConfigurable)
        self.assert_equals_resultset(service._configs)
