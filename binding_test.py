import wx
import wx.lib.masked
import binding_test_ui
import datetime
import logging
from databinding import *

class Model(object):
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

class MyFrame(binding_test_ui.MainFrame):
    def __init__(self, model):
        binding_test_ui.MainFrame.__init__(self, None)

        self.autosync = True

        self.binding_context = BindingContext(model)

        # Automatically binds controls if they are exposed as properties by the view and
        # if the object has properties with the same name and compatible type
        self.binding_context.auto_bind(self, callback_auto_syncing=self.auto_syncing)

        # use a non-default object by passing it to the *Binding classes - in this case 'self'
        self.binding_context.add(ButtonBinding(self.sync_object_to_ctrls, 'on_sync_object_to_ctrls', self))
        self.binding_context.add(ButtonBinding(self.sync_ctrls_to_object, 'on_sync_ctrls_to_object', self))
        self.binding_context.add(CheckBoxBinding(self.autobindctrl, 'autosync', self, callback_auto_synced=self.auto_synced))
        self.binding_context.add(EnableBinding(self.sync_ctrls_to_object, 'sync_ctrls_to_objects_enabled', self))

        self.binding_context.sync_objects_to_ctrls()

    def on_sync_object_to_ctrls(self):
        self.binding_context.sync_objects_to_ctrls()

    def on_sync_ctrls_to_object(self):
        self.binding_context.sync_ctrls_to_objects()

    def _init_timectrl(self):
        self.time = wx.lib.masked.TimeCtrl(self)

    @property
    def sync_ctrls_to_objects_enabled(self):
        return not self.autosync

    def auto_synced(self, binding):
        if self.autosync: # Autosync activated
            wx.MessageDialog(self, "Autosync enabled. Click \"Sync Object to Ctrls\" to disable the manual button", style=wx.OK).ShowModal()
        else: # Autosync deactivated
            wx.MessageDialog(self, "Autosync disabled. Click \"Sync Object to Ctrls\" to enable the manual button", style=wx.OK).ShowModal()

    def auto_syncing(self, binding):
        # disable/enable automatic syncing from controls to objects but only if they are not buttons (buttons rely on autosyncing to work)
        if isinstance(binding, ButtonBinding):
            return True 
        else:
            return self.autosync

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    app = wx.App(False)

    model = Model()
    frame = MyFrame(model)
    frame.Show()
    app.MainLoop()
