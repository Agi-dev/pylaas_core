import pytest

from pylaas_core.abstract.abstract_test_case import AbstractTestCase
from pylaas_core.pylaas_core import PylaasCore
from pylaas_core.technical.container import Container
from tests.fixtures.data_sets.service.dummy.dummy import Dummy


class TestPylaasCore(AbstractTestCase):
    """
    __new__
    """

    def test_new_raise_TypeError(self):
        """Test unique instance creation"""
        with pytest.raises(TypeError):
            PylaasCore()

    """
    _init
    """

    def test__init_success(self):
        PylaasCore._init({'services': {'a service': 'data'}})
        expected = {'configurations': {}, 'services': {'a service': 'data'}}
        assert expected == PylaasCore._container._definitions

    """
    get_container
    """

    def test_get_container(self):
        PylaasCore._init({'services': 'a service'})
        assert isinstance(PylaasCore.get_container(), Container)

    """
    get_service
    """

    def test_get_service(self):
        PylaasCore._init(self.datasets_path + '/container/definitions.yml')
        assert isinstance(PylaasCore.get_service('dummy'), Dummy)
