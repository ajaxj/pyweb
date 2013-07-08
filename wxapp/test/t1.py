#  -*- coding:utf-8 -*-
import wx


# 主窗口类
class Frame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,-1,title)
        panel = wx.Panel(self)
        text = wx.StaticText(panel,-1,"Test")



#主应用函数
class App(wx.App):
    def OnInit(self):
        frame = Frame(parent=None, title='Bare')
        self.SetTopWindow(frame)
        frame.Show(True)
        return True

#主运行类
if __name__ == "__main__":
    app = App()
    app.MainLoop()





