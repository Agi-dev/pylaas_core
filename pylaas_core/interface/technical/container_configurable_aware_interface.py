import abc


class ContainerConfigurableAwareInterface(abc.ABC):
    """
    Container interface
    """

    @abc.abstractmethod
    def set_configs(self, configurations):
        """Set config to a service

        Args:
            configurations (mixed): service configurations

        Returns:
            ServiceInterface
        """
        pass
