import wx
import wx.lib.masked
import simple_ctrls_ui
import datetime
import logging
import sys
import os.path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../'))
from databinding import *

class Model(AutoBindingMixin, object):
    def __init__(self):
        self.name = "Donald"
        self.active = True
        self.time = datetime.datetime.now().time()
        self.colour_picker = (255, 0, 0)
        self.dir_picker = ''

    def change_name(self):
        self.name = "Mickey"

    def change_active(self):
        self.active = not self.active

    def change_time(self):
        self.time = datetime.datetime.now().time()

    def change_colour(self):
        self.colour_picker = (127, 127, 127)

    def change_dir(self):
        self.dir_picker = os.path.dirname(os.path.abspath(__file__))

    @property
    def object(self):
        return unicode(self)

    def __unicode__(self):
        return "Name: {}\nActive: {}\nTime: {}\nColour: {}\nDirectory: {}".format(self.name, self.active, self.time, self.colour_picker, self.dir_picker)

class MyFrame(simple_ctrls_ui.MainFrame):
    def __init__(self, model):
        simple_ctrls_ui.MainFrame.__init__(self, None)
        self.model = model

        self.binding_context = BindingContext(model)

        # Automatically binds controls if they are exposed as properties by the view and
        # if the object has properties with the same name and compatible type
        self.binding_context.auto_bind(self, callback_auto_synced=self.print_model)

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
