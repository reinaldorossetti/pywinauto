import pywinauto
from pywinauto.application import Application, findwindows
from time import sleep
from os import getcwd, path
from pywinauto.application import Application

path_project = getcwd()
print(path_project)
path_app = path.join(path_project, "App\\FlightsGUI.exe")
print(path_app)
app = Application(backend="uia").start(cmd_line=path.join(path_app))
flight_app = app[u"HP MyFlight Sample .*"]
flight_app.exists(30)
flight_app.Edit.select().type_keys("john")
flight_app.Edit2.select().type_keys("HP")
flight_app.OKButton.click()

flight_app.ComboBox.select(u'Zurich')
print(flight_app.ComboBox.texts())
flight_app.ComboBox2.select(u'Denver')
flight_app.ComboBox3.select(u'First')
print(flight_app.ComboBox3.texts())
flight_app.ComboBox4.select(u'99')
flight_app.FindFlightsButton.click()

sleep(3)
print(flight_app.print_control_identifiers(depth=None))

grid = flight_app.child_window(auto_id="flightsDataGrid", control_type="DataGrid")
windows_items = grid.descendants(control_type='DataItem')
list_lines = [item.texts() for item in windows_items]
print(list_lines)

grid = flight_app.child_window(title=list_lines[0][0], control_type="Custom")
menu_item = flight_app.descendants(control_type="Text")
valores = [item.texts() for item in menu_item]

select_viagem = flight_app.child_window(title="166,80", control_type="Text")
select_viagem.click()


# sleep(3)
# flight_app.BACK.click()
# #print(flight_app.print_control_identifiers(depth=None))
# sleep(3)
# menu_item = flight_app.child_window(title="SEARCH ORDER", control_type="TabItem")
# menu_item.select()
# sleep(5)
# print(flight_app.print_control_identifiers(depth=None))
# order = flight_app.child_window(auto_id="byNumberRadio", control_type="RadioButton")
# sleep(3)
# order.select()

# order = flight_app.child_window(auto_id="byNumberWatermark", control_type="Edit")
# order.print_control_identifiers(depth=None)
# order.type_keys("HP")



