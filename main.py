import wx
from app import App
from image import ImagePanel

class MainFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size=(1000,600))
        screenSize = wx.DisplaySize()
        initSize = (screenSize[0] * 0.6, screenSize[1] * 0.75)
        self.SetInitialSize(initSize)
        self.Show(True)
        self.build()
        

    def build(self):
        gbs = wx.GridBagSizer(1, 1)
        mainPanel = wx.Panel(self)
        mainPanel.SetSizer(gbs)

        gbs.Add(
            ImagePanel(mainPanel),
            wx.GBPosition(0,0),
            wx.GBSpan(2, 2),
            flag=wx.EXPAND
        )

        gbs.AddGrowableCol(0, 1)
        gbs.AddGrowableRow(0, 1)

        gbs.Fit(self)

app = wx.App(False)
frame = MainFrame(None, 'Auto Selector')
app.MainLoop()