#!/usr/bin/env python

import sys
import os
import unittest
import tempfile

# import classes from al_contacts.reader_writer
from al_contacts.views import Views
from al_contacts.views import ViewsException


class MockView:
    """
    This is a mock class for al_contacts.view.View
    """
    def __str__(self):
        return 'MockView'

    def __repr__(self):
        return 'MockView'

    def notify(self, *args, **kwargs):
        pass


class TestViews(unittest.TestCase):
    """
    Test Cases for the class al_contacts.views.Views
    """
    @classmethod
    def setUpClass(cls):
        cls.mockView = MockView()


    @classmethod
    def tearDownClass(cls):
        pass


    def setUp(self):
        self.views = Views()


    def tearDown(self):
        # just passing as python will do the garbage collection.
        pass


    ######################################################################
    # test al_contacts.views.Views object creation/initialisation        #
    ######################################################################

    def testInitialisationForViewsInstanceVariables(self):
        """
        test Initialisation For 'views' Instance Variables
        """
        self.assertEqual(self.views.views, [])
        self.assertEqual(self.views.data, [])


    def testInstantiationWithInvaldData(self):
        """
        test Initialisation with Invalid(non list) data
        """
        self.assertRaises(ViewsException, Views, 'non list data')

    ######################################################################
    # tests for al_contacts.views.Views.register_view()                  #
    ######################################################################

    def testRegisterViewWithAlreadyRegisteredView(self):
        """
        test al_contacts.views.Views.register_view() with an already registered view.
        """
        self.views.register_view(self.mockView)
        self.assertIn(self.mockView, self.views.views)
        self.assertRaises(ViewsException, self.views.register_view, self.mockView)


    def testRegisterViewWithUnregisteredView(self):
        """
        test al_contacts.views.Views.register_view() with an unregistered view.
        """
        self.assertNotIn(self.mockView, self.views.views)
        self.views.register_view(self.mockView)
        self.assertIn(self.mockView, self.views.views)


    ######################################################################
    # tests for al_contacts.views.Views.unregister_view()                #
    ######################################################################

    def testUnregisterViewWithUnregisteredView(self):
        """
        test al_contacts.views.Views.unregister_view() with an unregistered view.
        """
        self.assertNotIn(self.mockView, self.views.views)
        self.assertRaises(ViewsException, self.views.unregister_view, self.mockView)


    def testUnregisterViewWithRegisteredView(self):
        """
        test al_contacts.views.Views.unregister_view() with a registered view.
        """
        self.views.register_view(self.mockView)
        self.assertIn(self.mockView, self.views.views)
        self.views.unregister_view(self.mockView)
        self.assertNotIn(self.mockView, self.views.views)


    ######################################################################
    # tests for al_contacts.views.Views.notify_views()                   #
    ######################################################################

    def testNotifyViewsWithNoRegisteredViews(self):
        """
        test al_contacts.views.Views.notify_views() with no registered views.
        """
        self.assertEqual(self.views.views, [])
        self.assertRaises(ViewsException, self.views.notify_views)


    def testNotifyViewsWithRegisteredViewsAndNonEmptyStrViewName(self):
        """
        test al_contacts.views.Views.notify_views() with registered views and
        a non-empty non-string view argument.
        """
        self.views.register_view(self.mockView)
        self.assertIn(self.mockView, self.views.views)
        self.assertRaises(ViewsException, self.views.notify_views, ['aaaaaaa'])


    def testNotifyViewsWithRegisteredViewsAndInvalidViewName(self):
        """
        test al_contacts.views.Views.notify_views() with registered views and a
        non existing view argument.
        """
        self.views.register_view(self.mockView)
        self.assertIn(self.mockView, self.views.views)
        self.assertRaises(ViewsException, self.views.notify_views, 'xxxxxxxx')




if __name__ == '__main__':
    unittest.main()