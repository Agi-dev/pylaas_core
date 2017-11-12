import pytest

from abstract.abstract_service_unit_test import AbstractServiceUnitTest
from abstract.abstract_test_case import AbstractTestCase
from pylaas_core.pylaas_core import PylaasCore


class TestAbstractServiceUnitTest(AbstractTestCase):
    """Test Suite for AbstractServiceUnitTest"""

    def init_container(self):
        PylaasCore._init(self.datasets_path + '/container/definitions.yml')

    """
    __init__
    """

    def test_init_success(self):
        test = AbstractServiceUnitTest()
        assert test._service is None

    """
    setup_method
    """

    def test_setup_method_with_service_id_empty_raise_exception(self):
        test = AbstractServiceUnitTest()
        with pytest.raises(RuntimeError):
            test.setup_method('launch_exception')

    def test_setup_method_with_service_without_adapter(self):
        self.init_container()
        test = AbstractServiceUnitTest()
        test._service_id = 'dummy'
        test.setup_method('set_no_adapter')
        # check a mock adapter has not been set
        assert not test._service.has_adapter()

    def test_setup_method_with_service_with_adapter(self):
        self.init_container()
        test = AbstractServiceUnitTest()
        test._service_id = 'dummy_adapter'
        test.setup_method('set_adapter')
        # check a mock adapter has been set
        assert test._service.has_adapter()
