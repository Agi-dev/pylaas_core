"""
This module implements the alfred core system.

Pylaas(<config: file|{}>)
"""
from pylaas_core.technical.container import Container


class PylaasCore:
    _instance = None

    def __new__(cls, definitions):
        """Force singleton of this class

        Initialize container with it's definition
        """
        if not cls._instance:
            cls._instance = super(PylaasCore, cls).__new__(cls)
            cls._container = Container().add_definition(definitions)
        return cls._instance
