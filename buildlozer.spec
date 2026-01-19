[app]
title = Tu Truyen Pro
package.name = tutruyen
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.2.1,kivymd,pillow,android,pyjnius
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True
p4a.branch = release-2022.12.20
# QUAN TRỌNG: Dòng này giúp tránh lỗi build
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1