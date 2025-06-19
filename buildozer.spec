[app]

# (str) Title of your application
title = Bluetooth Scanner

# (str) Package name
package.name = btapp

# (str) Package domain (can be anything)
package.domain = org.example

# (str) Source code where your main.py lives
source.dir = .

# (str) Name of your main .py file
source.main = main.py

# (list) List of inclusions
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Python dependencies
requirements = python3,kivy,pyjnius,android

# (str) Supported orientation (landscape, portrait, etc.)
orientation = portrait

# (list) Permissions
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION

# (int) Target API (31 is good for most devices)
android.api = 31

# (int) Minimum API your app supports
android.minapi = 21

# (str) Entry point for the app
entrypoint = main.py

# (str) Icon (optional)
# icon.filename = %(source.dir)s/icon.png

# (str) Presplash (optional)
# presplash.filename = %(source.dir)s/presplash.png

# (str) Package format: apk or aab
android.packaging = apk

# (str) Full screen
fullscreen = 1

# (bool) Hide status bar
android.hide_statusbar = 0

# (str) Supported architectures
android.archs = arm64-v8a, armeabi-v7a

# (str) Application ID (can be same as package.name)
package.id = btapp

# (bool) Include a requirement to open Bluetooth
android.features = android.hardware.bluetooth
