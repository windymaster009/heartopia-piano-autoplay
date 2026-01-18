import pydirectinput
import keyboard
import time
import threading
import argparse
import os
import re

pydirectinput.PAUSE = 0
DEFAULT_TEMPO = 1.0
MIN_DELAY_MS = 10

KEY_MAP = {
    'Q': 'q',
    'W': 'w',
    'E': 'e',
    'R': 'r',
    'T': 't',
    'Y': 'y',
    'U': 'u',
    'I': 'i',
    'D2': '2',
    'D3': '3',
    'D5': '5',
    'D6': '6',
    'D7': '7',
    'Z': 'z',
    'X': 'x',
    'C': 'c',
    'V': 'v',
    'B': 'b',
    'N': 'n',
    'M': 'm',
    'S': 's',
    'D': 'd',
    'G': 'g',
    'H': 'h',
    'J': 'j',
    'L': 'l',
    'O': 'o',
    'P': 'p',
    'D0': '0',
    'KeyCode186': ';',
    'KeyCode191': '/',
    'KeyCode189': '-',
    'KeyCode188': ',',
    'KeyCode219': '[',
    'KeyCode221': ']',
    'KeyCode187': '=',
    'KeyCode190': '.'
}

is_playing = False
stop_request = False
target_file = None
note_folder = "note"
txt_files = []

def play_music(filename):
    global is_playing, stop_request
    
    current_tempo = DEFAULT_TEMPO
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        for line in lines:
            if "TEMPO" in line:
                match = re.search(r"TEMPO\s*:\s*([\d.]+)", line)
                if match:
                    current_tempo = float(match.group(1))
                    print(f"Tempo found in file: {current_tempo}")
                break

        print(f"Starting playback: {filename} (Speed: {current_tempo})")
        print("Switch to game window within 3 seconds...")
        time.sleep(3)
        
        total_lines = len(lines)
        print("")
        
        i = 0
        while i < len(lines):
            if stop_request: break
            
            current_percent = int((i / total_lines) * 100)
            bar_length = 40
            filled_length = int(bar_length * i / total_lines)
            bar = '=' * filled_length + '>' + ' ' * (bar_length - filled_length - 1)
            print(f'\rProgress: [{bar}] {current_percent}%', end='', flush=True)
            
            line = lines[i].strip()
            
            if not line or line.startswith('[') or "TEMPO" in line:
                i += 1
                continue

            if "DELAY" in line:
                ms_str = "".join(filter(str.isdigit, line))
                if ms_str:
                    delay_ms = int(ms_str)
                    if delay_ms >= MIN_DELAY_MS:
                        time.sleep((delay_ms / 1000) * current_tempo)
                i += 1
            
            elif "Keyboard" in line:
                batch = []
                while i < len(lines):
                    current_line = lines[i].strip()
                    if not current_line or "DELAY" in current_line or not "Keyboard" in current_line:
                        break
                    
                    parts = current_line.split(':')
                    if len(parts) >= 3:
                        key_raw = parts[1].strip()
                        action = parts[2].strip()
                        key_to_press = KEY_MAP.get(key_raw, key_raw.lower())
                        batch.append((key_to_press, action))
                    i += 1
                
                for key_to_press, action in batch:
                    try:
                        if action == "KeyDown":
                            pydirectinput.keyDown(key_to_press)
                        elif action == "KeyUp":
                            pydirectinput.keyUp(key_to_press)
                    except:
                        pass
            else:
                i += 1

    except FileNotFoundError:
        print(f"\nFile not found: {filename}")
    except Exception as e:
        print(f"\nError: {e}")
    
    print("\nPlayback completed (100%)")
    is_playing = False

def toggle():
    global is_playing, stop_request, target_file
    if not is_playing:
        if target_file is None:
            print("\nNo file selected. Press F3 to select a file.")
            return
        is_playing = True
        stop_request = False
        t = threading.Thread(target=play_music, args=(target_file,))
        t.daemon = True
        t.start()
    else:
        print("\nStopping playback immediately...")
        stop_request = True

def select_file():
    global target_file, is_playing, txt_files, note_folder
    
    if is_playing:
        print("\nCannot select file while playing. Press F4 to stop first.")
        return
    
    print("\n" + "=" * 50)
    print(f"Available files in '{note_folder}/' folder:")
    print("-" * 50)
    for idx, filename in enumerate(txt_files, 1):
        print(f"{idx}. {filename}")
    print("-" * 50)
    
    while True:
        try:
            choice = input("\nSelect file number: ")
            file_idx = int(choice) - 1
            if 0 <= file_idx < len(txt_files):
                target_file = os.path.join(note_folder, txt_files[file_idx])
                print(f"\nSelected file: {txt_files[file_idx]}")
                print("Press F4 to start playback.\n")
                break
            else:
                print("Invalid number. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nSelection cancelled.\n")
            break

if __name__ == "__main__":
    print("=" * 50)
    print("Heartopia Auto Piano Player")
    print("=" * 50)
    
    if not os.path.exists(note_folder):
        print(f"Error: Folder '{note_folder}/' not found")
        print("Please create a 'note' folder and add your .txt files")
        input("Press Enter to exit...")
        exit()
    
    txt_files = [f for f in os.listdir(note_folder) if f.endswith('.txt')]
    
    if not txt_files:
        print(f"No .txt files found in '{note_folder}/' folder")
        input("Press Enter to exit...")
        exit()
    
    select_file()
    
    print("\nControls:")
    print("  F3  - Select another file")
    print("  F4  - Start/Stop playback")
    print("  ESC - Exit program")
    print("\nReady. Press F4 to start...\n")
    
    keyboard.add_hotkey('f3', select_file)
    keyboard.add_hotkey('f4', toggle)
    keyboard.wait('esc')
    print("\nProgram terminated.")