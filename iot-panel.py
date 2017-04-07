#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

import urwid
import paho.mqtt.client as mq

cli = None
terminar = False

def conectar(host="192.168.25.150",port=1883):
    global cli
    cli = mq.Client()
    print(cli.connect(host, port, 60))

def keys(key):
    if key in ('q', 'Q'):
        sair(key)

def sair(evento):
    global terminar
    terminar = True
    raise urwid.ExitMainLoop()

def publicar(mensagem,topic='musica'):
    # print(mensagem)
    if not cli:
        conectar()
    transmissao = cli.publish(topic, str(mensagem))
    # print("Transmissão de %s:%s, 1a tentativa: %s" \
    #       % (topic, mensagem, transmissao.is_published()))
    if not transmissao.is_published():
        cli.reconnect()
        transmissao = cli.publish(topic, mensagem)
        # print("Transmissão de %s:%s, 2a tentativa: %s" \
        #       % (topic, mensagem, transmissao.is_published()))

def pedir_musica():
    print("================================")
    print("    O que você quer ouvir? ")
    print("================================")
    musica = input("")
    publicar(musica, topic='musica')

def mandar_mensagem():
    print("================================")
    print("    Qual o tópico da mensagem? ")
    print("================================")
    topic = input("")
    print("================================")
    print("    Qual a mensagem? ")
    print("================================")
    mensagem = input("")
    publicar(mensagem, topic=topic)

def botao_musica(evento):
    global acao
    acao = pedir_musica
    raise urwid.ExitMainLoop()

def botao_mensagem(evento):
    global acao
    acao = mandar_mensagem
    raise urwid.ExitMainLoop()


botao_b1 = urwid.LineBox(urwid.Button("\nPedir uma Música!!!\n",
                                      on_press=botao_musica))

botao_b2 = urwid.LineBox(urwid.Button("\nMandar Mensagens!\n",
                                      on_press=botao_mensagem))
botao_b3 = urwid.LineBox(urwid.Button("\nSair\n", on_press=sair))
botoes = [botao_b1, botao_b2, botao_b3]
button_container = urwid.Columns(botoes)
header = urwid.Text("O que você quer fazer?")
footer  = urwid.Text("")
p = urwid.Pile([header, button_container, footer])
screen = urwid.Filler(p)
# outer_screen = urwid.Filler(screen)
loop = urwid.MainLoop(screen,
                      unhandled_input=keys)
acao = print

while not terminar:
    loop.run()
    if not terminar:
        acao()
