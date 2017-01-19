#! /usr/bin/env python


class ViewException(Exception):
    """
    Exception raise from `al_contacts.view.View` class and its subclasses.
    Customise if required
    """
    pass


class View:
    """
    This class is an observer class for observable 'Views' class.
    This implements a notify() method that the 'Views' class uses to send notifications.
    It also defines a display() method that does the display from a specific view.
    """
    def __init__(self, views):
        views.register_view(self)


    def __str__(self):
        return 'base view observer'


    def __repr__(self):
        return 'base view observer'


    def notify(self, views, data, *args, **kwargs):
        """
        This is the method that instance of observable class `al_contacts.view.View` will call
        to send notifications to this observer class.

        :Params:
            data: `list`
                data is a list of dictionaries with with keys = ['name', 'address', 'phone']
            views: `al_contacts.views.Views`
                object of the `al_contacts.views.Views` observer class to which this class' instance
                registers. This could be used later to communicate back.
        """
        if not isinstance(data, list):
            raise ViewException('Data supplied must be a list of dictionaries')

        self._display(data)


    def _display(self, data):
        """
        This method takes the input data from 'data' dictionary and displays it.
        This method needs to be implemented by the subclasses with whatever displays supported.

        :Params:
            data: `list`
                data is a list of dictionaries with with keys = ['name', 'address', 'phone']
        """
        print('View._display() needs to be implemented by the subclasses')
        pass


class TableView(View):
    """
    This class inherits from 'View' class, that defines common methods for all
    view classes.
    This class is an observer class, for observable 'Views' class, for Table View.
    It implements _display() method for Table View.
    """
    def __str__(self):
        return 'table'


    def __repr__(self):
        return 'table'


    def _display(self, data):
        """
        Implementation of base class _display() method.
        This method takes the input data from 'data' dictionary and displays it in Table Format.

        :Params:
            data: `list`
                data is a list of dictionaries with with keys = ['name', 'address', 'phone']
        """
        print('\n\nContact Details in Table View:')
        print('-'*98)
        print('| {0:<5} | {1:<15} | {2:<50} | {3:<15} |'.format('Index', 'Name', 'Address', 'Phone'))
        print('-'*98)
        for index, item in enumerate(data):
            print('| {0:<5} | {1:<15} | {2:<50} | {3:<15} |'.format(index+1, item['name'], item['address'], item['phone']))
        print('-'*98)


class ListView(View):
    """
    This class inherits from 'View' class, that defines common methods for all
    view classes.
    This class is an observer class, for observable 'Views' class, for List View.
    It implements _display() method for List View.
    """
    def __str__(self):
        return 'list'


    def __repr__(self):
        return 'list'


    def _display(self, data):
        """
        Implementation of base class _display() method.
        This method takes the input data from 'data' dictionary and displays it in List Format.

        :Params:
            data: `list`
                data is a list of dictionaries with with keys = ['name', 'address', 'phone']
        """
        print('\n\nContact Details in List View:')
        print('-'*28)
        for index, item in enumerate(data):
            print('Index: {0}'.format(index+1))
            print('Name: {0}'.format(item['name']))
            print('Address: {0}'.format(item['address']))
            print('Phone: {0}'.format(item['phone']))
            print('\n')
