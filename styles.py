
from tkinter import *
from tkinter import ttk
import tkinter as tk

#############
# Utilities #
#############

class BetterWidget(object):
    """A BetterWidget returns itself on pack and config for call chaining."""
    def pack(self, **kwargs):
        super().pack(**kwargs)
        return self

    def config(self, **kwargs):
        super().config(**kwargs)
        return self

class TextWidget(BetterWidget):
    """A TextWidget contains a mutable line of text."""
    def __init__(self, **kwargs):
        self.textvar = kwargs.get('textvariable', tk.StringVar())
        self.config(textvariable=self.textvar)
        if 'text' in kwargs:
            self.textvar.set(kwargs['text'])

    @property
    def text(self):
        return self.textvar.get()

    @text.setter
    def text(self, value):
        return self.textvar.set(str(value))

class Text(tk.Text):
    """A Text is a text box."""
    def __init__(self, parent, **kwargs):
        kwargs.update(text_theme)
        tk.Text.__init__(self, parent, **kwargs)

class Label(TextWidget, tk.Label):
    """A Label is a text label."""
    def __init__(self, parent, **kwargs):
        kwargs.update(label_theme)
        tk.Label.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Button(BetterWidget, tk.Button):
    """A Button is an interactive button."""
    def __init__(self, *args, **kwargs):
        kwargs.update(button_theme)
        tk.Button.__init__(self, *args, **kwargs)

class ComboBox(BetterWidget, ttk.Combobox):
    """A Button is an interactive button."""
    def __init__(self, *args, **kwargs):
        kwargs.update(combo_box_theme)
        tk.Button.__init__(self, *args, **kwargs)


class Entry(TextWidget, tk.Entry):
    """An Entry widget accepts text entry."""
    def __init__(self, parent, **kwargs):
        kwargs.update(entry_theme)
        tk.Entry.__init__(self, parent, **kwargs)
        TextWidget.__init__(self, **kwargs)

class Frame(BetterWidget, tk.Frame):
    """A Frame contains other widgets."""
    def __init__(self, *args, **kwargs):
        kwargs.update(frame_theme)
        tk.Frame.__init__(self, *args, **kwargs)

class IORedirector(object):
    """A general class for redirecting I/O to this Text widget."""
    def __init__(self, text_area):
        self.text_area = text_area

class StdoutRedirector(IORedirector):
    """A class for redirecting stdout to this Text widget."""
    def write(self, text):
        self.text_area.insert(END, text)
        self.text_area.see(END)

    def flush(self):
        pass  # No-op to prevent crash (https://stackoverflow.com/a/43014145).



##########
# THEMES #
##########

select_bg = '#a6d785'
bg='#000000'
fg='#ffffff'
font=('Arial', 10)
height=5  # Lines

frame_theme = {
    'bg': bg,
}

label_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
}

text_theme = {
    'font': font,
    'bg': bg,
    'fg': fg,
    'height': height,
}

button_theme = {
    'font': font,
    'activebackground': select_bg,
    'bg': bg,
    'fg': fg,
}

combo_box_theme = {
    'font': font,
    'activebackground': select_bg,
    'bg': bg,
    'fg': fg,
}

entry_theme = {
    'fg': fg,
    'bg': bg,
    'font': font,
    'insertbackground': fg,
}