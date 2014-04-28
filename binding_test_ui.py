# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Nov  6 2013)
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
		
		self.m_staticText24 = wx.StaticText( self, wx.ID_ANY, u"Active:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )
		gSizer1.Add( self.m_staticText24, 0, wx.ALL, 5 )
		
		self.active = wx.CheckBox( self, wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.active, 0, wx.ALL, 5 )
		
		self.change_active = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_active, 0, wx.ALL, 5 )
		
		self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )
		gSizer1.Add( self.m_staticText9, 0, wx.ALL, 5 )
		
		self._init_timectrl()
		gSizer1.Add( self.time, 0, wx.ALL, 5 )
		
		self.change_time = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_time, 0, wx.ALL, 5 )
		
		
		sbSizer5.Add( gSizer1, 0, 0, 5 )
		
		
		bSizer31.Add( sbSizer5, 0, 0, 5 )
		
		
		self.SetSizer( bSizer31 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

