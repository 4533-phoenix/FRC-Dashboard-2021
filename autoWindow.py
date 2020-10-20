import wx
from image import ImagePanel

class window2(wx.Frame):

    title = "new Window"
    pointArr = []

    def __init__(self,parent,id):
        length = 1000
        width = length * 0.51376721
        wx.Frame.__init__(self, parent, title="Select autonomous", size=(1000, 600))
        panel=wx.Panel(self, -1)
        self.Centre()
        self.Show()
        self.showImage()
        panel.Bind(wx.EVT_LEFT_DOWN, self.printPos)

    def showImage(self):
        length = 1000
        width = length * 0.51376721
        rootPanel = wx.Panel(self, size=(length, width))
        sizer = wx.GridBagSizer(2,2)
        rootPanel.SetSizer(sizer)
        rootPanel.SetBackgroundColour(wx.BLACK)
        
        
        sizer.Add(
            ImagePanel(rootPanel),
            wx.GBPosition(0,0),
            wx.GBSpan(2, 2),
            flag=wx.EXPAND
        )

    def printPos(self, event):
        pos = wx.GetMouseState().GetPosition()
        x = pos.x - self.GetPosition().x
        y = pos.y - self.GetPosition().y
        newPoint = wx.Point(x, y)
        self.pointArr.append(newPoint)
        print(str(x) + ", " + str(y))
        if (len(self.pointArr) >= 5):
            print(self.pointArr)
        
