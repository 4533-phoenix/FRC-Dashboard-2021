import wx

class App:
    def startApp():
        app = wx.App(False)
        frame = wx.Frame(None, wx.ID_ANY, "Game Changers Dashboard")
        frame.Show(True)
        app.MainLoop()