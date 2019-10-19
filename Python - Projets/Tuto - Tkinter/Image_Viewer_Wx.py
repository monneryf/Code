# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:05:22 2019

@author: Philippe BOULANGER
"""

import os
import wx
import wx.adv

ID_Menu_New   = 5000
ID_Menu_Open  = 5001
ID_Menu_Exit  = 5002


wildcard = "Bitmap files (*.bmp)|*.bmp|"              \
           "JPEG files (*.jpg, *jpeg)|*.jpg, *.jpeg|" \
           "PNG files (*.png)|*.png|"                 \
           "GIF files (*.gif)|*.gif|"                 \
           "Icon files (*.ico)|*.ico|"                \
           "Targa files (*.tga)|*.tga|"               \
           "TIFF files (*.tif,*tiff)|*.tif,*tiff|"    \
           "All files (*.*)|*.*"



class MyParentFrame( wx.MDIParentFrame ):

    def __init__( self ):
        wx.MDIParentFrame.__init__( self,
                                    None,
                                    -1,
                                    "MDI Parent",
                                    size  = (600,400),
                                    style = wx.DEFAULT_FRAME_STYLE | wx.HSCROLL | wx.VSCROLL )
        self.create_menu_bar()
        self.create_toolbar()



    def create_menu_bar( self ):
        # create the "File" menu
        menuFile = wx.Menu()
        menuFile.Append( ID_Menu_New,  "&New Window" )
        menuFile.Append( ID_Menu_Open, "&Open file" )
        menuFile.AppendSeparator()
        menuFile.Append( ID_Menu_Exit, "E&xit" )

        # create the menu bar
        menubar = wx.MenuBar()
        menubar.Append( menuFile, "&File" )
        self.SetMenuBar( menubar )

        # bind the events
        self.Bind( wx.EVT_MENU, self.OnNewWindow, id = ID_Menu_New )
        self.Bind( wx.EVT_MENU, self.OnOpenFile,  id = ID_Menu_Open )
        self.Bind( wx.EVT_MENU, self.OnExit,      id = ID_Menu_Exit )



    def create_toolbar( self ):
        # create the toolbar
        tsize = ( 32, 32 )
        tb    = self.CreateToolBar( True )
        tb.SetToolBitmapSize( tsize )

        # new window
        new_bmp =  wx.ArtProvider.GetBitmap( wx.ART_NEW, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_New,
                    "New",
                    new_bmp,
                    wx.NullBitmap,
                    wx.ITEM_NORMAL,
                    "New",
                    "Long help for 'New'",
                    None )

        # open file
        open_bmp = wx.ArtProvider.GetBitmap( wx.ART_FILE_OPEN, wx.ART_TOOLBAR, tsize )
        tb.AddTool( ID_Menu_Open,
                    "Open",
                    open_bmp,
                    wx.NullBitmap,
                    wx.ITEM_NORMAL,
                    "Open",
                    "Long help for 'Open'",
                    None )

        # display the toolbar
        tb.Realize()

        # bind the events
        self.Bind( wx.EVT_TOOL, self.OnNewWindow, id = ID_Menu_New )
        self.Bind( wx.EVT_TOOL, self.OnOpenFile,  id = ID_Menu_Open )



    def OnNewWindow( self, event ):
        win    = wx.MDIChildFrame( self, -1, "Child Window" )
        canvas = wx.ScrolledWindow( win )
        win.Show( True )



    def OnOpenFile( self, event ):
        # choose the file
        dlg = wx.FileDialog( self,
                             message     = "Choose a file",
                             defaultDir  = os.getcwd(),
                             defaultFile = "",
                             wildcard    = wildcard,
                             style       = wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR |
                                           wx.FD_FILE_MUST_EXIST | wx.FD_PREVIEW )
        if dlg.ShowModal() == wx.ID_OK:
            for path in dlg.GetPaths():
                self.read_file( path )
        dlg.Destroy()



    def OnExit( self, event ):
        self.Close( True )



    def read_file( self, filename ):
        # read image if possible
        try:
            image = wx.Image( filename, wx.BITMAP_TYPE_ANY )
        except:
            return

        # create the window
        win     = wx.MDIChildFrame( self, -1, filename )
        canvas  = wx.ScrolledWindow( win )
        sizer   = wx.BoxSizer(wx.HORIZONTAL )
        statBmp = wx.StaticBitmap( canvas, wx.ID_ANY, image.ConvertToBitmap() )
        sizer.Add( statBmp, 1, wx.EXPAND )
        canvas.SetSizer( sizer )
        sizer.Fit( canvas )
        win.Show( True )



class MyApp(wx.App):
    def OnInit(self):
        frame = MyParentFrame()
        frame.Show( True )
        self.SetTopWindow( frame )
        return True


if __name__ == '__main__':
    app = MyApp( False )
    app.MainLoop()


