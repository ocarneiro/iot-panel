import urwid

def show_or_exit(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    txt.set_text(repr(key))

def apertei(botao):
    txt.set_text(botao.label)

txt = urwid.Text(u"Estou aqui!!")
bt = urwid.AttrMap(urwid.Button(u"Olha pra mim!"),None)
bt2 = urwid.Button(u"Unicode no cabeção!")
pile = urwid.Pile([txt,bt2])
fill = urwid.Filler(pile, "top")
loop = urwid.MainLoop(fill, unhandled_input=show_or_exit)
loop.run()




# loop = urwid.MainLoop(pile,
def dont():
    tela = urwid.Overlay(pile, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
              align='center', width=('relative', 60),
              valign='middle', height=('relative', 60),
              min_width=20, min_height=9)
 
