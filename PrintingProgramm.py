import wx
import os.path
from wx.lib.intctrl import IntCtrl
from testcardsettings import TestCardSettings
from testcardproductionmock import TestCardProduction
from tkinter import Tk
DBG = True

APP_EXIT = 1
PLATFORM_SELECTION_LIST = ('None','SLE78', 'SLC52', 'Pxyz')
INTERFACE_SELECTION_LIST = ('CB', 'CL')
SCP_SELECTION_LIST = ('02', '03')
TEST_KEYS_SELECTION_LIST = ('none', 'VISA test keys fix', 'VISA test keys derived','from JLoad key file')
LCS_SELECTION_LIST = ('OP_READY', 'INITIALIZED', 'SECURED', 'CARD_LOCKED')
IN = ('https://www.linkedin.com/in/christian-schmid-8b4b1b16a')

class ComboBoxFrame(wx.Frame):
    def __init__(self, testCardSettings = None):
        self.fileName = None
        if testCardSettings == None:
            self.testCardSettings = TestCardSettings()
        else:
            self.testCardSettings = testCardSettings
        self.menuBar = wx.Frame.__init__(self, None, -1, 'Loaded-File :', size=(720, 390))
        
        self.panel = wx.Panel(self, -1)
        self.SetBackgroundColour('#ffffff')
        path = os.path.abspath("img/icon.png")
        icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
        self.SetIcon(icon)
        #Create CB_DROPDOWN Buttons and save ability
        
        
        wx.StaticText(self.panel, -1, "Platform", (15, 21))
        self.ComboBox1 = wx.ComboBox(self.panel, -1, "...", (15, 41), wx.DefaultSize, PLATFORM_SELECTION_LIST, wx.CB_DROPDOWN)
        self.ComboBox1.Bind(wx.EVT_COMBOBOX, self.OnComboBox1)


        wx.StaticText(self.panel, -1, "SCP", (130, 21))
        self.ComboBox2 = wx.ComboBox(self.panel, -1, "...", (130, 41), wx.DefaultSize, SCP_SELECTION_LIST, wx.CB_DROPDOWN)
        self.ComboBox2.Bind(wx.EVT_COMBOBOX, self.OnComboBox2)
        
        
        wx.StaticText(self.panel, -1, "Keys", (240, 200))
        self.ComboBox3 = wx.ComboBox(self.panel, -1, "...", (240, 220), wx.DefaultSize, TEST_KEYS_SELECTION_LIST, wx.CB_DROPDOWN)
        self.ComboBox3.Bind(wx.EVT_COMBOBOX, self.onKey)
        
        
        wx.StaticText(self.panel, -1, "LCS", (15, 81))
        self.ComboBox4 = wx.ComboBox(self.panel, -1, "...", (15, 101), wx.DefaultSize, LCS_SELECTION_LIST, wx.CB_DROPDOWN)
        self.ComboBox4.Bind(wx.EVT_COMBOBOX, self.OnComboBox4)
        
        
        wx.StaticText(self.panel, -1, "Interface", (15, 141))
        self.ComboBox5 = wx.ComboBox(self.panel, -1, "...", (15, 161), wx.DefaultSize, INTERFACE_SELECTION_LIST, wx.CB_DROPDOWN)
        self.ComboBox5.Bind(wx.EVT_COMBOBOX, self.OnComboBox5)
        
        
        #Button Bindings for Browsing
        
        
        self.openFileDlgBtn0 = wx.Button(self.panel, -1, "Img-file",(450,40))
        self.openFileDlgBtn0.SetForegroundColour('blue')
        self.openFileDlgBtn0.Bind(wx.EVT_BUTTON, self.onOpenFileName0)
        self.openFileDlgBtn1 = wx.Button(self.panel,-1, "Script-file", (450, 101))
        self.openFileDlgBtn1.SetForegroundColour('blue')
        self.openFileDlgBtn1.Bind(wx.EVT_BUTTON, self.onOpenFileName1)
        self.openFileDlgBtn2 = wx.Button(self.panel,-1, "CAP-file", (450, 160))
        self.openFileDlgBtn2.SetForegroundColour('blue')
        self.openFileDlgBtn2.Bind(wx.EVT_BUTTON, self.onOpenFileName2)
        self.openFileDlgBtn3 = wx.Button(self.panel,-1, "Key-file", (450, 220))
        self.openFileDlgBtn3.SetForegroundColour('blue')
        self.openFileDlgBtn3.Bind(wx.EVT_BUTTON, self.onKey)
        self.openFileDlgBtn4 = wx.Button(self.panel,-1, "Print-file", (450, 280))
        self.openFileDlgBtn4.SetForegroundColour('blue')
        self.openFileDlgBtn4.Bind(wx.EVT_BUTTON, self.onOpenFileName4)
        self.openFileDlgBtn5 = wx.Button(self.panel, -1, "Preview", (600, 280))
        self.openFileDlgBtn5.SetForegroundColour('blue')
        self.openFileDlgBtn5.Bind(wx.EVT_BUTTON, self.onOpenFileName5)
        execute = wx.Button(self.panel, -1, "Execute", (15, 281))
        execute.SetForegroundColour('red')
        openPrintButton = execute
        openPrintButton.Bind(wx.EVT_BUTTON, self.onExecute)
                             
                             
        #Check boxes and delFile buttons-
        
        
        self.delFile0 = wx.Button(self.panel, -1, "X", (240, 41), size=(23,23))
        self.delFile0.Bind(wx.EVT_BUTTON, self.onDelFileName0)
        self.delFile0.SetForegroundColour('red')
        self.delFile1 = wx.Button(self.panel, -1, "X", (240, 101), size=(23,23))
        self.delFile1.Bind(wx.EVT_BUTTON, self.onDelFileName1)
        self.delFile1.SetForegroundColour('red')
        self.delFile2 = wx.Button(self.panel, -1, "X", (240, 161), size=(23,23))
        self.delFile2.Bind(wx.EVT_BUTTON, self.onDelFileName2)
        self.delFile2.SetForegroundColour('red')
        self.delFile3 = wx.Button(self.panel, -1, "X", (240,281), size=(23,23))
        self.delFile3.Bind(wx.EVT_BUTTON, self.onDelFileName3)
        self.delFile3.SetForegroundColour('red')
        
        
        #Text entrys
        
        
        self.t0 = wx.TextCtrl(self.panel, wx.TE_READONLY, pos=(275, 41))
        self.t1 = wx.TextCtrl(self.panel, wx.TE_READONLY, pos=(275, 101))
        self.t2 = wx.TextCtrl(self.panel, wx.TE_READONLY, pos=(275, 161))
        self.t3 = wx.TextCtrl(self.panel, wx.TE_READONLY, pos=(275, 281))
        self.t4 = IntCtrl(self.panel,size=(30, -1), pos=(130, 282))
        
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        ope = wx.MenuItem(fileMenu, wx.ID_ANY, '&Open\tCtrl+O')
        self.Bind(wx.EVT_MENU, self.onOpenSaveFile, ope)
        ope.SetBitmap(wx.Bitmap('img/open.png'))
        fileMenu.Append(ope)
        fileMenu.AppendSeparator()
        
        
        saf = wx.MenuItem(fileMenu, wx.ID_ANY, '&Save\tCtrl+S')
        saf.SetBitmap(wx.Bitmap('img/save.png'))
        saf.SetTextColour('blue')
        self.Bind(wx.EVT_MENU, self.OnSave, saf)
        fileMenu.Append(saf)
        
        
        safas = wx.MenuItem(fileMenu, wx.ID_SAVE, '&SaveAs')
        safas.SetTextColour('blue')
        fileMenu.Append(safas)
        self.Bind(wx.EVT_MENU, self.OnSaveAs, safas)
        fileMenu.AppendSeparator()
        
        
        qmi = wx.MenuItem(fileMenu, wx.ID_EXIT, '&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('img/close.png'))
        qmi.SetTextColour('red')
        fileMenu.Append(qmi)
        self.Bind(wx.EVT_MENU, self.OnQuit, qmi)
        fileMenu.AppendSeparator()
        
        refMenu = wx.Menu()
        self.link = ('https://www.linkedin.com/in/christian-schmid-8b4b1b16a')
        self.ref = wx.MenuItem(refMenu, wx.ID_ANY, self.link)
        self.ref.SetBitmap(wx.Bitmap('img/avatar.png'))
        self.ref.SetTextColour('blue')
        self.Bind(wx.EVT_MENU, self.OnRef, self.ref)
        refMenu.Append(self.ref)
        

        menubar.Append(fileMenu, '&File')
        menubar.Append(refMenu, '&Reference')
        self.SetMenuBar(menubar)
        self.Centre()
        self.SetOwnBackgroundColour('#FFFFFF')
        self.update()
        
        
    def update(self):
        if self.link == ('https://www.linkedin.com/in/christian-schmid-8b4b1b16a') and IN == self.link:
            if DBG:
                print('* update')
                    
            if self.fileName is None:
                displayFileName = ''
            else:
                displayFileName = os.path.basename(self.fileName)
    
            self.SetTitle('Loaded-File :      %s' % displayFileName)
                
            try:
                i = PLATFORM_SELECTION_LIST.index(self.testCardSettings.platform)
            except ValueError:
                print('Error: platform "%s" not in list' % self.testCardSettings.platform)
                i = 0
            self.ComboBox1.SetSelection(i)
            
            
            try:
                i = SCP_SELECTION_LIST.index(self.testCardSettings.scp)
            except ValueError:
                print('Error: SCP "%s" not in list' % self.testCardSettings.scp)
                i = 0
            self.ComboBox2.SetSelection(i)
            
            
            try:
                i = TEST_KEYS_SELECTION_LIST.index(self.testCardSettings.testKeys)
            except ValueError:
                print('Error: test keys "%s" is not in list' % self.testCardSettings.testKeys)
                i = 0
            self.ComboBox3.SetSelection(i)
            
            
            try:
                i = LCS_SELECTION_LIST.index(self.testCardSettings.lcs)
            except ValueError:
                print('Error: LCS "%s" not in list' % self.testCardSettings.lcs)
                i = 0
            self.ComboBox4.SetSelection(i)
            
            
            try: 
                i = INTERFACE_SELECTION_LIST.index(self.testCardSettings.interface)
            except ValueError:
                print('Error: Interface "%s" not ins list' % self.testCardSettings.interface)
                i = 0
            self.ComboBox5.SetSelection(i)
            
            if self.testCardSettings.imageFileName is None:
                pass #print('None')
            else:
                self.testCardSettings.imageFileName
                self.t0.WriteText(self.testCardSettings.imageFileName)
            print(self.testCardSettings.imageFileName)
    
            
            if self.testCardSettings.capFileName is None:
                pass #print('None')
            else:
                self.testCardSettings.capFileName
                self.t2.WriteText(self.testCardSettings.capFileName)
            print(self.testCardSettings.capFileName)
            
            
            if self.testCardSettings.scriptFileName is None:
                pass #print('None')
            else:
                self.testCardSettings.scriptFileName
                self.t1.WriteText(self.testCardSettings.scriptFileName)
            print(self.testCardSettings.scriptFileName)
            
            
            if self.testCardSettings.printFileName is None:
                pass #print('None')
            else:
                self.testCardSettings.printFileName
                self.t3.WriteText(self.testCardSettings.printFileName)
            print(self.testCardSettings.printFileName)
        else:
            pass
          
        
    def OnComboBox1(self, event):
        self.testCardSettings.platform = self.ComboBox1.GetValue()
        print(self.testCardSettings.platform)
        
        
    def OnComboBox2(self, event):
        self.testCardSettings.scp = self.ComboBox2.GetValue()
        print(self.testCardSettings.scp)
        
       
        
    def OnComboBox4(self, event):
        self.testCardSettings.lcs = self.ComboBox4.GetValue()
        print(self.testCardSettings.lcs)
        
    
    def OnComboBox5(self, event):
        self.testCardSettings.interface = self.ComboBox5.GetValue()
        print(self.testCardSettings.interface)
    
        
    def OnQuit(self, e):
        self.Close()        
        

    def OnRef(self, event):
        c = Tk()
        c.withdraw()
        c.clipboard_clear()
        if self.link == ('https://www.linkedin.com/in/christian-schmid-8b4b1b16a'):
            c.clipboard_append(self.link)
            c.update() 
            c.destroy()
            txt = ('Copied LinkedIn link to clipboard')
            cap = ('LinkedIn profile from Christian Schmid')
            wx.MessageBox(txt, cap)
        else:
            self.panel.Destroy()
        
    
    #image-file    
    def onOpenFileName0(self, event):
        self.openFileDialog5 = wx.FileDialog(self.panel, "Open file", wildcard="LDF file(*.fl_ldf)|*.fl_ldf|Hex file(*.hex)|*.hex|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        self.openFileDialog5.ShowModal()
        self.file4 = self.openFileDialog5.GetPath()
        self.t0.Clear()
        self.t0.WriteText(self.file4)
        self.testCardSettings.imageFileName = self.file4
        self.openFileDialog5.Destroy() 
    
        
    #script-file
    def onOpenFileName1(self, event):    
        openFileDialog3 = wx.FileDialog(self.panel, "Open file", wildcard="Jload file(*.jload)|*.jload|Python (*.py)|*.py|SCC file(*.scc)|*.scc|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog3.ShowModal()#
        self.file1 = openFileDialog3.GetPath()
        self.t1.Clear()
        self.t1.WriteText(self.file1)
        self.testCardSettings.scriptFileName = self.file1
        print(self.testCardSettings.scriptFileName)
        openFileDialog3.Destroy()   
    
    
    #cap-file   
    def onOpenFileName2(self, event):    
        openFileDialog2 = wx.FileDialog(self.panel, "Open file", wildcard="CAP file(*.cap)|*.cap|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog2.ShowModal()#
        self.file2 = openFileDialog2.GetPath()
        self.t2.Clear()
        self.t2.WriteText(self.file2)
        self.testCardSettings.capFileName = self.file2
        openFileDialog2.Destroy()
    
    
    #key-file
    def onKey(self, event):
        self.testCardSettings.testKeys = self.ComboBox3.GetValue()
        if self.ComboBox3.GetCurrentSelection() == 3:
            self.openFileDlgBtn3.Bind(wx.EVT_BUTTON, self.onOpenFile3)
        else:
            print(self.ComboBox3.GetCurrentSelection())
    
    
    #key-file
    def onOpenFile3(self, event):    
        openFileDialog = wx.FileDialog(self.panel, "Open file", wildcard="Key file(*.key)|*.key|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()#
        openFileDialog.GetPath()
        self.file = openFileDialog.GetPath()
        self.testCardSettings.keyFileName = self.file
        openFileDialog.Destroy()
        
        
    #print-file
    def onOpenFileName4(self, event):    
        openFileDialog4 = wx.FileDialog(self.panel, "Open file", wildcard="EPS file(*.eps)|*.eps|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog4.ShowModal()
        file3 = openFileDialog4.GetPath()
        self.t3.Clear()
        self.t3.WriteText(file3)
        self.testCardSettings.printFileName = file3
        openFileDialog4.Destroy()   
     
    #preview
    def onOpenFileName5(self, event):
        printPreview = str(self.t3.GetValue())
        testCardProduction = TestCardProduction(printPreview, self.testCardSettings)
        testCardProduction.preview()
        
        
    def onDelFileName0(self, event):
        self.t0.Clear()
        self.testCardSettings.imageFileName = None
        
            
    def onDelFileName1(self, event):
        self.t1.Clear()
        self.testCardSettings.capFileName = None
    
    def onDelFileName2(self, event):
        self.t2.Clear()
        self.testCardSettings.scriptFileName = None
    
    def onDelFileName3(self, event):
        self.t3.Clear()
        self.testCardSettings.printFileName = None
    

    def onExecute(self, flashImage):
        if DBG:
            print('* execute')
            self.testCardSettings.print()
        nCardsToProduce = int(self.t4.GetValue())
        testCardProduction = TestCardProduction(nCardsToProduce, self.testCardSettings)
        testCardProduction.run()

    
    def onOpenSaveFile(self, event):    
        if DBG:
            print('* onOpenSaveFile')
        openFileDialog = wx.FileDialog(self.panel, "Open file", wildcard="TCS files (*.tcs)|*.tcs|All files (*.*)|*.*",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
        openFileDialog.ShowModal()#
        fileName = openFileDialog.GetPath()
        openFileDialog.Destroy()
        try:
            self.t0.Clear()
            self.t1.Clear()
            self.t2.Clear()
            self.t3.Clear()
            self.testCardSettings.load(fileName)
            self.fileName = fileName
            self.update()
        except:
            print('Error reading %s' % fileName)
            
    
    def OnSaveAs(self, event):
        with wx.FileDialog(self, "Save file", wildcard="TCS files (*.tcs)|*.tcs|All files (*.*)|*.*",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            # save the current contents in the file
            self.fileName = fileDialog.GetPath()
        self.testCardSettings.save(self.fileName)
        self.update()
    
    
    def OnSave(self, event):
        if self.fileName is None:
            with wx.FileDialog(self, "Save file", wildcard="TCS files (*.tcs)|*.tcs|All files (*.*)|*.*",
                           style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT) as fileDialog:
                if fileDialog.ShowModal() == wx.ID_CANCEL:
                    return     # the user changed their mind
            # save the current contents in the file
                self.fileName = fileDialog.GetPath()
            self.testCardSettings.save(self.fileName)
        else:
            self.testCardSettings.save(self.fileName)
    
if __name__ == '__main__':
    if IN == ('https://www.linkedin.com/in/christian-schmid-8b4b1b16a'):
    # When this module is run (not imported) then create the app, the
    # frame, show it, and start the event loop.
        app = wx.App()
        testCardSettings = TestCardSettings()
        comboBoxFrame = ComboBoxFrame(testCardSettings)
        comboBoxFrame.Show()
        app.MainLoop()
