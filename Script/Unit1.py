def Dane_do_sprawy():
    #Runs the "starter" tested application.
    TestedApps.starter.Run(1, True)
    #Enters the text 'a' in the 'Edit' text editor.
    Aliases.komornik.dlg.Edit.SetText("a")
    #Enters the text 'a' in the 'Edit2' text editor.
    Aliases.komornik.dlg.Edit2.SetText("a")
    #Clicks the 'btnZaloguj' button.
    Aliases.komornik.dlg.btnZaloguj.ClickButton()
    #Clicks the 32805 item of the 'Item' toolbar.
    Aliases.komornik.wndAfx.Item.ClickItem(32805, False)
    #Clicks at point (166, 66) of the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView140.AfxMDIFrame140.AfxMDIFrame140.ListView.Click(166, 66)
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView140.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgNowaSprawa.btnZapisz.ClickButton()
    #Double-clicks the '|Tytuły wykonawcze' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Tytuły wykonawcze")
    #Clicks the '|Tytuły wykonawcze' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.ClickItem("|Tytuły wykonawcze")
    #Clicks at point (128, 110) of the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Click(128, 110)
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Selects the 'Postanowienie o nadaniu klauzuli wykonalności' item of the 'ComboBox' combo box.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.ComboBox.ClickItem("Postanowienie o nadaniu klauzuli wykonalności")
    #Clicks at point (147, 8) of the 'Edit' object.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.Edit.Click(147, 8)
    #Enters the text '12m' in the 'Edit' text editor.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.Edit.SetText("12m")
    #Sets the 'DateTimePick' date/time picker's check box to the True state.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.DateTimePick.wChecked = True
    #Sets the date '22.03.2018' in the 'DateTimePick' date/time picker.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.DateTimePick.wDate = "22.03.2018"
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgWstawTytu_Wykonawczy.btnZapisz.ClickButton()
    #Double-clicks the '|Wierzyciele' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Wierzyciele")
    #Clicks the '|Wierzyciele' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.ClickItem("|Wierzyciele")
    #Clicks at point (152, 100) of the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Click(152, 100)
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Clicks the 'btnAnuluj' button.
    Aliases.komornik.dlgWstawianieOsobyZListy.btnAnuluj.ClickButton()
    #Enters the text 'Białek' in the 'Edit' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit.SetText("Białek")
    #Enters the text 'Sławomir' in the 'Edit2' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit2.SetText("Sławomir")
    #Enters the text 'test' in the 'Edit3' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit3.SetText("test")
    #Enters the text '1' in the 'Edit4' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit4.SetText("1")
    #Enters the text 'Kraków' in the 'Edit5' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit5.SetText("Kraków")
    #Enters the text '12-222' in the 'Edit6' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit6.SetText("12-222")
    #Enters the text 'Kraków' in the 'Edit7' text editor.
    Aliases.komornik.dlgWstawWierzyciela.page32770.Edit7.SetText("Kraków")
    #Selects the 'Dane uzup.' tab of the 'tbcWstawWierzyciela' tab control.
    Aliases.komornik.dlgWstawWierzyciela.tbcWstawWierzyciela.ClickTab("Dane uzup.")
    #Enters text in the text editor.
    Aliases.komornik.dlgWstawWierzyciela.page327702.Edit.SetText("7356702693")
    #Enters text in the text editor.
    Aliases.komornik.dlgWstawWierzyciela.page327702.editRegon.SetText("833876061")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgWstawWierzyciela.btnZapisz.ClickButton()
    #Double-clicks the '|Wierzyciele|Rachunki bankowe' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Wierzyciele|Rachunki bankowe")
    #Clicks the 0 subitem of the ' ( brak ) ' item of the 'ListView2' list view.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView2.ClickItem(" ( brak ) ")
    #Enters '[Ins]' in the 'ListView2' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView2.Keys("[Ins]")
    #Clicks at point (62, 9) of the 'Edit' object.
    Aliases.komornik.dlgDaneKontBank.Edit.Click(62, 9)
    #Drags from point (62, 8) of the 'Edit' object to offset (-98, 5).
    Aliases.komornik.dlgDaneKontBank.Edit.Drag(62, 8, -98, 5)
    #Enters the text '70200001' in the 'Edit' text editor.
    Aliases.komornik.dlgDaneKontBank.Edit.SetText("70200001")
    #Clicks the 'btn1' button.
    Aliases.komornik.dlgDaneKontBank.btn1.ClickButton()
    #Clicks the 'Testowy bank' subitem of the 0 item of the 'List1' list view.
    Aliases.komornik.dlgListaDost_pnychBank_w.List1.ClickItem(0, "Testowy bank")
    #Clicks the 'btnPrzepisz' button.
    Aliases.komornik.dlgListaDost_pnychBank_w.btnPrzepisz.ClickButton()
    #Clicks the 'btnOK' button.
    Aliases.komornik.dlgDaneKontBank.btnOK.ClickButton()
    #Double-clicks the '|Dłużnicy' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Dłużnicy")
    #Clicks the 1 subitem of the ' ( brak ) ' item of the 'ListView' list view.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.ClickItem(" ( brak ) ", 1)
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Clicks the 'btnAnuluj' button.
    Aliases.komornik.dlgWstawianieOsobyZListy.btnAnuluj.ClickButton()
    #Enters the text 'Małek' in the 'Edit' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit.SetText("Małek")
    #Enters the text 'Wioletta' in the 'Edit2' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit2.SetText("Wioletta")
    #Enters the text 'krakowska' in the 'Edit3' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit3.SetText("krakowska")
    #Enters the text '5' in the 'Edit4' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit4.SetText("5")
    #Enters the text 'Kraków' in the 'Edit5' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit5.SetText("Kraków")
    #Enters the text '21-333' in the 'Edit6' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit6.SetText("21-333")
    #Enters the text 'Kraków' in the 'Edit7' text editor.
    Aliases.komornik.dlgWstawD_u_nika.page32770.Edit7.SetText("Kraków")
    #Selects the 'Dane uzup.' tab of the 'tbcWstawD_u_nika' tab control.
    Aliases.komornik.dlgWstawD_u_nika.tbcWstawD_u_nika.ClickTab("Dane uzup.")
    #Enters text in the text editor.
    Aliases.komornik.dlgWstawD_u_nika.page327702.Edit.SetText("7356702693")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgWstawD_u_nika.btnZapisz.ClickButton()
    #Clicks the 'btnNie' button.
    Aliases.komornik.dlg.btnNie.ClickButton()
    #Double-clicks the '|Dłużnicy|Rachunki bankowe' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Dłużnicy|Rachunki bankowe")
    #Clicks the '|Dłużnicy|Rachunki bankowe' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.ClickItem("|Dłużnicy|Rachunki bankowe")
    #Clicks the 0 subitem of the ' ( brak ) ' item of the 'ListView2' list view.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView2.ClickItem(" ( brak ) ")
    #Enters '[Ins]' in the 'ListView2' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView2.Keys("[Ins]")
    #Drags from point (44, 9) of the 'Edit' object to offset (-78, -2).
    Aliases.komornik.dlgDaneKontBank.Edit.Drag(44, 9, -78, -2)
    #Enters the text '70200001' in the 'Edit' text editor.
    Aliases.komornik.dlgDaneKontBank.Edit.SetText("70200001")
    #Clicks the 'btn1' button.
    Aliases.komornik.dlgDaneKontBank.btn1.ClickButton()
    #Clicks the 'btnPrzepisz' button.
    Aliases.komornik.dlgListaDost_pnychBank_w.btnPrzepisz.ClickButton()
    #Clicks the 'btnOK' button.
    Aliases.komornik.dlgDaneKontBank.btnOK.ClickButton()
    #Double-clicks the '|Uczestnicy postęp.' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Uczestnicy postęp.")
    #Clicks the '|Uczestnicy postęp.' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.ClickItem("|Uczestnicy postęp.")
    #Expands the '|Uczestnicy postęp.' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.ExpandItem("|Uczestnicy postęp.")
    #Clicks the 0 subitem of the ' ( brak ) ' item of the 'ListView' list view.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.ClickItem(" ( brak ) ")
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Enters '![ReleaseLast]' in the 'Edit' object.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit.Keys("![ReleaseLast]")
    #Enters the text 'Nowal' in the 'Edit' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit.SetText("Nowal")
    #Enters the text 'Magdalena' in the 'Edit2' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit2.SetText("Magdalena")
    #Selects the 'ul.' item of the 'ComboBox' combo box.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.ComboBox.ClickItem("ul.")
    #Enters the text 'testowa' in the 'Edit3' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit3.SetText("testowa")
    #Enters the text '12' in the 'Edit4' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit4.SetText("12")
    #Enters the text 'Test' in the 'Edit5' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit5.SetText("Test")
    #Enters the text '32-111' in the 'Edit6' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit6.SetText("32-111")
    #Enters the text 'Test' in the 'Edit7' text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit7.SetText("Test")
    #Enters text in the text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit8.SetText("5611121698")
    #Enters text in the text editor.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.page32770.Edit9.SetText("658703309")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgWstawUczestnikaPost_powania.btnZapisz.ClickButton()
    #Selects the 'Dane kont bank.' tab of the 'tbcEdytujDaneUczestnikaPost_powania' tab control.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.tbcEdytujDaneUczestnikaPost_powania.ClickTab("Dane kont bank.")
    #Clicks the 0 subitem of the 0 item of the 'List1' list view.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.List1.ClickItem(0)
    #Enters '[Ins]' in the 'List1' object.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.List1.Keys("[Ins]")
    #Enters the text '65621688347245289482390443' in the 'Edit7' text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit7.SetText("65621688347245289482390443")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit.SetText("Bank testowy")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit2.SetText("zmyślna")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit3.SetText("1")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit4.SetText("Kraków")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit5.SetText("12-777")
    #Enters text in the text editor.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.Edit6.SetText("Kraków")
    #Selects the 'ul.' item of the 'ComboBox' combo box.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.page32770.ComboBox.ClickItem("ul.")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgEdytujDaneUczestnikaPost_powania.btnZapisz.ClickButton()
    #Double-clicks the '|Inne (sz: 9; sw 0)' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Inne (sz: 9; sw 0)")
    #Sets the 'VScroll' scrollbar control to position 285.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.page32770.VScroll.Pos = 285
    #Clicks the 'btnOpisRoszczenia' button.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.page32770.btnOpisRoszczenia.ClickButton()
    #Sets the state of the 'checkZabezpieczenieCywilne' check box to cbChecked.
    Aliases.komornik.dlgOpisRoszczenia.checkZabezpieczenieCywilne.ClickButton(cbChecked)
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgOpisRoszczenia.btnZapisz.ClickButton()
    #Sets the 'VScroll' scrollbar control to position 78.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.page32770.VScroll.Pos = 78
    #Selects the 'Przekazana od kom. sądowego' item of the 'ComboBox' combo box.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.page32770.ComboBox.ClickItem("Przekazana od kom. sądowego")
    #Clicks the 'btn1' button.
    Aliases.komornik.dlgPrzekazanaOdKomornikaS_dowego.btn1.ClickButton()
    #Moves the mouse cursor to the menu item specified and then simulates a single click.
    Aliases.komornik.dlgPrzekazanaOdKomornikaS_dowego.btn1.PopupMenu.Click("Wybierz...")
    #Clicks the 0 subitem of the 'Komornik Sądowy przy Sądzie Rejonowym  Gdańsk-Południe w Gdańsku Adam Kosik' item of the 'List3' list view.
    Aliases.komornik.dlgWybierzUrz_dDoPrzepisania.List3.ClickItem("Komornik Sądowy przy Sądzie Rejonowym  Gdańsk-Południe w Gdańsku Adam Kosik")
    #Clicks the 'btnPrzepisz' button.
    Aliases.komornik.dlgWybierzUrz_dDoPrzepisania.btnPrzepisz.ClickButton()
    #Enters the text '1/18' in the 'Edit' text editor.
    Aliases.komornik.dlgPrzekazanaOdKomornikaS_dowego.Edit.SetText("1/18")
    #Clicks the 'btnOK' button.
    Aliases.komornik.dlgPrzekazanaOdKomornikaS_dowego.btnOK.ClickButton()
    #Double-clicks the '|Stan sprawy|Roszczenie' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Stan sprawy|Roszczenie")
    #Clicks the 1 subitem of the ' ( brak ) ' item of the 'ListView' list view.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.ClickItem(" ( brak ) ", 1)
    #Enters '[Ins]' in the 'ListView' object.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.AfxMDIFrame140.ListView.Keys("[Ins]")
    #Enters the text '20 000,00' in the 'Text' text editor.
    Aliases.komornik.dlgWstawRoszczenie.page32770.Item.Text.SetText("20 000,00")
    #Clicks the 'btnZapisz' button.
    Aliases.komornik.dlgWstawRoszczenie.btnZapisz.ClickButton()
    #Double-clicks the '|Czynności' item of the 'TreeView' tree.
    Aliases.komornik.wndAfx.MDIClient.wndAfxFrameOrView1402.AfxMDIFrame140.TreeView.DblClickItem("|Czynności")
    Aliases.notepad.wndNotepad.Edit.Keys(Var1)
