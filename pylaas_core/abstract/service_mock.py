from unittest.mock import MagicMock


class ServiceMock(MagicMock):

    def get_method_call_args(self, method, index_call=0):
        """
        Args:
            method (string) : method name
            index_call (int): index

        Returns:
            method call args
        """
        if hasattr(self, method):
            mock = getattr(self, method)
            if index_call < len(mock.call_args_list):
                return mock.call_args_list[index_call][0]
            raise RuntimeError("no #{} method '{}' registered call".format(index_call, method))
        raise RuntimeError("no registered calls for method {}".format(method))
