import inspect
import json
import unittest
import pickle
import errno
from pylaas_core import Debug
from os import makedirs
from os.path import exists, dirname
from abc import ABC


class AbstractTestCase(ABC, unittest.TestCase):
    """Abstract class to handle common functionality"""

    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self._fixture_path = None
        self._calframe = None

    def assert_equals_resultset(self, actual):
        """assert result set equality

        Build resulset name from filename. Compare expected to resultset for test method
        """

        # build resultset filename from caller filename
        method_name = self._get_calling_method_name()
        filename = self._get_calling_filename()
        lineno = self._get_calling_lineno()
        f = filename.split('/')
        resultset_filename = "{}/{}/rs_{}".format(self.resultsets_path, f[-2], f[-1]).replace('.py', '.json')
        self._check_file_can_be_created(resultset_filename)

        # get expected result sets from file
        if exists(resultset_filename):
            with open(resultset_filename) as json_file:
                list_resultsets = json.load(json_file)
        else:
            # create missing file
            with open(resultset_filename, 'a') as f:
                json.dump({}, f)
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

            Debug.s({
                'file'        : "{} line {}".format(filename, lineno),
                'test'        : method_name,
                'expected'    : expected if expected else 'Need to be set',
                'actual'      : actual,
                'fixed into'  : tmp_resultset_filename,
                'file to edit': resultset_filename
            })
            raise e

    def load_expected(self, actual):
        """
        load expected for current testing method
        Args:
            actual:

        Returns:

        """
        expected_filename = self._get_expected_filename()
        if exists(expected_filename):
            with open(expected_filename) as pickle_file:
                return pickle.load(open(expected_filename, 'rb'))
        raise FileNotFoundError('expected file {} not found, create it with save_expected'.format(expected_filename))

    def save_expected(self, actual):
        """
        save actual into expected filename
        Args:
            actual:

        Returns:

        """
        expected_filename = self._get_expected_filename()
        self._check_file_can_be_created(expected_filename)
        pickle.dump(actual, open(expected_filename, 'wb+'))
        Debug.s({
            'actual'    : actual,
            'saved into': expected_filename,
        })
        raise AssertionError('You are saving expected result, verify dump.')

    def _get_expected_filename(self) -> str:
        """
        get expected filename for current testing method
        Returns:
            str : filename
        """
        method_name = self._get_calling_method_name()
        filename = self._get_calling_filename()
        f = filename.split('/')
        return "{}/expected/{}/{}/{}.pickle".format(self.resultsets_path, f[-2], f[-1], method_name).replace('.py', '')

    def _get_calframe(self):
        """
        find calling frame from stack calls
        Returns:
            FrameInfo : frame
        """
        self._calframe = None
        if not self._calframe:
            # find calling frame
            calframe = inspect.getouterframes(inspect.currentframe(), 2)
            # search caller filename (=> first which is not current file)
            for frame in calframe:
                if not frame.filename.find('/abstract_test_case.py') > 0:
                    self._calframe = frame
                    break
            if None == self._calframe:
                raise ValueError('Unable to determine calling frame')
        return self._calframe

    def _get_calling_method_name(self) -> str:
        """
        Returns:
            str: calling method name
        """
        return self._get_calframe()[3]

    def _get_calling_filename(self) -> str:
        """
        Returns:
            str: calling filename
        """
        return self._get_calframe().filename

    def _get_calling_lineno(self) -> str:
        """
        Returns:
            str: calling line number
        """
        return self._get_calframe().lineno

    def _check_file_can_be_created(self, filename) -> None:
        """
        create missing directories for filename
        Args:
            filename (string) : fullpath filename

        Returns:
            None
        """
        if not exists(filename):
            try:
                makedirs(dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

    @property
    def fixtures_path(self):
        """Get fixture path

        Returns:
            string: path to fixtures
        """
        if not self._fixture_path:
            filename = self._get_calling_filename()
            pos = filename.find('/tests')
            if not pos > 0:
                raise ValueError('Unable to determine root tests path from {}'.format(filename))
            self._fixture_path = '{}/tests/fixtures'.format(filename[:pos])

        return self._fixture_path

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
