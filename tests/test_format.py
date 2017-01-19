#!/usr/bin/env python

import sys
import os
import unittest
import tempfile

# import classes from al_contacts.reader_writer
from al_contacts.format import Format
from al_contacts.format import FormatException
from al_contacts.format import JsonFormat
from al_contacts.format import PickleFormat


class MockFormats:
    """
    This is a mock class for al_contacts.formats.Formats
    """
    def __str__(self):
        return 'MockFormats'

    def __repr__(self):
        return 'MockFormats'

    def register_format(self, *args, **kwargs):
        pass


class MockReaderWriter:
    """
    This is a mock class for al_contacts.reader_writer.ReaderWriter
    """
    def __str__(self):
        return 'MockReaderWriter'

    def __repr__(self):
        return 'MockReaderWriter'

    def notify(self, *args, **kwargs):
        pass


class TestFormat(unittest.TestCase):
    """
    Test Cases for the class al_contacts.format.Format
    """
    @classmethod
    def setUpClass(cls):
        cls.mockReaderWriter = MockReaderWriter()
        cls.mockFormats = MockFormats()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.format = Format(self.mockFormats)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.format.Format object creation/initialisation      #
    ######################################################################

    def testInitialisationForFormatInstanceVariable(self):
        """
        test Initialisation For 'rw' Instance Variable
        """
        self.assertEqual(self.format.rw, None)


    ######################################################################
    # tests for al_contacts.format.Format.register_rw()                  #
    ######################################################################

    def testRegisterRWWithAlreadyRegisteredRW(self):
        """
        test al_contacts.format.Format.register_rw() with an already registered format.
        """
        self.format.register_rw(self.mockReaderWriter)
        self.assertEqual(self.mockReaderWriter, self.format.rw)
        self.assertRaises(FormatException, self.format.register_rw, self.mockReaderWriter)


    def testRegisterRWWithUnRegisteredRW(self):
        """
        test al_contacts.format.Format.register_rw() with an unregistered format.
        """
        self.assertNotEqual(self.mockReaderWriter, self.format.rw)
        self.format.register_rw(self.mockReaderWriter)
        self.assertEqual(self.mockReaderWriter, self.format.rw)


    ######################################################################
    # tests for al_contacts.format.Format.unregister_rw()                #
    ######################################################################

    def testUnRegisterRWWithUnRegisteredRW(self):
        """
        test al_contacts.format.Format.unregister_rw() with an unregistered format.
        """
        self.assertNotEqual(self.mockReaderWriter, self.format.rw)
        self.assertRaises(FormatException, self.format.unregister_rw, self.mockReaderWriter)


    def testUnRegisterRWWithRegisteredRW(self):
        """
        test al_contacts.format.Format.unregister_rw() with a registered format.
        """
        self.format.register_rw(self.mockReaderWriter)
        self.assertEqual(self.mockReaderWriter, self.format.rw)
        self.format.unregister_rw(self.mockReaderWriter)
        self.assertNotEqual(self.mockReaderWriter, self.format.rw)


    ######################################################################
    # tests for al_contacts.format.Format.notify_rw()                    #
    ######################################################################

    def testNotifyRWWithNoRegisteredRW(self):
        """
        test al_contacts.format.Format.notify_rw() with no registered rw.
        """
        self.assertEqual(self.format.rw, None)
        self.assertRaises(FormatException, self.format.notify_rw)


    ######################################################################
    # tests for al_contacts.format.Format.notify()                       #
    ######################################################################

    def testNotifyWithNoRegisteredRW(self):
        """
        test al_contacts.reader_writer.ReaderWriter.notify() with action arg is None.
        """
        self.assertEqual(self.format.rw, None)
        self.assertRaises(FormatException, self.format.notify, self.mockFormats)


class TestJsonFormat(unittest.TestCase):
    """
    Test Cases for the class al_contacts.format.JsonFormat
    """
    @classmethod
    def setUpClass(cls):
        cls.mockFormats = MockFormats()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.format = JsonFormat(self.mockFormats)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.format.JsonFormat object creation/initialisation  #
    ######################################################################

    def testStringRepresentationForNewInstance(self):
        """
        test String Representation For the New Instance
        """
        self.assertEqual(str(self.format), 'json')


class TestPickleFormat(unittest.TestCase):
    """
    Test Cases for the class al_contacts.format.PickleFormat
    """
    @classmethod
    def setUpClass(cls):
        cls.mockFormats = MockFormats()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.format = PickleFormat(self.mockFormats)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.format.PickleFormat object creation/initialisation#
    ######################################################################

    def testStringRepresentationForNewInstance(self):
        """
        test String Representation For the New Instance
        """
        self.assertEqual(str(self.format), 'pickle')


if __name__ == '__main__':
    unittest.main()