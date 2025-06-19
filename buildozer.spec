[app]
title = Bluetooth Scanner
package.name = btapp
package.domain = org.example
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius,android
orientation = portrait
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION
android.api = 31
android.minapi = 21
entrypoint = main.py
android.packaging = apk
fullscreen = 1
android.hide_statusbar = 0
android.archs = arm64-v8a, armeabi-v7a
package.id = btapp
android.features = android.hardware.bluetooth
[buildozer]
