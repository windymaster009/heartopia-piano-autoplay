from mido import MidiFile

# Map MIDI note numbers to Heartopia keys
MIDI_TO_KEY = {
    60: 'Q', 62: 'W', 64: 'E', 65: 'R',
    67: 'T', 69: 'Y', 71: 'U',
    72: 'I'
}

mid = MidiFile('song.mid')
out = []

out.append("TEMPO: 1.0\n")

for msg in mid:
    delay_ms = int(msg.time * 1000)
    if delay_ms > 0:
        out.append(f"DELAY: {delay_ms}\n")

    if msg.type == 'note_on' and msg.velocity > 0:
        key = MIDI_TO_KEY.get(msg.note)
        if key:
            out.append(f"Keyboard: {key} : KeyDown\n")
            out.append(f"Keyboard: {key} : KeyUp\n")

with open('note/song.txt', 'w') as f:
    f.writelines(out)

print("Converted successfully!")
