# Simple Tools
## 1. File Organizer
This tool is used to organize files by grouping them into folders based on their format type or extension.
### How to Use on Windows
1. Run the `fileOrganizer.bat` file.
2. Enter the folder path you want to organize, then press **Enter**. 
   If you want to organize the folder where this application is located, just press **Enter**.

### How to Use on Linux
1. Open the Terminal application.
2. Run the following command:
   ```bash
   python3 fileOrganizer.py
   ```
   Or also with:
   ```bash
   ./fileOrganizer.sh
   ```
3. Enter the folder path you want to organize, then press **Enter** (or just press **Enter** for the current folder).

### How to Use on Android
1. Open a terminal application (such as Termux).
2. Run the following command:
   ```sh
   sh fileOrganizer.sh
   ```

---

## 2. Image to SVG Converter (Image to SVG)
This tool converts all images (.png, .jpg, .jpeg) in the folder into SVG format.
*Note: Make sure Python and OpenCV are installed on your computer or device. You can install OpenCV by typing the command `pip install opencv-python` in Terminal or Command Prompt.*
### How to Use (Windows and Linux)
1. Open Terminal or Command Prompt.
2. Run the following command:
   ```bash
   python imgToSvg.py
   ```
3. The program will look for images. Type `y` then press **Enter** to approve the image conversion and delete the old image files.
