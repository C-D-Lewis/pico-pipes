import pretty_midi
import sys
import time
import csv

OUTPUT_NAME = 'midi.csv'

PROGRAM_MAP = {
  1: 'Acoustic Grand Piano',
  2: 'Bright Acoustic Piano',
  3: 'Electric Grand Piano',
  4: 'Honky-tonk Piano',
  5: 'Electric Piano 1',
  6: 'Electric Piano 2',
  7: 'Harpsichord',
  8: 'Clavinet',
  9: 'Celesta',
  10: 'Glockenspiel',
  11: 'Music Box',
  12: 'Vibraphone',
  13: 'Marimba',
  14: 'Xylophone',
  15: 'Tubular Bells',
  16: 'Dulcimer',
  17: 'Drawbar Organ',
  18: 'Percussive Organ',
  19: 'Rock Organ',
  20: 'Church Organ',
  21: 'Reed Organ',
  22: 'Accordion',
  23: 'Harmonica',
  24: 'Tango Accordion',
  25: 'Acoustic Guitar (nylon)',
  26: 'Acoustic Guitar (steel)',
  27: 'Electric Guitar (jazz)',
  28: 'Electric Guitar (clean)',
  29: 'Electric Guitar (muted)',
  30: 'Overdriven Guitar',
  31: 'Distortion Guitar',
  32: 'Guitar harmonics',
  33: 'Acoustic Bass',
  34: 'Electric Bass (finger)',
  35: 'Electric Bass (pick)',
  36: 'Fretless Bass',
  37: 'Slap Bass 1',
  38: 'Slap Bass 2',
  39: 'Synth Bass 1',
  40: 'Synth Bass 2',
  41: 'Violin',
  42: 'Viola',
  43: 'Cello',
  44: 'Contrabass',
  45: 'Tremolo Strings',
  46: 'Pizzicato Strings',
  47: 'Orchestral Harp',
  48: 'Timpani',
  49: 'String Ensemble 1',
  50: 'String Ensemble 2',
  51: 'Synth Strings 1',
  52: 'Synth Strings 2',
  53: 'Choir Aahs',
  54: 'Voice Oohs',
  55: 'Synth Voice',
  56: 'Orchestra Hit',
  57: 'Trumpet',
  58: 'Trombone',
  59: 'Tuba',
  60: 'Muted Trumpet',
  61: 'French Horn',
  62: 'Brass Section',
  63: 'Synth Brass 1',
  64: 'Synth Brass 2',
  65: 'Soprano Sax',
  66: 'Alto Sax',
  67: 'Tenor Sax',
  68: 'Baritone Sax',
  69: 'Oboe',
  70: 'English Horn',
  71: 'Bassoon',
  72: 'Clarinet',
  73: 'Piccolo',
  74: 'Flute',
  75: 'Recorder',
  76: 'Pan Flute',
  77: 'Blown Bottle',
  78: 'Shakuhachi',
  79: 'Whistle',
  80: 'Ocarina',
  81: 'Lead 1 (square)',
  82: 'Lead 2 (sawtooth)',
  83: 'Lead 3 (calliope)',
  84: 'Lead 4 (chiff)',
  85: 'Lead 5 (charang)',
  86: 'Lead 6 (voice)',
  87: 'Lead 7 (fifths)',
  88: 'Lead 8 (bass + lead)',
  89: 'Pad 1 (new age)',
  90: 'Pad 2 (warm)',
  91: 'Pad 3 (polysynth)',
  92: 'Pad 4 (choir)',
  93: 'Pad 5 (bowed)',
  94: 'Pad 6 (metallic)',
  95: 'Pad 7 (halo)',
  96: 'Pad 8 (sweep)',
  97: 'FX 1 (rain)',
  98: 'FX 2 (soundtrack)',
  99: 'FX 3 (crystal)',
  100: 'FX 4 (atmosphere)',
  101: 'FX 5 (brightness)',
  102: 'FX 6 (goblins)',
  103: 'FX 7 (echoes)',
  104: 'FX 8 (sci-fi)',
  105: 'Sitar',
  106: 'Banjo',
  107: 'Shamisen',
  108: 'Koto',
  109: 'Kalimba',
  110: 'Bag pipe',
  111: 'Fiddle',
  112: 'Shanai',
  113: 'Tinkle Bell',
  114: 'Agogo',
  115: 'Steel Drums',
  116: 'Woodblock',
  117: 'Taiko Drum',
  118: 'Melodic Tom',
  119: 'Synth Drum',
  120: 'Reverse Cymbal',
  121: 'Guitar Fret Noise',
  122: 'Breath Noise',
  123: 'Seashore',
  124: 'Bird Tweet',
  125: 'Telephone Ring',
  126: 'Helicopter',
  127: 'Applause',
  128: 'Gunshot'
}

file_name = sys.argv[1]
play_tracks = sys.argv[2].split(',')
print(f"file_name: {file_name}, play_tracks: {play_tracks}")

data = {
  'instruments': [],
  'timeline': []
}

# Add a new event to the timeline
def add_event(track, is_on, pitch, at):
  data['timeline'].append({
    'track': track,
    'is_on': is_on,
    'pitch': pitch,
    'at': at
  })

# The main function
def main():
  # Load midi file
  midi_data = pretty_midi.PrettyMIDI(file_name)
  print()
  
  # Read instruments - skip the drums
  non_drum_instruments = []
  for i, instrument in enumerate(midi_data.instruments):
    if not instrument.is_drum:
      program_name = PROGRAM_MAP[instrument.program] if instrument.program > 0 else 'Unknown'
      num_notes = len(instrument.notes)
      selected = {
        'pm_instrument': instrument,
        'program_name': program_name,
        'num_notes': num_notes,
        'summary': f"Track {i} ({program_name}): {num_notes} notes"
      }
      non_drum_instruments.append(selected)
      print(selected['summary'])
  
  # Select instruments from constant list
  print()
  for i in range(0, len(play_tracks)):
    data['instruments'].append(non_drum_instruments[int(play_tracks[i])])
    print(f"using: {data['instruments'][i]['summary']}")

  # Build list of events of on and off for all tracks
  for (i, instrument) in enumerate(data['instruments']):
    for note in instrument['pm_instrument'].notes:
      # On event
      add_event(i, True, note.pitch, note.start)
      # Off event
      add_event(i, False, note.pitch, note.end)

  # Sort timeline by 'at' for list of events
  data['timeline'] = sorted(data['timeline'], key = lambda p: p['at']) 

  # Compile Python table
  output = ""
  for event in data['timeline']:
    output += f"{event['track']}"
    output += ","
    output += f"{1 if event['is_on'] == True else 0}"
    output += ","
    output += f"{event['pitch']}"
    output += ","
    output += f"{round(event['at'], 3)}"
    output += '\n'
  print(f"\nbuild size: {len(output)} bytes")

  # Write to Python file - must be as small as possible
  with open(OUTPUT_NAME, 'w', newline='') as file:
    file.write(output)

if '__main__' in __name__:
  main()
