========================================================================
🚀 SAP ABAP Deep Structure Generator (Python Tool)
========================================================================

This tool analyzes complex JSON data and automatically generates the necessary ABAP code for:
1. Deep Structure (TYPES) definitions,
2. The /ui2/cl_json=>deserialize method logic,
3. Automatic Mapping Tables (handling the 30-character limit and special characters).

It provides a ready-to-use ABAP solution for parsing nested JSON structures.

------------------------------------------------------------------------
📂 FOLDER CONTENTS
------------------------------------------------------------------------
Ensure the following 3 files are present in this folder:
1. app.py              (Interface/GUI Code)
2. json_to_abap.py     (Core Logic/Parser Code)
3. requirements.txt    (Library dependencies list)

------------------------------------------------------------------------
🛠️ STEP 1: PREREQUISITES
------------------------------------------------------------------------
If Python is not installed on your machine:

1. Go to https://www.python.org/downloads/
2. Click "Download Python" and run the installer.
⚠️ CRITICAL STEP: At the bottom of the installation window, ensure you check the box that says "Add Python to PATH".
   If you miss this, the commands will not work.
3. Click "Install Now" to finish.

(Visual Studio Code is recommended for viewing the code, but not required to run it.)

------------------------------------------------------------------------
⚙️ STEP 2: INSTALLING LIBRARIES (First time only)
------------------------------------------------------------------------
This tool requires the "Streamlit" library to run.

1. Open this folder in your File Explorer.
2. Type "cmd" in the address bar (where the folder path is) and press Enter.
   (This will open a black Command Prompt window).
3. Paste the following command and press Enter:

   pip install -r requirements.txt

   (Wait for the installation to complete. Once you see "Successfully installed...", you can close the window.)

------------------------------------------------------------------------
▶️ STEP 3: RUNNING THE APPLICATION
------------------------------------------------------------------------
Whenever you want to use the tool:

1. Open the Command Prompt (cmd) in this folder again (or use the VS Code terminal).
2. Type the following command and press Enter:

   python -m streamlit run app.py

3. Your default web browser will open automatically with the application.
   Paste your JSON on the left side, and copy the generated ABAP code from the right side.

------------------------------------------------------------------------
❓ TROUBLESHOOTING
------------------------------------------------------------------------
Q: I get a "'pip' or 'python' is not recognized" error.
A: You likely forgot to check "Add to PATH" during Python installation. Uninstall Python and reinstall it, ensuring that box is checked.

Q: The requirements.txt file is missing or failing.
A: No problem. You can install the library manually by running:
   pip install streamlit

Happy Coding! 🐍 -> ABAP