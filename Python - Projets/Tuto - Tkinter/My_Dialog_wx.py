# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 14:05:22 2019

@author: Philippe BOULANGER
"""

import wx

class MyDialog( wx.Dialog ):

    def __init__( self,
                  parent,
                  id,
                  title,
                  size  = wx.DefaultSize,
                  pos   = wx.DefaultPosition,
                  style = wx.DEFAULT_DIALOG_STYLE,
                  name  = 'My dialog' ):
        wx.Dialog.__init__( self )
        self.Create( parent, id, title, pos, size, style, name )
        staticText   = wx.StaticText( self, -1, "Hello world!" )
        okButton     = wx.Button( self, wx.ID_OK, "OK" )
        cancelButton = wx.Button( self, wx.ID_CANCEL, "Cancel" )
        
        self.Bind( wx.EVT_BUTTON, self.OnOK, okButton )
        self.Bind( wx.EVT_BUTTON, self.OnCancel, cancelButton )
        
        topSizer = wx.BoxSizer( wx.VERTICAL )
        topSizer.Add( staticText,   0, wx.EXPAND )
        hSizer = wx.BoxSizer( wx.HORIZONTAL )
        hSizer.Add( okButton,     0, wx.EXPAND )
        hSizer.Add( cancelButton, 0, wx.EXPAND )
        topSizer.Add( hSizer, 0, wx.EXPAND )
        self.SetSizer( topSizer )
        topSizer.Fit( self )


    def OnOK( self, event ):
        print( "OnOK" )
        self.EndModal( wx.ID_OK )


    def OnCancel( self, event ):
        print( "OnCancel" )
        self.EndModal( wx.ID_CANCEL )


class MyApplication( wx.App ):
    
    def OnInit( self ):
        # initialize
        print( "MyApplication.OnInit" )
        self.SetAppName( "HelloWordApp" )
        
        # create dialog box
        dlg = MyDialog( None, -1, "Hello world Application!" )
        print( "before ShowModal" )
        res = dlg.ShowModal()
        print( "after ShowModal" )
        if res == wx.ID_OK:
            print( "exit OK" )
        elif res == wx.ID_CANCEL:
            print( "exit CANCEL" )
        else:
            print( "exit %d" % res )
        dlg.Destroy()
        return True


if __name__ == '__main__':
    app = MyApplication()
    app.MainLoop()


