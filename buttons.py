import wx
from autoWindow import window2
from image import ImagePanel

class ButtonsPanel(wx.Panel):
    def __init__(self, parent=None, id=-1,pos=wx.DefaultPosition, title='wxPython'):
        wx.Frame.__init__(self, parent, id)
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.btn = wx.Button(self, -1, "Select Autonomous")
        sizer.Add(self.btn,1,wx.ALIGN_CENTER_HORIZONTAL, wx.ALL)
        self.btn.Bind(wx.EVT_BUTTON, self.onClicked)


    def onClicked(self, event):
        secondWindow = window2(self, -1)
        secondWindow.Show()


