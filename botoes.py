import urwid

def apertei(botao):
    if botao.label == u"Sair!":
        raise urwid.ExitMainLoop()
    txt.set_text(botao.label)

txt = urwid.Text(u"Estou aqui!!")
bt = urwid.Button(u"Olha pra mim!", on_press=apertei)
bt2 = urwid.Button(u"Unicode no cabeção!", on_press=apertei)
bt3 = urwid.Button(u"Sair!", on_press=apertei)
pile = urwid.Pile([txt,bt,bt2,bt3])
fill = urwid.Filler(pile, "top")
loop = urwid.MainLoop(fill)  # , unhandled_input=show_or_exit)
loop.run()




# loop = urwid.MainLoop(pile,
def dont():
    tela = urwid.Overlay(pile, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
              align='center', width=('relative', 60),
              valign='middle', height=('relative', 60),
              min_width=20, min_height=9)
 
