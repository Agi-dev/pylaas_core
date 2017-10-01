from pylaas_core.pylaas import Pylaas


class TestPylaas:
    """
    __new__
    """

    def test_new_create_unique_instance(self):
        """Test unique instance creation"""
        singleton1 = Pylaas({})
        singleton2 = Pylaas({'some configs'})
        assert singleton1 == singleton2
        assert singleton2._container._definitions == {}
