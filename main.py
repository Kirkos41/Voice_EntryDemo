import pvporcupine


porcupine = pvporcupine.create(
  access_key='oqbZibWdlALoAw6AFoXrUyMP7hfDNOi6OcT4Uwof4+M+rbWG0gSSLg==',
  keywords=['alexa', 'jarvis'])
)

def get_next_audio_frame():
  pass

while True:
  audio_frame = get_next_audio_frame()
  keyword_index = porcupine.process(audio_frame)
  if keyword_index == 0:
      print("Detected PI")
  elif keyword_index == 1:
      print("Detected BUMB")

porcupine.delete()
