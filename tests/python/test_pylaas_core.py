from pylaas_core.pylaas_core import PylaasCore


class TestPylaasCore:
    """
    __new__
    """

    def test_new_create_unique_instance(self):
        """Test unique instance creation"""
        singleton1 = PylaasCore({})
        singleton2 = PylaasCore({'some configs'})
        assert singleton1 == singleton2
        assert singleton2._container._definitions == {}
