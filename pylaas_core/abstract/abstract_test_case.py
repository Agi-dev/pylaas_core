from pylaas_core.utils import *
import json
from os.path import exists, dirname


class AbstractTestCase:
    """Abstract class to handle common functionality"""

    def assert_equals_resultset(self, actual):
        """assert result set equality

        Build resulset name from filename. Compare expected to resultset for test method
        """

        # build resultset filename from caller filename
        calframe = inspect.getouterframes(inspect.currentframe(), 2)
        method_name = calframe[1][3]
        filename = calframe[1].filename
        lineno = calframe[1].lineno
        f = filename.split('/')
        resultset_filename = "{}/{}/rs_{}".format(self.resultsets_path, f[-2], f[-1]).replace('.py', '.json')

        # get expected result sets from file
        if exists(resultset_filename):
            with open(resultset_filename) as json_file:
                list_resultsets = json.load(json_file)
        else:
            list_resultsets = {}

        # get result for method test
        expected = None
        if method_name in list_resultsets:
            expected = list_resultsets[method_name]

        # assert
        try:
            assert expected == actual
        except AssertionError as e:
            # build fix result set
            tmp_resultset_filename = resultset_filename.replace('.json', '_fix_DONOTCOMMIT.txt')

            with open(tmp_resultset_filename, 'a') as f:
                f.write('"{}": '.format(method_name))
                json.dump(actual, f)
                f.write(",\n")

            s({
                'file': "{} line {}".format(filename, lineno),
                'test': method_name,
                'expected': expected if expected else 'Need to be set',
                'actual': actual,
                'fixed into': tmp_resultset_filename,
                'file to edit': resultset_filename
            })
            raise e

    @property
    def fixtures_path(self):
        """Get fixture path

        Returns:
            string: path to fixtures
        """
        return dirname(__file__) + '/../../tests/fixtures'

    @property
    def resultsets_path(self):
        """Get result sets path

        Returns:
            string: path to result sets
        """
        return "{}/result_sets".format(self.fixtures_path)

    @property
    def datasets_path(self):
        """get data sets path

        Returns:
            string: path to data sets
        """
        return "{}/data_sets".format(self.fixtures_path)
