#!/usr/bin/env python2
# -*- encoding:utf-8 -*-

"""
Polyshaper exceptions
"""


class PolyshaperError(Exception):
    """ The base class of all exceptions in the polyshaper plugin

    Each exception should have a unique associated error code
    """

    def __init__(self, error_code):
        """ Constructor

        :param error_code: the error code associated to this exception
        :type error_code: int, >= 1
        """
        Exception.__init__(self)
        self.error_code = error_code

    def exit_code(self):
        """ Returns the error code with which program should terminate

        :return: the error code
        :rtype: int
        """

        return self.error_code

    def to_string(self):
        """ Converts to string
        """

        return _("Unknown error, error code: ") + str(self.error_code)


class PolyshaperIOError(PolyshaperError):
    """ The exception generated when wrong parameters are passed
    """

    def __init__(self, filename, message):
        """ Constructor

        :param filename: the name of the file on which IO error occurred
        :type filename: string
        :param message: the error message
        :type message: string
        """
        PolyshaperError.__init__(self, 1)

        self.filename = filename
        self.message = message

    def to_string(self):
        """ Converts to string
        """

        return _("Error while operating on file ") + self.filename + ", " + self.message


class UnrecognizedSVGElement(PolyshaperError):
    """ The exception generated when an unknown svg element is selected
    """

    def __init__(self, element):
        """ Constructor

        :param element: the name of the element that is not recognized
        :type element: string
        """
        PolyshaperError.__init__(self, 2)

        self.element = element

    def to_string(self):
        """ Converts to string
        """

        return _("Unknown SVG element: ") + self.element


class InvalidCuttingPath(PolyshaperError):
    """ The exception thrown when trying to generate tool path for cutting from an invalid path
    """

    def __init__(self, reason):
        """ Constructor

        :param reason: the reason why the path is invalid
        :type reason: string
        """
        PolyshaperError.__init__(self, 3)

        self.reason = reason

    def to_string(self):
        """ Converts to string
        """

        return _("Invalid cutting path, reason: ") + self.reason


class InvalidWorkpieceDimensions(PolyshaperError):
    """ The exception generated when the workpiece does not fit the machine
    """

    def __init__(self, machine_width, machine_height):
        """ Constructor

        :param machine_width: the width of the machine
        :type machine_width: float (mm)
        :param machine_height: the height of the machine
        :type machine_height: float (mm)
        """
        PolyshaperError.__init__(self, 4)

        self.machine_width = machine_width
        self.machine_height = machine_height

    def to_string(self):
        """ Converts to string
        """

        return (_("Piece too big: maximum allowed dimensions for the selected machine is ") +
                "{:.1f}X{:.1f}".format(self.machine_width, self.machine_height))
