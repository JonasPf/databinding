# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Oct  8 2012)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,430 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer31 = wx.BoxSizer( wx.VERTICAL )
		
		sbSizer5 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Object" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.m_staticText21 = wx.StaticText( self, wx.ID_ANY, u"Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )
		gSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )
		
		self.name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.name, 0, wx.ALL, 5 )
		
		self.change_name = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_name, 0, wx.ALL, 5 )
		
		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Read-only Name:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )
		gSizer1.Add( self.m_staticText26, 0, wx.ALL, 5 )
		
		self.read_only_name = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.read_only_name, 0, wx.ALL, 5 )
		
		self.m_staticText12 = wx.StaticText( self, wx.ID_ANY, u"(Hidden if empty)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )
		gSizer1.Add( self.m_staticText12, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )
		
		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Write-only Surname:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )
		gSizer1.Add( self.m_staticText27, 0, wx.ALL, 5 )
		
		self.write_only_surname = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.write_only_surname, 0, wx.ALL, 5 )
		
		self.change_surname = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_surname, 0, wx.ALL, 5 )
		
		self.m_staticText23 = wx.StaticText( self, wx.ID_ANY, u"Read-only Surname:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText23.Wrap( -1 )
		gSizer1.Add( self.m_staticText23, 0, wx.ALL, 5 )
		
		self.surname = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.surname.Wrap( -1 )
		gSizer1.Add( self.surname, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Active:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.active = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.active, 0, wx.ALL, 5 )
		
		self.change_active = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_active, 0, wx.ALL, 5 )
		
		self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Read-only Active:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )
		gSizer1.Add( self.m_staticText8, 0, wx.ALL, 5 )
		
		self.read_only_active = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.read_only_active.Wrap( -1 )
		gSizer1.Add( self.read_only_active, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self._init_timectrl()
		gSizer1.Add( self.time, 0, wx.ALL, 5 )
		
		self.change_time = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_time, 0, wx.ALL, 5 )
		
		self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Read-only Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )
		gSizer1.Add( self.m_staticText10, 0, wx.ALL, 5 )
		
		self.read_only_time = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.read_only_time.Wrap( -1 )
		gSizer1.Add( self.read_only_time, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer1, 0, 0, 5 )
		
		
		bSizer31.Add( sbSizer5, 0, 0, 5 )
		
		self.autobindctrl = wx.CheckBox( self, wx.ID_ANY, u"Automatic binding from the controls to the object", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer31.Add( self.autobindctrl, 0, wx.ALL, 5 )
		
		bSizer33 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.sync_object_to_ctrls = wx.Button( self, wx.ID_ANY, u"Sync Object to Ctrls", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.sync_object_to_ctrls, 0, wx.ALL, 5 )
		
		self.sync_ctrls_to_object = wx.Button( self, wx.ID_ANY, u"Sync Ctrls to Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sync_ctrls_to_object.Enable( False )
		
		bSizer33.Add( self.sync_ctrls_to_object, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer31 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

