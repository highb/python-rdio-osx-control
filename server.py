from bottle import route, run, get, response
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

# Doesn't work so well right now
@get('/track_art')
def get_track_art():
  artwork = subprocess.check_output(as_rdio_cmd('get the artwork of the current track'))
  response.content_type = 'image/tiff'
  return artwork

@get('/track_info')
def get_track_info():
  name = subprocess.check_output(as_rdio_cmd('get the name of the current track'))
  artist = subprocess.check_output(as_rdio_cmd('get the artist of the current track'))
  album = subprocess.check_output(as_rdio_cmd('get the album of the current track'))
  duration = subprocess.check_output(as_rdio_cmd('get the duration of the current track'))
  rdio_url = subprocess.check_output(as_rdio_cmd('get the rdio url of the current track'))
  return {
      'name':name,
      'artist':artist,
      'album':album,
      'duration':duration,
      'rdio_url':rdio_url
      }


run(host='localhost', port=8080)
