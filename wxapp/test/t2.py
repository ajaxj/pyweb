# -*- coding:utf-8 -*-
import wx

#TODO A
class main_window(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(500,500),style=wx.DEFAULT_FRAME_STYLE|wx.NO_FULL_REPAINT_ON_RESIZE)
        self.mainmenu = wx.MenuBar()
        menu = wx.Menu()
        item = menu.Append(wx.ID_OPEN,"&OPEN","Open project")
        self.Bind(wx.EVT_MENU,self.OnProjectOpen,item)
        item = menu.Append(wx.ID_NEW,"&New","New project")
        self.Bind(wx.EVT_MENU,self.OnProjectNew,item)
        item = menu.Append(wx.ID_EXIT,"E&xit","Exit program")
        self.Bind(wx.EVT_MENU,self.OnProjectExit,item)
        self.mainmenu.Append(menu,"&Project")
        #TODO A

        self.SetMenuBar(self.mainmenu)
        splitter = wx.SplitterWindow(self,style=wx.NO_3D|wx.SP_3D)
        splitter.SetMinimumPaneSize(1)

        splitter.SetSashPosition(180,True)

        # 公共变量
        self.projectdirty = False
        self.root = None
        self.close = False
        self.Bind(wx.EVT_CLOSE,self.OnProjectExit)
        self.Show(True)


    def OnProjectOpen(self,event):
        pass

    def OnProjectNew(self,event):
        pass

    def OnProjectExit(self,event):
        #TODO eDIT
        self.Close()

    def CheckProjectDirty(self):
        open_it = True
        if self.projectdirty:
            pass
        return open_it


class App(wx.App):
    def OnInit(self):
        frame = main_window(None,"wxProject - " )
        return True

if __name__ == "__main__":
    app = App(0)
    app.MainLoop()


