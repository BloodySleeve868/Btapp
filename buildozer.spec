[app]
title = Bluetooth Scanner
package.name = btapp
package.domain = org.example
source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,pyjnius,android,android_permissions,cython
orientation = portrait
android.permissions = BLUETOOTH, BLUETOOTH_ADMIN, ACCESS_FINE_LOCATION
android.api = 30
android.ndk_path = $ANDROID_NDK
android.sdk_path = $ANDROID_SDK
android.ndk_api = 21
android.minapi = 21
entrypoint = main.py
android.packaging = apk
fullscreen = 1
android.hide_statusbar = 0
android.archs = arm64-v8a, armeabi-v7a
package.id = btapp
android.features = android.hardware.bluetooth
[buildozer]
warn_on_root = 1

