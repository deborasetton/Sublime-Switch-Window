#!/usr/bin/env osascript

tell application "System Events"
  tell process "Sublime Text 2"
    return name of every menu item of menu 1 of menu bar item "Window" of menu bar 1
  end tell
end tell
