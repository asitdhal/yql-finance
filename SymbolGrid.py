# gridEvents.py

import wx
import wx.grid as gridlib
import fetch
import threading

########################################################################
class MyGrid(gridlib.Grid):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, parent, col_cnt,  row_cnt):
        """Constructor"""
        gridlib.Grid.__init__(self, parent)
        self.CreateGrid(col_cnt, row_cnt)


        # test all the events
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_CLICK, self.OnCellLeftClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_CLICK, self.OnCellRightClick)
        self.Bind(gridlib.EVT_GRID_CELL_LEFT_DCLICK, self.OnCellLeftDClick)
        self.Bind(gridlib.EVT_GRID_CELL_RIGHT_DCLICK, self.OnCellRightDClick)

        self.Bind(gridlib.EVT_GRID_LABEL_LEFT_CLICK, self.OnLabelLeftClick)
        self.Bind(gridlib.EVT_GRID_LABEL_RIGHT_CLICK, self.OnLabelRightClick)
        self.Bind(gridlib.EVT_GRID_LABEL_LEFT_DCLICK, self.OnLabelLeftDClick)
        self.Bind(gridlib.EVT_GRID_LABEL_RIGHT_DCLICK, self.OnLabelRightDClick)

        self.Bind(gridlib.EVT_GRID_ROW_SIZE, self.OnRowSize)
        self.Bind(gridlib.EVT_GRID_COL_SIZE, self.OnColSize)

        self.Bind(gridlib.EVT_GRID_RANGE_SELECT, self.OnRangeSelect)
        self.Bind(gridlib.EVT_GRID_CELL_CHANGE, self.OnCellChange)
        self.Bind(gridlib.EVT_GRID_SELECT_CELL, self.OnSelectCell)

        self.Bind(gridlib.EVT_GRID_EDITOR_SHOWN, self.OnEditorShown)
        self.Bind(gridlib.EVT_GRID_EDITOR_HIDDEN, self.OnEditorHidden)
        self.Bind(gridlib.EVT_GRID_EDITOR_CREATED, self.OnEditorCreated)

    def OnCellLeftClick(self, evt):
        print "OnCellLeftClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                 evt.GetCol(),
                                                 evt.GetPosition())
        evt.Skip()

    def OnCellRightClick(self, evt):
        print "OnCellRightClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetPosition())
        evt.Skip()

    def OnCellLeftDClick(self, evt):
        print "OnCellLeftDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetPosition())
        evt.Skip()

    def OnCellRightDClick(self, evt):
        print "OnCellRightDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition())
        evt.Skip()

    def OnLabelLeftClick(self, evt):
        print "OnLabelLeftClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetPosition())
        evt.Skip()

    def OnLabelRightClick(self, evt):
        print "OnLabelRightClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition())
        evt.Skip()

    def OnLabelLeftDClick(self, evt):
        print "OnLabelLeftDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                   evt.GetCol(),
                                                   evt.GetPosition())
        evt.Skip()

    def OnLabelRightDClick(self, evt):
        print "OnLabelRightDClick: (%d,%d) %s\n" % (evt.GetRow(),
                                                    evt.GetCol(),
                                                    evt.GetPosition())
        evt.Skip()

    def OnRowSize(self, evt):
        print "OnRowSize: row %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition())
        evt.Skip()

    def OnColSize(self, evt):
        print "OnColSize: col %d, %s\n" % (evt.GetRowOrCol(),
                                           evt.GetPosition())
        evt.Skip()

    def OnRangeSelect(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print "OnRangeSelect: %s  top-left %s, bottom-right %s\n" % (msg, evt.GetTopLeftCoords(),
                                                                     evt.GetBottomRightCoords())
        evt.Skip()


    def OnCellChange(self, evt):
        print "OnCellChange: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(), evt.GetPosition())

        # Show how to stay in a cell that has bad data.  We can't just
        # call SetGridCursor here since we are nested inside one so it
        # won't have any effect.  Instead, set coordinates to move to in
        # idle time.
        value = self.GetCellValue(evt.GetRow(), evt.GetCol())

        if value == 'no good':
            self.moveTo = evt.GetRow(), evt.GetCol()

    def OnSelectCell(self, evt):
        if evt.Selecting():
            msg = 'Selected'
        else:
            msg = 'Deselected'
        print "OnSelectCell: %s (%d,%d) %s\n" % (msg, evt.GetRow(),
                                                 evt.GetCol(), evt.GetPosition())

        # Another way to stay in a cell that has a bad value...
        row = self.GetGridCursorRow()
        col = self.GetGridCursorCol()

        if self.IsCellEditControlEnabled():
            self.HideCellEditControl()
            self.DisableCellEditControl()

        value = self.GetCellValue(row, col)

        if value == 'no good 2':
            return  # cancels the cell selection

        evt.Skip()


    def OnEditorShown(self, evt):
        if evt.GetRow() == 6 and evt.GetCol() == 3 and \
           wx.MessageBox("Are you sure you wish to edit this cell?",
                        "Checking", wx.YES_NO) == wx.NO:
            evt.Veto()
            return

        print "OnEditorShown: (%d,%d) %s\n" % (evt.GetRow(), evt.GetCol(),
                                               evt.GetPosition())
        evt.Skip()


    def OnEditorHidden(self, evt):
        if evt.GetRow() == 6 and evt.GetCol() == 3 and \
           wx.MessageBox("Are you sure you wish to  finish editing this cell?",
                        "Checking", wx.YES_NO) == wx.NO:
            evt.Veto()
            return

        print "OnEditorHidden: (%d,%d) %s\n" % (evt.GetRow(),
                                                evt.GetCol(),
                                                evt.GetPosition())
        evt.Skip()


    def OnEditorCreated(self, evt):
        print "OnEditorCreated: (%d, %d) %s\n" % (evt.GetRow(),
                                                  evt.GetCol(),
                                                  evt.GetControl())

########################################################################
class MyForm(wx.Frame):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        wx.Frame.__init__(self, parent=None, title="An Eventful Grid")
        panel = wx.Panel(self)
        lis = []
        fields = []
        fields.append('Symbol')
        #fields.append('YearLow')
        fields.append('LastTradePriceOnly')
        #fields.append('YearHigh')
        #fields.append('LastTradeDate')
        fields.append('Bid')
        #fields.append('PreviousClose')
        fields.append('PercentChange')
        fields.append('Ask')
        fields.append('Change')
        fields.append('Name')
        #fields.append('DaysRange')
        fields.append('LastTradeTime')
        #fields.append('StockExchange')
        #fields.append('DaysHigh')
        fields.append('Open')

        lis.append("TCS.NS")
        lis.append("HINDALCO.NS")

        myGrid = MyGrid(panel, len(lis), len(fields))
        yql_grid = YqlGridWrapper(myGrid, lis, fields)
        yql_grid.start()



        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(myGrid, 1, wx.EXPAND)
        panel.SetSizer(sizer)



class YqlGridWrapper(threading.Thread):
    def __init__(self, grid, symbols, fields):
        self.grid = grid
        self.symbols = symbols
        self.fields = fields
        threading.Thread.__init__(self)

    def run(self):
        print "Thread started"
        self.UpdateCellValue()
        print "Thread ends"

    def UpdateCellValue(self):
        while True:
            yql_ob = fetch.Yql(self.symbols, self.fields)
            yql_res = yql_ob.query_yql()
            row = 0
            col = 0
            for symbol in self.symbols:
                col = 0
                for fiels in self.fields:
                    print "(", row, ",", col, ",",yql_res[symbol][fiels]
                    self.grid.SetCellValue(row, col, str(yql_res[symbol][fiels]))
                    self.grid.ForceRefresh()
                    col = col + 1
                row = row + 1


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyForm().Show()
    app.MainLoop()