import abc


class ServiceInterface(abc.ABC):
    @abc.abstractmethod
    def set_adapter(self, adapter):
        """Set service adapter

        Args:
            adapter:

        Returns:
            cls
        """
        pass

    @abc.abstractmethod
    def get_adapter(self):
        """Get current adapter
        Returns:
            adapter
        """
        pass

    @abc.abstractmethod
    def has_adapter(self):
        """Check if an adapter exists
        Returns:
            bool
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def get_service(service_id) -> 'ServiceInterface':
        """
        Get service

        Args:
            service_id (string): service id to instantiate from container

        Returns:
            ServiceInterface
        """
