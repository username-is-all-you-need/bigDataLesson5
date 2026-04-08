import os, sys
for p in sys.path:
    qt_plugins = os.path.join(p, 'PyQt5', 'Qt5', 'plugins')
    if os.path.exists(qt_plugins):
        print(f"找到路径: {qt_plugins}")
        break