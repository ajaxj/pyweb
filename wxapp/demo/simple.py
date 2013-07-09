# -*- coding:utf-8 -*-
import wx

class MyFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,-1,title,pos=(150,150),size=(350,200))
        #create Menubar
        menuBar = wx.MenuBar()

        menu = wx.Menu()
        menu.Append(wx.ID_EXIT,"E&xit\tAlt-X",u"退出")
        self.Bind(wx.EVT_MENU,self.OnTimeToClose,id=wx.ID_EXIT)
        menuBar.Append(menu,"&File")
        self.SetMenuBar(menuBar)
        self.CreateStatusBar()
        panel = wx.Panel(self)
        text = wx.StaticText(panel,-1,u"测试中文")
        text.SetFont(wx.Font(14,wx.SWISS,wx.NORMAL,wx.BOLD))
        text.SetSize(text.GetBestSize())
        btn = wx.Button(panel,-1,u"关闭")
        self.Bind(wx.EVT_BUTTON,self.OnTimeToClose,btn)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text,0,wx.ALL,10)
        sizer.Add(btn,0,wx.ALL,10)
        panel.SetSizer(sizer)
        panel.Layout()





    def OnTimeToClose(self,evt):
        print "bye"
        self.Close()

class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame(None,"Simple App")
        self.SetTopWindow(frame)
        frame.Show(True)
        return True


if __name__ == '__main__':
    app = MyApp(redirect=True)
    app.MainLoop()



