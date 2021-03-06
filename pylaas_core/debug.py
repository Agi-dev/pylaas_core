import inspect
from var_dump import var_dump
from sys import exit


class Debug:
    @staticmethod
    def d(var):
        """Shorcut to prints HTML human-readable information about a variable"""
        Debug.dump(var, False)

    @staticmethod
    def dd(var):
        """Shorcut to prints (and DIE) HTML human-readable information about a variable"""
        Debug.dump(var)

    @staticmethod
    def s(var):
        """Shorcut to prints human-readable information about a variable"""
        Debug.dump(var, False, False)

    @staticmethod
    def sd(var):
        """Shorcut to prints (and DIE) human-readable information about a variable"""
        Debug.dump(var, True, False)

    @staticmethod
    def dump(var, die=True, html=True):
        """Prints human-readable information about a variable

        Args:
            var (mixed): variable to dump
            die (bool) : exit script. Defaults True
            html (bool): dump as HTML. Defautls True
        """
        # build resultset filename from caller filename
        caller = inspect.getouterframes(inspect.currentframe(), 2)[2]
        print("\n\n=== DEBUG FROM {} (line {})\n".format(caller.filename, caller.lineno))
        if html:
            print('<pre>')

        var_dump(var)

        if html:
            print('</pre>')

        print("\n=== FIN DEBUG {} (line {})\n".format(caller.filename, caller.lineno))

        if die:
            exit()
