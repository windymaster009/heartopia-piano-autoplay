# Heartopia Auto Piano Player

Automate piano playing in the Heartopia game! This tool reads note files and simulates keyboard inputs, letting you play songs automatically without manual key presses.

---

## 🎵 Key Features

- Automatic piano performance using keyboard simulation  
- Adjustable `tempo/speed` settings  
- Supports multiple song files  
- Hotkey controls for easy operation `(F3, F4, ESC)`  
- Real-time progress bar to track playback  
- Quickly switch songs without restarting the program  

---

## ⚙️ Requirements

- **Python** `3.6` or higher (recommended: `3.10.11`)  
- **Windows OS** (relies on `pydirectinput` for keyboard simulation)  

---

## 🎼 Getting Music Notes

You can get song note files from anywebsite just download a MIDI file, `make sure it Piano` and convert it ask txt use `convert.py`

## 🛠️ Installation Guide
### Step 1: Download the Project

1. Download this project as a ZIP (`Code → Download ZIP`)  
2. Extract it to a convenient location, e.g.:  
   `C:\\Users\\YourName\\Desktop\\htp-piano`  
3. Remember this folder location—it will be used later  

---

### Step 2: Install Dependencies

1. Open Command Prompt in the project folder:  
   - Navigate to the folder or type the path in Explorer and type `cmd` in the address bar  
2. Install required Python packages:

\`\`\`bash
pip install -r requirements.txt
\`\`\`

---

### Step 3: Create a Note Folder

The program needs a folder named `note` to store music files.

- **Option 1 (Command Prompt):**

\`\`\`bash
mkdir note
\`\`\`

- **Option 2 (Windows Explorer):**  
  Right-click → New → Folder → Name it `note`  

---

### Step 4: Add Your Music Files

1. Copy your downloaded `.mid` files to the `project` folder
2. convert `.mid` using convert.py to `txt`
3. run `main.py` after converted  

> Tip: Enable **“File name extensions”** in Windows Explorer to rename file types easily  

---

## ▶️ How to Use the Player

### Method 1: Double-Click (Quick Start)

1. Open your project folder  
2. Double-click `main.py` to run  
3. Type the number of the song you want to play and press Enter  

### Method 2: Command Prompt

1. Open Command Prompt as Administrator  
2. Navigate to your project folder, e.g.:

\`\`\`bash
cd /d C:\\Users\\YourName\\Desktop\\htp-piano
\`\`\`

3. Run the program:

\`\`\`bash
python main.py
\`\`\`

4. Select your song by typing its number and pressing Enter  

---

### Playing Music

1. Open the Heartopia game and ensure the game window is active  
2. Press **F4** to start playing  
   - You have **3 seconds** to switch to the game window after pressing F4  
3. The program will automatically play the song for you  

---

### 🎮 Hotkeys During Playback

- **F3** – Open song selection menu  
- **F4** – Start / Stop playback (toggle)  
- **ESC** – Exit the program completely  
"""
