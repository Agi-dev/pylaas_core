from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.pylaas_core import PylaasCore
# from pylaas_core.pylaas_core import PylaasCore
# from tests.fixtures.data_sets.service.dummy.dummy_configurable import DummyConfigurable
from tests.fixtures.data_sets.service.dummy_adapter.dummy_adapter_adapter import DummyAdapterAdapter


class TestAbstractService(AbstractTestCase):
    """Test Suite for AbstractService"""

    def init_container(self):
        p = PylaasCore()
        p._init(self.datasets_path + '/container/definitions.yml')

    """
    __init__
    """
    def test__init__with_no_adapter(self):
        self.init_container()
        assert PylaasCore().get_service('dummy').get_adapter() is None

    def test__init__with_adapter_set_adapter(self):
        self.init_container()
        assert isinstance(PylaasCore().get_service('dummy_adapter').get_adapter(), DummyAdapterAdapter)

    """
    __getattr__
    """
    # def test_get_attr_success_return_service(self):
    #     PylaasCore()._init(self.datasets_path + '/container/definitions.yml')
    #     dummy = PylaasCore().get_service('dummy')
    #     dummyC = dummy.test_magic_service_injection()
    #     assert isinstance(dummyC, DummyConfigurable)
    #
    # def test_get_attr_with_unknown_method_raise_RuntimeError(self):
    #     PylaasCore()._init(self.datasets_path + '/container/definitions.yml')
    #     dummy = PylaasCore().get_service('dummy')
    #     with pytest.raises(RuntimeError, match="service method 'bad_method_format' missing from class"):
    #         dummy.bad_method_format()

    """
    has_adapter
    """

    def test_has_adapter_with_no_adapter_return_false(self):
        self.init_container()
        dummy = PylaasCore().get_service('dummy')
        assert not dummy.has_adapter()

    def test_has_adapter_with_adapter_return_true(self):
        self.init_container()
        dummy_adapter = PylaasCore().get_service('dummy_adapter')
        assert dummy_adapter.has_adapter()

    """
    get_adapter
    """

    def test_get_adapter_with_no_adapter_return_none(self):
        self.init_container()
        assert PylaasCore().get_service('dummy').get_adapter() is None

    def test_get_adapter_with_adapter_return_adapter(self):
        self.init_container()
        assert isinstance(PylaasCore().get_service('dummy_adapter').get_adapter(), DummyAdapterAdapter)

    """
    set_adapter
    """

    def test_set_adapter_success(self):
        self.init_container()
        dummy = PylaasCore().get_service('dummy')
        assert not dummy.has_adapter()
        dummy.set_adapter(DummyAdapterAdapter)
        assert dummy.has_adapter()
        assert issubclass(dummy.get_adapter(), DummyAdapterAdapter)
