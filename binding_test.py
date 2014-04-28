import wx
import wx.lib.masked
import binding_test_ui
import datetime
import logging
from databinding import *

class Model(AutoBindingMixin, object):
    def __init__(self):
        self.name = "Donald"
        self.surname = "Duck"
        self.active = True
        self.time = datetime.datetime.now().time()

    def change_name(self):
        self.name = "Mickey"

    def change_surname(self):
        self.surname = "Mouse"

    def change_active(self):
        self.active = not self.active

    def change_time(self):
        self.time = datetime.datetime.now().time()

    def __unicode__(self):
        return "Name: {}\nSurname: {}\nActive: {}\nTime: {}".format(self.name, self.surname, self.active, self.time)

class MyFrame(binding_test_ui.MainFrame):
    def __init__(self, model):
        binding_test_ui.MainFrame.__init__(self, None)

        self.model = model

        self.binding_context = BindingContext(model)

        # Automatically binds controls if they are exposed as properties by the view and
        # if the object has properties with the same name and compatible type
        self.binding_context.auto_bind(self, callback_auto_synced=self.print_model)

        # use a non-default object by passing it to the *Binding classes - in this case 'self'

        # Sync once to intialise the controls
        self.binding_context.sync_objects_to_ctrls()

    def _init_timectrl(self):
        self.time = wx.lib.masked.TimeCtrl(self)

    def print_model(self, binding):
        print "---------------------------"
        print "The current model state is:"
        print unicode(self.model)
        print "---------------------------"

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app = wx.App(False)

    model = Model()
    frame = MyFrame(model)
    frame.Show()
    app.MainLoop()
