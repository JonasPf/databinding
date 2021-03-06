# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  6 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

TOOL1 = 1000
TOOL2 = 1001

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
		
		self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, u"Colour:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )
		gSizer1.Add( self.m_staticText7, 0, wx.ALL, 5 )
		
		self.colour_picker = wx.ColourPickerCtrl( self, wx.ID_ANY, wx.BLACK, wx.DefaultPosition, wx.DefaultSize, wx.CLRP_DEFAULT_STYLE )
		gSizer1.Add( self.colour_picker, 0, wx.ALL, 5 )
		
		self.change_colour = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_colour, 0, wx.ALL, 5 )
		
		self.m_staticText71 = wx.StaticText( self, wx.ID_ANY, u"Directory:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText71.Wrap( -1 )
		gSizer1.Add( self.m_staticText71, 0, wx.ALL, 5 )
		
		self.dir_picker = wx.DirPickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
		gSizer1.Add( self.dir_picker, 0, wx.ALL, 5 )
		
		self.change_dir = wx.Button( self, wx.ID_ANY, u"Change in Object", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.change_dir, 0, wx.ALL, 5 )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"Object:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		gSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )
		
		self.object = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.object.Wrap( -1 )
		gSizer1.Add( self.object, 0, wx.ALL, 5 )
		
		
		gSizer1.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer5.Add( gSizer1, 0, 0, 5 )
		
		
		bSizer31.Add( sbSizer5, 0, 0, 5 )
		
		sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Clicks" ), wx.VERTICAL )
		
		self.clicks = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.clicks.Wrap( -1 )
		self.clicks.SetMinSize( wx.Size( -1,200 ) )
		
		sbSizer2.Add( self.clicks, 0, wx.ALL, 5 )
		
		
		bSizer31.Add( sbSizer2, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer31 )
		self.Layout()
		self.toolbar = self.CreateToolBar( wx.TB_NOICONS|wx.TB_TEXT, wx.ID_ANY ) 
		self.tool1 = self.toolbar.AddLabelTool( TOOL1, u"Tool 1", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.tool2 = self.toolbar.AddLabelTool( TOOL2, u"Tool 2", wx.NullBitmap, wx.NullBitmap, wx.ITEM_NORMAL, wx.EmptyString, wx.EmptyString, None ) 
		
		self.toolbar.Realize() 
		
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.item1 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Item 1", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.item1 )
		
		self.item2 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"Item 2", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.AppendItem( self.item2 )
		
		self.m_menubar1.Append( self.m_menu1, u"Menu" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

