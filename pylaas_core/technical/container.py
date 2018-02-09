import yaml
import sys
from os import path

from pylaas_core.interface.core.service_interface import ServiceInterface
from pylaas_core.interface.technical.container_configurable_aware_interface import ContainerConfigurableAwareInterface
from pylaas_core.interface.technical.container_interface import ContainerInterface


class Container(ContainerInterface):
    """Container to handle DI

    Attributes:
        _definitions (dict) : list of container definitions
        _singletons (dict) : list of class singletons
    """

    def __init__(self) -> None:
        self._definitions = {}
        self._singletons = {}

    def add_definitions(self, definitions):
        """Add definition to container
        Args:
            definitions (dict|string): list of definitions

        Returns:
            ContainerInterface
        """
        if type(definitions) is not dict:
            if path.exists(definitions):
                with open(definitions, 'r') as f:
                    definitions = yaml.load(f)
            else:
                raise FileExistsError("Container definitions file '{}' does not exits".format(definitions))

        if self._definitions:
            if 'configurations' in definitions and definitions.get('configurations') is not None:
                self._definitions['configurations'].update(definitions['configurations'])
            if 'services' in definitions and definitions.get('services') is not None:
                self._definitions['services'].update(definitions['services'])
        else:
            self._definitions = {'configurations': {}, 'services': {}}
            self._definitions.update(definitions)

        return self

    def get_definitions(self):
        """Get container definitions

        Returns:
            definitions (dict): list of definitions
        """
        return self._definitions

    def has(self, def_id):
        """Returns true if the container can return an entry for the given identifier.

        Args:
            def_id: Identifier of the entry to look for

        Returns:
            bool
        """
        return def_id in self._definitions['services']

    def get(self, def_id):
        """Finds an entry of the container by its identifier and returns it.

        Args:
            def_id: Identifier of the entry to look for.

        Returns:
            ServiceInterface: singleton services
        """
        if not self.has(def_id):
            raise RuntimeError("service id '{}' does not exists".format(def_id))

        # check if service has been already created as a singleton
        if def_id not in self._singletons:
            parts = self._definitions['services'][def_id].split(".")
            module_name = ".".join(parts[:-1])
            class_name = parts[-1]
            __import__(module_name)
            service = getattr(sys.modules[module_name], class_name)
            service = service()
            if isinstance(service, ContainerConfigurableAwareInterface):
                service.set_configs(self._definitions['configurations'][def_id])
            self._singletons[def_id] = service

        return self._singletons[def_id]

    def clear(self, def_id) -> None:
        """Clear an entry of the container by its identifier

        Args:
            def_id: Identifier of the entry to look for.

        Returns:
            None
        """
        if def_id not in self._singletons:
            return
        del self._singletons[def_id]
