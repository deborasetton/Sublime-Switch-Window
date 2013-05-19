import sublime, sublime_plugin
import commands
import os

from subprocess import Popen, PIPE

class SwitchWindowCommand(sublime_plugin.ApplicationCommand):

  def script_path(self, script_name):
    return os.path.join(sublime.packages_path(), 'SwitchWindow', script_name)

  def window_items(self):
    output = Popen([self.script_path('run_get_windows.sh')], stdout=PIPE)
    f = open(self.script_path('open_windows.out'))
    lines = f.readlines()
    f.close()

    # A much better way to do it, that doesn't work:
    # proc = Popen(['run_get_windows.sh'], stdout=PIPE)
    # lines = proc.stdout.read()

    items = [val.decode('utf-8') for val in lines[0].split(',') if self.is_valid(val)]
    return items

  def selected_window(self, index):
    # The right way to do it, that doesn't work in OSX:
    # window = sublime.windows()[index]
    # window.focus_view(window.active_view())

    if index != -1:
      i = index - len(self.window_items())
      output = Popen([self.script_path('set_window.sh'), str(i)], stdout=PIPE)

  def is_valid(self, val):
    invalid = ['Minimize', 'Minimize All', 'Zoom', 'Zoom All', 'missing value', 'Bring All to Front', 'Arrange in Front']
    if val.strip() in invalid:
      return False
    return True

  def run(self):
    sublime.active_window().show_quick_panel(self.window_items(), self.selected_window)

