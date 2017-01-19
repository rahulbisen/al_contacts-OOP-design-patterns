#! /usr/bin/env python


class FormatException(Exception):
    """
    Exception raised by Formats class and its subclasses.
    """
    pass


class Format:
    """
    This class is an observer class for observable 'Formats' class.
    This implements a notify() method that the 'Formats' class uses to send notifications.
    This is also an observable class for reader/writer for a specific data Format.
    A ReaderWriter class can register itself with this class using the register_rw() method
    At a time, only one read/write class remains registered, the last one, under the assump-
    tion that this this project has not specified using multiple readers/writers for a format.
    A ReaderWriter class can un-register itself using the unregister_rw() method
    This class can send notifications to the registered reader/writer class using notify_rw() method
    """
    def __init__(self, formats):
        """
        :Params:
            formats: `al_contacts.formats.Formats`
                object of the 'al_contacts.formats.Formats' observer class to which this class' object registers.
        """
        self.rw = None
        formats.register_format(self)


    def __str__(self):
        return 'base'


    def __repr__(self):
        return 'base'


    def register_rw(self, rw):
        """
        A 'al_contacts.reader_writer.ReaderWriter' class instance for a specific format can register
        itself with this class using the register_rw() method. At any time, only one
        reader/writer instance remains registered.

        :Params:
            rw: `al_contacts.reader_writer.ReaderWriter`
                object of one of the 'reader/writer' classes which registers with this class.
        """
        if self.rw == rw:
            raise FormatException('"{0}" is already Registered with "{1}" format.'.format(self.rw, self))
        else:
            if self.rw:
                print('Unregistering "{0}" for format "{1}"'.format(self.rw, self))
            print('Registering "{0}" for format "{1}"'.format(rw, self))
            self.rw = rw


    def unregister_rw(self, rw):
        """
        A 'al_contacts.reader_writer.ReaderWriter' class instance for a specific format can unregister
        itself with this class using the unregister_rw() method. At any time, only one
        reader/writer instance remains registered.

        :Params:
            rw: `al_contacts.reader_writer.ReaderWriter`
                object of one of the 'reader/writer' classes which registers with this class.
        """
        if self.rw == rw:
            self.rw = None
            print('Unregistered "{0}"!. There is no reader/writer registered for "{1}" format currently'.format(rw, self))
        else:
            raise FormatException('"{0}" is not registered as the current reader/writer for "{1}" format'.format(rw, self))

    
    def notify_rw(self, action=''):
        """
        This class can send notifications to the registered reader/writer classes using notify_rw() method
        The reader/writer object  must implement notify() method

        :Params:
            action: `str`
                action is one of the actions supported by `al_contacts.reader_writer.ReaderWriter` class.
        """
        if self.rw:
            self.rw.notify(self, action)
        else:
            raise FormatException('There is no reader/writer registered for "{0}" format currently'.format(self))


    def notify(self, formats, *args, **kwargs):
        """
        This is the method that observable 'al_contacts.formats.Formats' class will use to send
        notifications to this class.
        This class will mostly forward notifications to the format reader/writer class.

        :Params:
            formats: `al_contacts.formats.Formats`
                object of the 'al_contacts.formats.Formats' observer class to which this class' object registers.
                This could be used later to communicate back.
        """
        if self.rw:
            print('"{0}" is registered with "{1}" format!'.format(self.rw, self))
        else:
            raise FormatException('There is no reader/writer registered for "{0}" format currently'.format(self))


class PickleFormat(Format):
    """
    This class inherits from 'Format' class that defines common methods for all format classes.
    This class is an observer class, for Pickle format, for the observable 'Formats' class
    This is also an observable class for reader/writer for Pickle data format.
    """
    def __str__(self):
        return 'pickle'

    def __repr__(self):
        return 'pickle'


class JsonFormat(Format):
    """
    This class inherits from 'Format' class that defines common methods for all format classes.
    This class is an observer class, for Json format, for the observable 'Formats' class
    This is also an observable class for reader/writer for Json data format.
    """
    def __str__(self):
        return 'json'

    def __repr__(self):
        return 'json'