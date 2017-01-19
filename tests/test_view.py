#!/usr/bin/env python

import sys
import os
import unittest
import tempfile

# import classes from al_contacts.view
from al_contacts.view import ViewException
from al_contacts.view import View
from al_contacts.view import TableView
from al_contacts.view import ListView


class MockViews:
    """
    This is a mock class for al_contacts.format.Format
    """
    def __str__(self):
        return 'MockViews'

    def __repr__(self):
        return 'MockViews'

    def register_view(self, rw):
        pass


class TestView(unittest.TestCase):
    """
    Test Cases for the class al_contacts.view.View
    """
    @classmethod
    def setUpClass(cls):
        cls.mockViews = MockViews()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.view = View(self.mockViews)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass

    ######################################################################
    # test al_contacts.view.View object creation/initialisation          #
    ######################################################################

    def testStringRepresentationOnInstantiation(self):
        """
        test String Representation On Instantiation
        """
        self.assertEqual(str(self.view), 'base view observer')


    ######################################################################
    # tests for al_contacts.view.View.notify()                           #
    ######################################################################

    def testNotifyWithNonListData(self):
        """
        test al_contacts.view.View.notify() with non-list data.
        """
        self.assertRaises(ViewException, self.view.notify, self.mockViews, 'Invalid Data')


    def testNotifyWithValidListDate(self):
        """
        test al_contacts.view.View.notify() with valid list data.
        """
        self.assertEqual(self.view.notify(self.mockViews, []), None)


class TestTableView(unittest.TestCase):
    """
    Test Cases for the class al_contacts.view.JsonRW
    """

    @classmethod
    def setUpClass(cls):
        cls.mockViews = MockViews()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.tv = TableView(self.mockViews)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.view.TableView object creation/initialisation     #
    ######################################################################

    def testStringRepresentationOnInstantiation(self):
        """
        test String Representation On Instantiation
        """
        self.assertEqual(str(self.tv), 'table')


    def test_DisplayReturnsNone(self):
        """
        test al_contacts.view.TableView._display() with some data.
        """
        self.assertEqual(self.tv._display([]), None)


class TestListView(unittest.TestCase):
    """
    Test Cases for the class al_contacts.view.JsonRW
    """

    @classmethod
    def setUpClass(cls):
        cls.mockViews = MockViews()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.lv = ListView(self.mockViews)


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.view.ListView object creation/initialisation      #
    ######################################################################

    def testStringRepresentationOnInstantiation(self):
        """
        test String Representation On Instantiation
        """
        self.assertEqual(str(self.lv), 'list')


    def test_DisplayReturnsNone(self):
        """
        test al_contacts.view.ListView._display() with some data.
        """
        self.assertEqual(self.lv._display([]), None)



if __name__ == '__main__':
    unittest.main()