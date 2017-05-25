from pywinauto.application import Application
app = Application().Start(cmd_line=u"notepad.exe")
notepad = app.Notepad
notepad.Wait('ready')

notepad.Edit.type_keys("pywinauto Works!", with_spaces = True)
menu_item = notepad.MenuItem(u'&Arquivo->Salvar\tCtrl+O')
menu_item.Click()

window = app.Dialog
window.Wait('ready')
combobox = window[u'4']
window.combobox.type_keys("pywinauto.txt", with_spaces = True)
button = window.Button
button.Click()
menu_item2 = notepad.MenuItem(u'&Arquivo->Sair\tCtrl+O')
menu_item2.Click()
