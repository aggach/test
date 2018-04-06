def Test2():
    Var1 = "fyrdytuio"
    Aliases.explorer.wndShell_TrayWnd.ReBarWindow32.MSTaskSwWClass.MSTaskListWClass.Click(494, 26)
    Aliases.notepad.wndNotepad.Edit.Keys("ygiugukxt[Enter]")
    Aliases.notepad.wndNotepad.Edit.Keys(Var1)
    
def GeneralEvents_OnLogError(Sender, LogParams):
  Sys.Process("notepad").Terminate()
  pass
