#! /usr/bin/env python


class FormatsException(Exception):
    """
    Exception raised by Formats class.
    """
    pass


class Formats:
    """
    This is an observable class for formats.
    Any format class can register itself with this class using the register_format() method
    Formats can un-register themselves using the unregister_format() method
    This class can send notifications to the format classes using notify_formats() method
    """
    def __init__(self):
        self.formats = []


    def __str__(self):
        return 'Formats'


    def __repr__(self):
        return 'Formats'


    def register_format(self, format):
        """
        Any al_contacts.format.Format class instance can register itself with this class using the
        register_format() method

        :Params:
            format: `al_contacts.format.Format`
                object of one of the 'Format' classes which registers with this class.
        """
        if format in self.formats:
            raise FormatsException('"{0}" format already registered with "{1}"'.format(format, self))
        else:
            print('Registering "{0}" format with "{1}"'.format(format, self))
            self.formats.append(format)


    def unregister_format(self, format):
        """
        Any al_contacts.format.Format class can unregister itself with this class using the
        unregister_format() method

        :Params:
            format: `al_contacts.format.Format`
                object of one of the 'Format' classes which registers with this class.
        """
        if format in self.formats:
            print('Unregistering "{0}" format from "{1}"'.format(format, self))
            self.formats.pop(self.formats.index(format))
        else:
            raise FormatsException('"{0}" format is not registered with "{1}"'.format(format, self))

    
    def notify_formats(self, *args, **kwargs):
        """
        This class can send notifications to the 'Format' class objects using notify_formats() method
        The 'Format' class objects must implement notify() method
        """
        if not self.formats:
            raise FormatsException('There are no formats registered with "{0}" currently'.format(self))
        else:
            for aFormat in self.formats:
                aFormat.notify(self)