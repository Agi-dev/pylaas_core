# import pytest

from pylaas_core.abstract.abstract_test_case import AbstractTestCase


# from pylaas_core.pylaas_core import PylaasCore
# from tests.fixtures.data_sets.service.dummy.dummy_configurable import DummyConfigurable


class TestAbstractService(AbstractTestCase):
    """Test Suite for AbstractService"""

    """
    __getattr__
    """
    # def test_get_attr_success_return_service(self):
    #     PylaasCore._init(self.datasets_path + '/container/definitions.yml')
    #     dummy = PylaasCore.get_service('dummy')
    #     dummyC = dummy.test_magic_service_injection()
    #     assert isinstance(dummyC, DummyConfigurable)
    #
    # def test_get_attr_with_unknown_method_raise_RuntimeError(self):
    #     PylaasCore._init(self.datasets_path + '/container/definitions.yml')
    #     dummy = PylaasCore.get_service('dummy')
    #     with pytest.raises(RuntimeError, match="service method 'bad_method_format' missing from class"):
    #         dummy.bad_method_format()
