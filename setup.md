## python lecture at KIS 2020

### Installation guide

For the purposes of this lecture, we will be using [Anaconda](https://www.anaconda.com/distribution/) for managing our python distribution and additional packages, [jupyter notebooks](https://jupyter.org/try) as our IDE and of course [python](https://www.python.org/) as our programming language.

## 1. Installing Anaconda
Should you already have Anaconda installed, skip to step 1.4.

### 1.1. Installation under Windows
- [Download the Anaconda installer](https://www.anaconda.com/distribution/#windows) (Python 3.7 version)
- Anaconda is about 3 GB, make sure there's enough disk space available
- Double click the installer to launch
- Click Next
- Read the licensing terms and click "I Agree"
- Select an install for "Just Me" and click Next
- Select a destination folder to install Anaconda and click Next, you can use the default (for example `C:\Users\<user>\anaconda3`)
- Check only "Register Anaconda3 as my default Python 3.7"
- Click the Install button
- Click Next
- Anaconda will ask you to install PyCharm, which is another IDE that we will not use. Click Next to skip
- If the installation was successful, click Finish
- Verify your installation by doing the following:
    - Click Start, search or select Anaconda Prompt from the menu
    - This will open a Terminal in a new window. Enter `conda list`
    - Enter `python`, wait until it is loaded and enter `quit()`
    - Type `jupyter notebook`, this will open a new tab in your browser, click quit in the upper right and close the tab
- If any of the above commands lead to errors, refer to step 1.5.

### 1.2. Installation under Linux
You may need to [install additional dependencies for Qt](https://docs.continuum.io/anaconda/install/linux/). This should not be necessary for jupyter notebooks, but may be needed for other IDEs and packages. Ignore this if you are unsure.

- [Download the Anaconda installer](https://www.anaconda.com/distribution/#linux) for Linux (Python 3.7 version)
- In a terminal enter `bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh`
- Hit Enter to view license terms, scroll to the bottom and enter "Yes"
- The default path of installation is `/home/<user>/anaconda3`. It is recommended to use this as your install location (but you may enter a different path at this point). Hit Enter.
- It is recommended to initialize Anaconda3 by typing "yes"
- Close the current terminal window and open a new one
- Run the command `conda config --set auto_activate_base False`
- Verify your installation by doing the following:
    - Enter `conda list`
    - Enter `python`, wait until it is loaded and enter `quit()`
    - Type `jupyter notebook`, this will open a new tab in your browser, click quit in the upper right and close the tab
- If any of the above commands lead to errors, refer to step 1.5.

### 1.3. Installation under macOS
- [Download the graphical Anaconda installer](https://www.anaconda.com/distribution/#macos) for macOS (Python 3.7 version)
- Double-click the downloaded file and click continue to start the installation
- Answer the prompts on the Introduction, Read Me, and License screens
- Click the Install button to install Anaconda in your `~/opt` directory (which is recommended, you can click the "Change Install Location" button to install in another location)
- On the Destination Select screen, select Install for me only
- Click Continue
- Anaconda will ask you to install PyCharm, which is another IDE that we will not use. Click Continue to skip
- If the installation was successful, click Close
- Verify your installation by doing the following:
    - Hit Cmd+Space, type "Anaconda Prompt" and and start the program
    - This will open a Terminal in a new window. Enter `conda list`
    - Enter `python`, wait until it is loaded and enter `quit()`
    - Type `jupyter notebook`, this will open a new tab in your browser, click quit in the upper right and close the tab
- If any of the above commands lead to errors, refer to step 1.5.

### 1.4. Updating an existing version of Anaconda
Windows: Open the Start Menu and choose Anaconda Prompt

Linux and macOS: Open a terminal window
- type the following two commands:
```bash
conda update conda
```

### 1.5. Troubleshoot
- Refer to https://docs.continuum.io/anaconda/user-guide/troubleshooting/
- If that does not help: Contact me (waidele@leibniz-kis.de), or Carl (schaffer@leibniz-kis.de) or Saida (smdiazcas@leibniz-kis.de)

## 2. Downloading the lecture repository
All of the material for the lecture will be located in my [GitHub-repository](https://github.com/mwaidele/python_lecture_KIS2020). Although it can be easily viewed and accessed there, it is more convenient to download the whole repository on your local device. Note that content in this repository will change over time.

### 2.1. Downloading via Browser
- [Download my GitHub repo](https://github.com/mwaidele/python_lecture_KIS2020/zipball/master)
- Click "Save File"
- Move the downloaded file (should be in your `Downloads/` directory) into any folder you would like to store the lecture material
- Extract all files (double click the .zip file)
- After extraction, rename the folder that was created to `python_lecture_KIS2020`

### 2.2. Downloading via `git`
If you have `git` installed, you can clone the repository. This is only available for Linux and macOS users.
- Make a new directory for the lecture material (for example `~/lectures`)
- In a terminal window, type `git clone https://github.com/mwaidele/python_lecture_KIS2020.git`

## 3. Setup the lecture environment
In order to make sure we are all using the same packages and versions, a virtual environment, specifically for this lecture can be installed.

Windows: Open the Start Menu and choose Anaconda Prompt

Linux and macOS: Open a terminal window

- Navigate your directory to the lecture material via 
```bash
cd <your_dir>/python_lecture_KIS2020
```
where `<your_dir>` is the folder in which you extracted the .zip file (or cloned the repo into via `git`)

- Type the following command
```bash
conda env create -f pyKIS.yml
```
- The installation will take about 3 minutes
- Type 
```bash
conda activate pyKIS
ipython kernel install --user --name=pyKIS
jupyter notebook
```
- Click "Quit" in the upper right in the browser tab that just opened
- Type `conda deactivate pyKIS`

You should be all set up and ready for the lecture now. If you have any issues, please feel free to contact me (waidele@leibniz-kis.de), Carl (schaffer@leibniz-kis.de) or Saida (smdiazcas@leibniz-kis.de)
