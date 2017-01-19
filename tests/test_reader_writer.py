#!/usr/bin/env python

import sys
import os
import unittest
import tempfile
import json
import pickle

# import classes from al_contacts.reader_writer
from al_contacts.reader_writer import ReaderWriterException
from al_contacts.reader_writer import ReaderWriter
from al_contacts.reader_writer import JsonRW
from al_contacts.reader_writer import PickleRW


class MockFormat:
    """
    This is a mock class for al_contacts.format.Format
    """
    def __str__(self):
        return 'MockFormat'

    def __repr__(self):
        return 'MockFormat'

    def register_rw(self, rw):
        pass


class TestReaderWriter(unittest.TestCase):
    """
    Test Cases for the class al_contacts.reader_writer.ReaderWriter
    """
    @classmethod
    def setUpClass(cls):
        cls.mockFormat = MockFormat()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.rw = ReaderWriter(self.mockFormat)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass

    ######################################################################
    # test al_contacts.reader_writer.ReaderWriter instance initialisation#
    ######################################################################

    def testDefaultInitialisationForDataArgument(self):
        """
        test Default Initialisation For 'data' Argument
        """
        self.assertEqual(self.rw.data, [])


    def testDefaultInitialisationForFileArgument(self):
        """
        test Default Initialisation For 'filepath' Argument
        """
        self.assertEqual(self.rw.filepath, '')


    def testInitialisationForActionsInstanceVariable(self):
        """
        test Initialisation For 'actions' Instance Variable
        """
        self.assertEqual(self.rw.actions, ['serialise', 'deserialise'])


    ######################################################################
    # tests for al_contacts.reader_writer.ReaderWriter.notify()          #
    ######################################################################

    def testNotifyWithActionNone(self):
        """
        test al_contacts.reader_writer.ReaderWriter.notify() with action arg is None.
        """
        self.assertRaises(ReaderWriterException, self.rw.notify, self.mockFormat, None)


    def testNotifyWithInvalidActionName(self):
        """
        test al_contacts.reader_writer.ReaderWriter.notify() when action arg is invalid action name.
        """
        invalidActionName = 'xxxxxxxxx'
        self.assertRaises(ReaderWriterException, self.rw.notify, self.mockFormat, invalidActionName)


    def testNotifyWithValidAction(self):
        """
        test al_contacts.reader_writer.ReaderWriter.notify() with valid action arg.
        """
        validAction = 'serialise'
        self.assertIn(validAction, self.rw.actions)
        self.assertEqual(self.rw.notify(self.mockFormat, validAction), None)


class TestJsonRW(unittest.TestCase):
    """
    Test Cases for the class al_contacts.reader_writer.JsonRW
    """


    @classmethod
    def setUpClass(cls):
        cls.mockFormat = MockFormat()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.jrw = JsonRW(self.mockFormat)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # tests for al_contacts.reader_writer.JsonRW.serialise()             #
    ######################################################################

    def testSerialiseWithEmptyOrNoneData(self):
        """
        test al_contacts.reader_writer.JsonRW.serialise() with empty/None data.
        """
        filePathTmp = tempfile.mkstemp(prefix='al_contacts_test_')[1]
        self.jrw.filepath = filePathTmp
        self.jrw.data = []
        self.assertRaises(ReaderWriterException, self.jrw.serialise)
        self.jrw.data = None
        self.assertRaises(ReaderWriterException, self.jrw.serialise)


    def testSerialiseWithEmptyOrNoneFilepath(self):
        """
        test al_contacts.reader_writer.JsonRW.serialise() with empty/None filepath.
        """
        self.jrw.data = {'a':'aa'}
        self.jrw.filepath = ''
        self.assertRaises(ReaderWriterException, self.jrw.serialise)
        self.jrw.filepath = None
        self.assertRaises(ReaderWriterException, self.jrw.serialise)


    def testSerialiseWithValidDataCreatesFileWritesValidData(self):
        """
        test serialise With Valid Data creates file and writes valid data
        """
        tmpDirPath = tempfile.mkdtemp(prefix='al_contacts_test')
        filePath = os.path.join(tmpDirPath, 'serialised.json')

        if  os.path.exists(tmpDirPath):
            data = [{'a':'aa'}, {'b': 'bb'}]
            self.jrw.data = data
            self.jrw.filepath = filePath
            self.jrw.serialise()
            self.assertTrue(os.path.exists(filePath))
            self.assertEqual(self.jrw.data, data)

        else:
            # this is to cover the case where the dir got deleted for some reason
            message = 'Temp fir:{0} did not get created or does not exist. Re-run the test.'.format(tmpDirPath)
            self.assertTrue(False, msg=message)


    ######################################################################
    # tests for al_contacts.reader_writer.JsonRW.deserialise()           #
    ######################################################################


    def testDesrialiseWithEmptyOrNoneFilepath(self):
        """
        test al_contacts.reader_writer.JsonRW.serialise() with empty/None filepath.
        """
        self.jrw.data = {'a':'aa'}
        self.jrw.filepath = ''
        self.assertRaises(ReaderWriterException, self.jrw.deserialise)
        self.jrw.filepath = None
        self.assertRaises(ReaderWriterException, self.jrw.deserialise)


    def testDeserialiseWithNonExistingFilepath(self):
        """
        test al_contacts.reader_writer.JsonRW.deserialise() with non-existing filepath.
        """
        self.jrw.data = {'a':'aa'}
        self.jrw.filepath = 'bla bla'
        self.assertRaises(ReaderWriterException, self.jrw.deserialise)


    def testDeserialiseWithExistingFilepathAndValidData(self):
        """
        test deserialise With Existing Filepath And Valid Data. Validate deserialised data
        """
        filePath = tempfile.mkstemp(prefix='al_contacts_test_')[1]
        if  os.path.exists(filePath):
            data = [{'a':'aa'}, {'b': 'bb'}]
            with open(filePath, 'w') as fp:
                json.dump(data, fp)

            self.jrw.filepath = filePath
            self.jrw.deserialise()
            self.assertEqual(self.jrw.data, data)

        else:
            # this is to cover the case where the dir got deleted for some reason
            message = 'Temp file:{0} did not get created or does not exist. Re-run the test.'.format(filePath)
            self.assertTrue(False, msg=message)


class TestPickleRW(unittest.TestCase):
    """
    Test Cases for the class al_contacts.reader_writer.PickleRW
    """


    @classmethod
    def setUpClass(cls):
        cls.mockFormat = MockFormat()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.prw = PickleRW(self.mockFormat)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # tests for al_contacts.reader_writer.PickleRW.serialise()           #
    ######################################################################

    def testSerialiseWithEmptyOrNoneData(self):
        """
        test al_contacts.reader_writer.PickleRW.serialise() with empty/None data.
        """
        filePathTmp = tempfile.mkstemp(prefix='share_test')[1]
        self.prw.filepath = filePathTmp
        self.prw.data = []
        self.assertRaises(ReaderWriterException, self.prw.serialise)
        self.prw.data = None
        self.assertRaises(ReaderWriterException, self.prw.serialise)


    def testSerialiseWithEmptyOrNoneFilepath(self):
        """
        test al_contacts.reader_writer.PickleRW.serialise() with empty/None filepath.
        """
        self.prw.data = [{'a':'aa'}]
        self.prw.filepath = ''
        self.assertRaises(ReaderWriterException, self.prw.serialise)
        self.prw.filepath = None
        self.assertRaises(ReaderWriterException, self.prw.serialise)


    def testSerialiseWithValidDataCreatesFileWritesValidData(self):
        """
        test serialise With Valid Data creates file and writes valid data
        """
        tmpDirPath = tempfile.mkdtemp(prefix='al_contacts_test')
        filePath = os.path.join(tmpDirPath, 'serialised.json')

        if  os.path.exists(tmpDirPath):
            data = [{'a':'aa'}, {'b': 'bb'}]
            self.prw.data = data
            self.prw.filepath = filePath
            self.prw.serialise()
            self.assertTrue(os.path.exists(filePath))
            self.assertEqual(self.prw.data, data)

        else:
            # this is to cover the case where the dir got deleted for some reason
            message = 'Temp fir:{0} did not get created or does not exist. Re-run the test.'.format(tmpDirPath)
            self.assertTrue(False, msg=message)

    ######################################################################
    # tests for al_contacts.reader_writer.PickleRW.deserialise()         #
    ######################################################################


    def testDesrialiseWithEmptyOrNoneFilepath(self):
        """
        test al_contacts.reader_writer.PickleRW.serialise() with empty/None filepath.
        """
        self.prw.filepath = ''
        self.assertRaises(ReaderWriterException, self.prw.deserialise)
        self.prw.filepath = None
        self.assertRaises(ReaderWriterException, self.prw.deserialise)


    def testDeserialiseWithNonExistingFilepath(self):
        """
        test al_contacts.reader_writer.PickleRW.deserialise() with non-existing filepath.
        """
        self.prw.filepath = 'bla bla'
        self.assertRaises(ReaderWriterException, self.prw.deserialise)


    def testDeserialiseWithExistingFilepathAndData(self):
        """
        test deserialise With Existing Filepath And Data. Validate deserialised data
        """
        filePath = tempfile.mkstemp(prefix='al_contacts_test_')[1]
        if  os.path.exists(filePath):
            data = [{'a':'aa'}, {'b': 'bb'}]
            with open(filePath, 'w') as fp:
                pickle.dump(data, fp)

            self.prw.filepath = filePath
            self.prw.deserialise()
            self.assertEqual(self.prw.data, data)

        else:
            # this is to cover the case where the dir got deleted for some reason
            message = 'Temp file:{0} did not get created or does not exist. Re-run the test.'.format(filePath)
            self.assertTrue(False, msg=message)


if __name__ == '__main__':
    unittest.main()