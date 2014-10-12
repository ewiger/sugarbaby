
class SugaBabeError(Exception):
    '''Custom hierarchy of errors'''


class MissingCliArgs(SugaBabeError):
    '''Error of parsing command-line arguments.'''


class DataModelError(SugaBabeError):
    pass
