import wx
import logging
import datetime

# only works with unicode version of wxpython

logger = logging.getLogger(__name__)

def pytime2wxdate(pytime):
	result = wx.DateTime()
	result.SetHMS(pytime.hour, pytime.minute, pytime.second, 0)
	return result

def wxdate2pytime(wxdate):
	return datetime.time(hour=wxdate.GetHour(), minute=wxdate.GetMinute(), second=wxdate.GetSecond())

class AbstractBinding(object):
	def __init__(self, ctrl, my_property, my_object = None, callback_auto_syncing = None, callback_auto_synced = None):
		self.ctrl = ctrl
		self.property = my_property
		self.object = my_object

		self.callback_auto_synced = callback_auto_synced
		self.callback_auto_syncing = callback_auto_syncing

		self._init_events()

	def _init_events(self):
		pass

	def sync_ctrl_to_object(self):
		pass

	def sync_object_to_ctrl(self):
		pass

	def _on_change(self, e):
		if callable(self.callback_auto_syncing):
			if self.callback_auto_syncing(self) is False:
				return # veto - don't sync

		if self.sync_ctrl_to_object():
			# if syncing was successfull, call auto_synced
			if callable(self.callback_auto_synced):
				self.callback_auto_synced(self)

	@staticmethod
	def autobind(ctrl, value):
		return False

BOOLEAN_LABEL_CONVERSION = {True: "Yes", False: "No"}

class LabelBinding(AbstractBinding):
	def sync_object_to_ctrl(self):
		new_text = getattr(self.object, self.property)

		if new_text is None:
			new_text = ''
		elif type(new_text) == bool:
			new_text = BOOLEAN_LABEL_CONVERSION[new_text]
		else:
			new_text = unicode(new_text)

		if self.ctrl.GetLabel() != new_text:
			self.ctrl.SetLabel(new_text)
			return True

		return False

	@staticmethod
	def autobind(ctrl, value):
		return isinstance(ctrl, wx.StaticText) # accept any value because we use unicode() to output any object

class TextBinding(AbstractBinding):
	def _init_events(self):
		self.ctrl.Bind(wx.EVT_TEXT, self._on_change)

	def sync_ctrl_to_object(self):
		# TODO: Only update if something has changed
		setattr(self.object, self.property, self.ctrl.GetValue())
		return True

	def sync_object_to_ctrl(self):
		new_text = getattr(self.object, self.property)

		if new_text is None:
			new_text = ''

		if self.ctrl.GetValue() != new_text:
			self.ctrl.ChangeValue(new_text)
			self.ctrl.SetInsertionPoint(self.ctrl.GetLastPosition())
			return True

		return False

	@staticmethod
	def autobind(ctrl, value):
		return isinstance(ctrl, wx.TextCtrl) and (isinstance(value, str) or isinstance(value, unicode))

class HideBinding(AbstractBinding):
	def sync_object_to_ctrl(self):
		value = getattr(self.object, self.property)

		if value and not self.ctrl.IsShown():
			self.ctrl.Show()
			return True
		elif not value and self.ctrl.IsShown():
			self.ctrl.Hide()
			return True
		else:
			# ctrl is already correctly hidden/shown
			return False

	@staticmethod
	def autobind(ctrl, value):
		return True

class TimeBinding(AbstractBinding):
	def _init_events(self):
		self.ctrl.Bind(wx.lib.masked.EVT_TIMEUPDATE, self._on_change)

	def sync_ctrl_to_object(self):
		new_value = wxdate2pytime(self.ctrl.GetValue(as_wxDateTime=True))
		old_value = getattr(self.object, self.property)

		if new_value != old_value:
			setattr(self.object, self.property, new_value)
		return True

		return False

	def sync_object_to_ctrl(self):
		new_time = pytime2wxdate(getattr(self.object, self.property))

		if self.ctrl.GetValue(as_wxDateTime=True) != new_time:
			self.ctrl.SetValue(new_time)
			return True

		return False

	@staticmethod
	def autobind(ctrl, value):
		return isinstance(ctrl, wx.lib.masked.TimeCtrl) and isinstance(value, datetime.time)

class CheckBoxBinding(AbstractBinding):
	def _init_events(self):
		self.ctrl.Bind(wx.EVT_CHECKBOX, self._on_change)

	def sync_ctrl_to_object(self):
		if self.ctrl.IsChecked() != getattr(self.object, self.property):
			setattr(self.object, self.property, self.ctrl.IsChecked())
			return True

		return False

	def sync_object_to_ctrl(self):
		new_value = getattr(self.object, self.property)

		if self.ctrl.IsChecked() != new_value:
			self.ctrl.SetValue(new_value)
			return True

		return False

	@staticmethod
	def autobind(ctrl, value):
		return isinstance(ctrl, wx.CheckBox) and isinstance(value, bool)

class EnableBinding(AbstractBinding):
	def sync_object_to_ctrl(self):
		new_enabled = getattr(self.object, self.property)

		if self.ctrl.IsEnabled() != new_enabled:
			self.ctrl.Enable(new_enabled)
			return True

		return False

class ButtonBinding(AbstractBinding):
	def _init_events(self):
		self.ctrl.Bind(wx.EVT_BUTTON, self._on_click)

	def _on_click(self, e):

		if callable(self.callback_auto_syncing):
			if self.callback_auto_syncing(self) is False:
				return # Veto, don't execute the function

		function = getattr(self.object, self.property)
		function()

		if callable(self.callback_auto_synced):
			self.callback_auto_synced(self)


	@staticmethod
	def autobind(ctrl, value):
		return isinstance(ctrl, wx.Button) and callable(value)

class BindingContext(object):
	def __init__(self, default_object = None):
		self.bindings = []
		self.default_object = default_object
		self.autobind_classes = [TextBinding, LabelBinding, ButtonBinding, CheckBoxBinding, TimeBinding]

	def auto_bind(self, view, my_object = None, callback_auto_syncing=None, callback_auto_synced=None):
		if my_object is None:
			my_object = self.default_object

		view_vars = vars(view)
		object_vars = dir(my_object) # use dir instead of vars because we want methods to bind them to buttons

		for v in view_vars:
			if v in object_vars:
				ctrl = getattr(view, v)
				value = getattr(my_object, v)

				for clazz in self.autobind_classes:
					if clazz.autobind(ctrl, value):
						logger.debug('Autobind {} in {}.{} to {}.{}'.format(ctrl.__class__.__name__, 
							view.__class__.__name__, v, 
							my_object.__class__.__name__, v))
						self.add(clazz(ctrl, v, my_object, 
							callback_auto_syncing=callback_auto_syncing, 
							callback_auto_synced=callback_auto_synced))

	def add(self, binding):
		if binding.object is None:
			if self.default_object is not None:
				binding.object = self.default_object
			else:
				raise Exception("No binding object specified") 

		self.bindings.append(binding)

	def sync_ctrls_to_objects(self):
		for b in self.bindings:
			b.sync_ctrl_to_object()

	def sync_objects_to_ctrls(self):
		for b in self.bindings:
			b.sync_object_to_ctrl()