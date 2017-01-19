#! /usr/bin/env python

import os
from contextlib import contextmanager
import json
import pickle


class ReaderWriterException(Exception):
    """
    Exception raised by ReaderWriter and its subclasses.
    """
    pass


class ReaderWriter:
    """
    This class is an observer class for observable 'Format' class and has to ne instantiated
    with an object of one of the 'Format' classes to support.
    This implements a notify() method that the 'Format' class uses to send notifications.
    It also defines serialise() and deserialise() methods for a specific format.
    """
    def __init__(self, format, data=[], filepath=''):
        """
        :Params:
            format: `al_contacts.format.Format`
                object of one of the 'Format' classes to which the readre/writer object registers.

            data: `list`
                list of dictionaries of key-value pairs, with keys = ['name', 'address', 'phone']
                defaults to an empty list.

            filepath: `string`
                file path where the data is to be written to or read from.

        """
        self.data = data
        self.filepath = filepath
        self.actions = ['serialise', 'deserialise']
        format.register_rw(self)


    def __str__(self):
        return 'base reader/writer observer'


    def __repr__(self):
        return 'base reader/writer observer'


    def notify(self, format, action, *args, **kwargs):
        """
        This is the method that observable class 'Format' will use to send notifications to
        this observer class.

        :Params:
            format: `al_contacts.format.Format`
                object of one of the 'Format' classes to which the readre/writer object registers.
                This can be used in case the caller 'Format' object needs to be notified back.
            action: `str`
                action is one of the actions supported by this class.
        """
        if not action:
            raise ReaderWriterException('Specify an <action> from {0} to perform"'.format(self.actions))
        if action not in self.actions:
            raise ReaderWriterException('Operation "{0}" is not defined in "{1}"'.format(action, self))

        if action == 'serialise':
            self.serialise()
        elif action == 'deserialise':
            self.deserialise()


    def serialise(self):
        """
        Serialise data(self.data) to a file
        This method needs to be implemented by the subclasses.

        """
        print('ReaderWriter.serialise() needs to be implemented by the subclasses')
        pass


    def deserialise(self):
        """
        Recover the original objects / object-types from the serialised data in self.filepath
        This method needs to be implemented by the subclasses.
        """
        print('ReaderWriter.deserialise() needs to be implemented by the subclasses')
        pass


class JsonRW(ReaderWriter):
    """
    This class inherits from 'ReaderWriter' class that defines common methods for all
    reader/writer classes.
    This class is an observer class for observable 'Format' class for Json Format.
    It implements serialise() and deserialise() methods for Json Format.
    """
    def __str__(self):
        return 'json reader/writer'


    def __repr__(self):
        return 'json reader/writer'


    def serialise(self):
        """
        Implementation of the base class serialise() method for the JsonRW class.
        Serialise passed data to json format and save at filepath.
        """
        if not self.data:
            raise ReaderWriterException('self.data empty for "{0}" instance'.format(self))

        if not self.filepath:
            raise ReaderWriterException('self.filepath, to write json data to, empty for "{0}" instance'.format(self))

        with open(self.filepath, 'w') as fp:
            json.dump(self.data, fp, encoding='utf-8')

        print('Serialised Json data into the file:{0}'.format(self.filepath))


    def deserialise(self):
        """
        Implementation of the base class deserialise() method for the JsonRW class.
        Recover the original python objects from the json data at self.filepath
        """

        if not self.filepath:
            raise ReaderWriterException('self.filepath, to read json data from, empty for "{0}" instance'.format(self))

        if not os.path.exists(self.filepath):
            raise ReaderWriterException('Specified path for deserialisation of data does not exist: "{0}"'.format(self.filepath))

        with open(self.filepath, 'r') as fp:
            self.data = json.load(fp, encoding='utf-8')

        print('De-serialised Json data from the file:{0}'.format(self.filepath))


class PickleRW(ReaderWriter):
    """
    This class inherits from 'ReaderWriter' class that defines common methods for all
    reader/writer classes.
    This class is an observer class for observable 'Format' class for Pickle Format.
    It implements serialise() and deserialise() methods for Pickle Format.
    """
    def __str__(self):
        return 'Pickle reader/writer'


    def __repr__(self):
        return 'Pickle reader/writer'


    def serialise(self):
        """
        Implementation of the base class serialise() method for the PickleRW class.
        Serialise passed data to Pickle format and save at filepath.
        """
        if not self.data:
            raise ReaderWriterException('self.data empty for "{0}" instance'.format(self))

        if not self.filepath:
            raise ReaderWriterException('self.filepath, to write json data to, empty for "{0}" instance'.format(self))

        with open(self.filepath, 'w') as fp:
            pickle.dump(self.data, fp)

        print('Serialised Json data into the file:{0}'.format(self.filepath))


    def deserialise(self):
        """
        Implementation of the base class deserialise() method for the PickleRW class.
        Recover the original python objects from the Pickle data at self.filepath
        """
        if not self.filepath:
            raise ReaderWriterException('self.filepath, to read json data from, empty for "{0}" instance'.format(self))

        if not os.path.exists(self.filepath):
            raise ReaderWriterException('Specified path for deserialisation of data does not exist: "{0}"'.format(self.filepath))

        with open(self.filepath, 'r') as fp:
            self.data = pickle.load(fp)

        print('De-serialised Json data from the file:{0}'.format(self.filepath))