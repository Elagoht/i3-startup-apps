# i3-startup-apps

This script lets you to locate your startup apps into ~/.config/autostart/ directory. Just place the .desktop files here and run the script.

To run script run this command:

```sh
curl -fsSl https://raw.githubusercontent.com/Elagoht/i3-startup-apps/main/refresh-autostart.py | python
```

A config file will be created on your i3 config directory. Then you must include that file on your i3 config file.

Simply **add this line** to your config file:

> include ~/.config/i3/startup-apps

