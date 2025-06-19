from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

# Try importing Android permissions (only works on real device)
try:
    from android.permissions import request_permissions, Permission
    from jnius import autoclass
    android_available = True
except ImportError:
    android_available = False

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.label = Label(text="Bluetooth Scanner", size_hint_y=None, height=50)
        self.add_widget(self.label)

        self.scan_btn = Button(text="Scan for Devices", size_hint_y=None, height=50)
        self.scan_btn.bind(on_press=self.scan_devices)
        self.add_widget(self.scan_btn)

        self.result_box = GridLayout(cols=1, size_hint_y=None)
        self.result_box.bind(minimum_height=self.result_box.setter('height'))

        self.scroll = ScrollView()
        self.scroll.add_widget(self.result_box)
        self.add_widget(self.scroll)

    def scan_devices(self, instance):
        self.result_box.clear_widgets()

        if not android_available:
            self.result_box.add_widget(Label(text="Android permissions not available."))
            return

        Context = autoclass('org.kivy.android.PythonActivity').mActivity
        BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')

        adapter = BluetoothAdapter.getDefaultAdapter()

        if not adapter.isEnabled():
            adapter.enable()
            self.result_box.add_widget(Label(text="Enabling Bluetooth..."))

        bonded = adapter.getBondedDevices().toArray()
        if bonded:
            self.result_box.add_widget(Label(text="Paired Devices:"))
            for device in bonded:
                self.result_box.add_widget(Label(text=f"{device.getName()} ({device.getAddress()})"))
        else:
            self.result_box.add_widget(Label(text="No paired devices found."))

class BTApp(App):
    def build(self):
        if android_available:
            request_permissions([
                Permission.BLUETOOTH,
                Permission.BLUETOOTH_ADMIN,
                Permission.ACCESS_FINE_LOCATION
            ])
        return MainLayout()

if __name__ == '__main__':
    BTApp().run()
