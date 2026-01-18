# Heartopia Auto Piano Player

An automated piano player for Heartopia game that reads note files and simulates keyboard inputs to play music automatically.

## Features

- 🎹 Automated piano playing with keyboard simulation
- ⚡ Adjustable tempo/speed control
- 📁 Multiple song file support
- 🎮 Hotkey controls (F3, F4, ESC)
- 📊 Real-time progress bar
- 🔄 Easy song switching without restart

## Requirements

- Python 3.6 or higher (recommend Python 3.10.11)
- Windows OS (uses pydirectinput for keyboard simulation)

## Where to Get Music Notes

You can purchase music note files from: **https://www.youtube.com/@dad_piano**

### Important Security Notice

⚠️ **Download on a secondary/backup computer first** - The zip files contain `.exe` files that may be flagged by antivirus software. Using a virtual machine (like VMware) for downloading is recommended.

### Steps to Install Notes:

1. Download the note files from the YouTube channel above
2. Extract the zip file on your secondary/backup computer or VM
3. Locate the `.mrc` files from the extracted folder
4. Copy the `.mrc` files to the `/note` folder on your main gaming computer
5. Rename the file extension from `.mrc` to `.txt`
6. The notes are now ready to use with the auto player!


## Installation (Step-by-Step for Beginners)

### Step 1: Install Python (If You Don't Have It)

1. Go to https://www.python.org/downloads/
2. Click the yellow "Download Python" button (recommend Python 3.10.11 or newer)
3. **IMPORTANT**: When installing, CHECK the box "Add Python to PATH" at the bottom
4. Click "Install Now"
5. Wait for installation to complete
6. Verify installation by opening Command Prompt and typing:
```bash
python --version
```
   You should see something like "Python 3.10.11"

### Step 2: Download This Program

1. Download this project as a ZIP file (click the green "Code" button → "Download ZIP")
2. Extract the ZIP file to a location you can easily find
   - Example: `D:\htp-piano-marco` or `C:\Users\YourName\Desktop\htp-piano-marco`
3. Remember this location, you'll need it later!

### Step 3: Install Required Libraries

1. Open File Explorer and navigate to your extracted project folder
2. In the folder address bar (at the top), click and type `cmd` then press Enter
   - This opens Command Prompt in your project folder
3. Type this command and press Enter:
```bash
pip install -r requirements.txt
```
4. Wait for the installation to complete (you'll see "Successfully installed...")

### Step 4: Create Note Folder

The program needs a folder called `note` to store your music files.

**Option A - Using Command Prompt:**
```bash
mkdir note
```

**Option B - Using Windows Explorer:**
1. Right-click in your project folder
2. Select "New" → "Folder"
3. Name it exactly: `note`

### Step 5: Add Your Music Files

1. Get your `.mrc` files (see "Where to Get Music Notes" section above)
2. Copy them to the `note` folder you just created
3. Rename each file extension from `.mrc` to `.txt`
   - Example: `song.mrc` → `song.txt`
   - To change file extensions, you may need to enable "File name extensions" in Windows Explorer (View tab)

## Usage (How to Play Music)

### Method 1: Simple Double-Click (Easiest)

If you're in your project folder:
1. Double-click `main.py` to run it
2. A window will open showing available songs
3. Type the number of the song you want (e.g., type `1` for the first song)
4. Press Enter

### Method 2: Using Command Prompt

1. Open Command Prompt **as Administrator** (right-click Command Prompt → "Run as administrator")
2. Navigate to your project folder:
```bash
cd /d D:\htp-piano-marco
```
   Replace `D:\htp-piano-marco` with your actual folder location

3. Run the program:
```bash
python main.py
```

4. Select a song by typing its number and pressing Enter

### Playing the Music

1. After selecting a song, open your Heartopia game
2. Make sure the game window is active (click on it)
3. Press **F4** to start playing
   - You have 3 seconds to switch to the game window after pressing F4
4. The program will automatically play the piano for you!

### Controls While Running

- **F3** - Open song selection menu (choose a different song)
- **F4** - Start playing / Stop playing (toggle)
- **ESC** - Close the program completely