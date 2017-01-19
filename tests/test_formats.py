#!/usr/bin/env python

import sys
import os
import unittest
import tempfile

# import classes from al_contacts.reader_writer
from al_contacts.formats import Formats
from al_contacts.formats import FormatsException


class MockFormat:
    """
    This is a mock class for al_contacts.format.Format
    """
    def __str__(self):
        return 'MockFormat'

    def __repr__(self):
        return 'MockFormat'

    def notify(self, *args, **kwargs):
        pass


class TestFormats(unittest.TestCase):
    """
    Test Cases for the class al_contacts.formats.Formats
    """
    @classmethod
    def setUpClass(cls):
        cls.mockFormat = MockFormat()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.formats = Formats()


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.formats.Formats object creation/initialisation    #
    ######################################################################

    def testInitialisationForFormatsInstanceVariable(self):
        """
        test Initialisation For 'formats' Instance Variable
        """
        self.assertEqual(self.formats.formats, [])


    ######################################################################
    # tests for al_contacts.formats.Formats.register_format()            #
    ######################################################################

    def testRegisterFormatWithAlreadyRegisteredFormat(self):
        """
        test al_contacts.formats.Formats.register_format() with an already
        registered format.
        """
        self.formats.register_format(self.mockFormat)
        self.assertIn(self.mockFormat, self.formats.formats)
        self.assertRaises(FormatsException, self.formats.register_format, self.mockFormat)


    def testRegisterFormatWithUnRegisteredFormat(self):
        """
        test al_contacts.formats.Formats.register_format() with an unregistered format.
        """
        self.assertNotIn(self.mockFormat, self.formats.formats)
        self.formats.register_format(self.mockFormat)
        self.assertIn(self.mockFormat, self.formats.formats)


    ######################################################################
    # tests for al_contacts.formats.Formats.unregister_format()          #
    ######################################################################

    def testUnRegisterFormatWithUnRegisteredFormat(self):
        """
        test al_contacts.formats.Formats.unregister_format() with an unregistered format.
        """
        self.assertNotIn(self.mockFormat, self.formats.formats)
        self.assertRaises(FormatsException, self.formats.unregister_format, self.mockFormat)


    def testUnRegisterFormatWithRegisteredFormat(self):
        """
        test al_contacts.formats.Formats.unregister_format() with a registered format.
        """
        self.formats.register_format(self.mockFormat)
        self.assertIn(self.mockFormat, self.formats.formats)
        self.formats.unregister_format(self.mockFormat)
        self.assertNotIn(self.mockFormat, self.formats.formats)


    ######################################################################
    # tests for al_contacts.formats.Formats.notify_formats()             #
    ######################################################################

    def testNotifyFormatsWithNoRegisteredFormats(self):
        """
        test al_contacts.formats.Formats.notify_formats() with no registered formats.
        """
        self.assertEqual(self.formats.formats, [])
        self.assertRaises(FormatsException, self.formats.notify_formats)


if __name__ == '__main__':
    unittest.main()