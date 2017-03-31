import urwid

txt = urwid.Text("Ola, Mundo!")
fill = urwid.Filler(txt, "top")
loop = urwid.MainLoop(fill)
loop.run()

