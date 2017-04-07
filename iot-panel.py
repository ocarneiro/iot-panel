import urwid

def keys(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()

botao_b1 = urwid.Button("B1")
botao_b2 = urwid.Button("B2")
botao_b3 = urwid.Button("B3")
botoes = [botao_b1, botao_b2, botao_b3]
button_container = urwid.Columns(botoes)
# body = urwid.GridFlow(button_container, 10, 3, 2, 'center')
header = urwid.Text("Header messages and instructions goes here")
# header = urwid.Filler(msgs)
footer  = urwid.Text("Footer additional options here")
# footer = urwid.Filler(options)
# center_frame = urwid.Pile([('pack', header),
#                            body,
#                            ('pack', footer)])
# center_frame = urwid.Frame(body, header, footer)
# inner_screen = urwid.Filler(body, 'middle', 'flow')
p = urwid.Pile([header, button_container, footer])
screen = urwid.Filler(p)
# outer_screen = urwid.Filler(screen)
loop = urwid.MainLoop(screen,
                      unhandled_input=keys)
loop.run()
