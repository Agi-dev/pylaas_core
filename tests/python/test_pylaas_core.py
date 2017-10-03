import pytest
from pylaas_core.pylaas_core import PylaasCore
from pylaas_core.technical.container import Container


class TestPylaasCore:
    """
    __new__
    """

    def test_new_raise_TypeError(self):
        """Test unique instance creation"""
        with pytest.raises(TypeError):
            PylaasCore()

    """
    init
    """

    def test_init_success(self):
        PylaasCore.init({'services': 'a service'})
        assert PylaasCore._container._definitions == {'services': 'a service'}

    """
    get_container
    """

    def test_get_container(self):
        PylaasCore.init({'services': 'a service'})
        assert isinstance(PylaasCore.get_container(), Container)
