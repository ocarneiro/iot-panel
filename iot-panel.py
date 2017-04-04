import urwid

botao_b1 = urwid.Button("B1")
botao_b2 = urwid.Button("B2")
botao_b3 = urwid.Button("B3")
botoes = [botao_b1, botao_b2, botao_b3]
body = urwid.GridFlow(botoes, 10, 3, 2, 'center')
# body = urwid.Pile(botoes)
# screen = urwid.SolidFill(body)
screen = urwid.Filler(body)

loop = urwid.MainLoop(screen)
loop.run()
