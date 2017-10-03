import abc


class ContainerInterface(abc.ABC):
    """
    Container interface
    """

    @abc.abstractmethod
    def add_definitions(self, definitions):
        """Add definition to container
        Args:
            definitions (dict|string): list of definitions

        Returns:
            ContainerInterface
        """
        pass

    @abc.abstractmethod
    def get_definitions(self):
        """Get container definitions

        Returns:
            definitions (dict): list of definitions
        """
        pass

    @abc.abstractmethod
    def has(self, def_id):
        """Returns true if the container can return an entry for the given identifier.

        Args:
            def_id: Identifier of the entry to look for

        Returns:
            bool
        """
        pass

    @abc.abstractmethod
    def get(self, def_id):
        """Finds an entry of the container by its identifier and returns it.

        Args:
            def_id: Identifier of the entry to look for.

        Returns:
            ServiceInterface
        """
        pass
