from bottle import route, run
import subprocess

def as_rdio_cmd(cmd):
  return ["osascript", "-e", """tell app "Rdio" to """ + cmd + """"""]

@route('/play_pause')
def play_pause():
  subprocess.call(as_rdio_cmd('playpause'))
  return {'status':'ok'}

@route('/play')
def play():
  subprocess.call(as_rdio_cmd('play'))
  return {'status':'ok'}

@route('/pause')
def pause():
  subprocess.call(as_rdio_cmd('pause'))
  return {'status':'ok'}

@route('/prev_track')
def prev_track():
  subprocess.call(as_rdio_cmd('previous track'))
  return {'status':'ok'}

@route('/next_track')
def next_track():
  subprocess.call(as_rdio_cmd('next track'))
  return {'status':'ok'}


run(host='localhost', port=8080)
