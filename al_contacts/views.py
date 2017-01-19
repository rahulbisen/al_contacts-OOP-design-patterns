#! /usr/bin/env python


class ViewsException(Exception):
    """
    Exception raise from `al_contacts.views.Views class.
    Customise if required
    """
    pass


class Views:
    """
    This is an observable class for views.
    Any View class can register itself with this class using the register_view() method
    a View can un-register itself using the unregister_view() method
    This class can send notifications to the view classes using notify_views() method
    """
    def __init__(self, data=[]):
        """
        :Params:
            data: `list`
                data is a list of dictionaries with with keys = ['name', 'address', 'phone']
        """
        self.views = []
        if not isinstance(data, list):
            raise ViewsException('Views object instantiation Failed. Data supplied must be a list of dictionaries')
        self.data = data


    def __str__(self):
        return 'Views'


    def __repr__(self):
        return 'Views'


    def register_view(self, view):
        """
        Any al_contacts.view.View class instance can register itself with this class using the
        register_view() method

        :Params:
            format: `al_contacts.view.View`
                object of one of the View' classes which registers with this class.
        """
        if view in self.views:
            raise ViewsException('"{0}" view already registered with "{1}".'.format(view, self))

        print('Registering "{0}" view with "{1}"'.format(view, self))
        self.views.append(view)


    def unregister_view(self, view):
        """
        Any al_contacts.view.View class instance can unregister itself with this class using the
        unregister_view() method

        :Params:
            format: `al_contacts.view.View`
                object of one of the View subclasses which has to be unregistered with
                this class.
        """
        if view not in self.views:
            raise ViewsException('"{0}" view is not registered with "{1}".'.format(view, self))

        print('Unregistering "{0}" view from "{1}"'.format(view, self))
        self.views.pop(self.views.index(view))
            
    
    def notify_views(self, view=''):
        """
        This method sends notifications to the all instances of `al_contacts.view.View` that are
        registered with this class.
        If 'view' is passed, it sends notification only to a view whose string representation
        matches with the passed 'view'.
        It calls the notify() method of the registered views along with the data that has to
        be displayed.
        The `al_contacts.view.View` must implement notify() method

        :Params:
            view: `str`
                string representation for a registered `al_contacts.view.View` instance.
        """
        if not self.views:
            raise ViewsException('There are no Views registered with "{0}" currently'.format(self))

        if view:
            if not isinstance(view, str):
                raise ViewsException('View name supplied must be a string')

            if view not in [str(aView) for aView in self.views]:
                raise ViewsException('There is no view named "{0}" registered with "{0}" currently'.format(view, self))

            for aView in self.views:
                if str(aView) == view:
                    aView.notify(self, self.data)
                    break
        else:
            for aView in self.views:
                aView.notify(self, self.data)
