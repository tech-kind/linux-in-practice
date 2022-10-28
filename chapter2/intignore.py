#! /usr/bin/python3
import signal

# SIGINTシグナルを無視するように設定
# 第1引数にはハンドラを設定するシグナルの番号（ここではsignal.SIGINT）
# 第2引数にはシグナルハンドラ（ここではsignal.SIG_IGN）
signal.signal(signal.SIGINT, signal.SIG_IGN)
while True:
    pass