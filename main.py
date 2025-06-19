from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from jnius import autoclass
from android.permissions import request_permissions, Permission

class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)

        self.label = Label(text="Press the button to start Bluetooth scan")
        self.add_widget(self.label)

        self.button = Button(text="Start Scan")
        self.button.bind(on_press=self.start_scan)
        self.add_widget(self.button)

        # Request necessary permissions
        request_permissions([
            Permission.BLUETOOTH,
            Permission.BLUETOOTH_ADMIN,
            Permission.ACCESS_FINE_LOCATION
        ])

        self.adapter = autoclass('android.bluetooth.BluetoothAdapter').getDefaultAdapter()

    def start_scan(self, instance):
        if not self.adapter.isEnabled():
            self.label.text = "Bluetooth is OFF. Turn it on first."
        else:
            self.adapter.startDiscovery()
            self.label.text = "Scanning... (real-time results coming soon)"

class BluetoothScannerApp(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    BluetoothScannerApp().run()
