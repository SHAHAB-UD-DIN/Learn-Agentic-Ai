## Step 1: Install Python
Ensure you have Python installed (version 3.8 or later). Download it from the official site if needed:
- [Download Python](https://www.python.org/downloads/)
- Check installation by running in Command Prompt (CMD):
```python
python --version
```
## Step 2: Install `uv` via PowerShell
Open PowerShell and run:
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```
It looks like you've successfully installed `uv` on your Windows system. The installation path is C:\Users\eshop\.local\bin, and the final step is to add this path to your system's environment variables so that you can run uv from anywhere in the command line

## Using the GUI (Graphical User Interface)
#### Step 1: Open Environment Variables
- Press `Win + s`, type `advanced system settings`, and press **Enter**.
- Click the "Environment Variables..." button at the bottom.
- In **System variables**, find the `Path` variable.
- Select `Path` and click **Edit**...

#### Step 2: Add the New Path
- Click **New** and add the following path:
```bash
C:\Users\kh\.local\bin
```
- Click **OK** to close all windows.

## Step 3: Restart the Terminal
After adding the path, restart **Command Prompt** or **PowerShell**, then type:
```bash
uv --version
```
If it displays the version, the installation was successful.

# Download Visual Studio Build Tools
1. Open your browser and go to the official Microsoft download page:
[Download Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)

2. Click the **Download Build Tools** button to get the latest installer (`vs_BuildTools.exe`)

#### Step 1: Run the Installer
1. Locate the downloaded `vs_BuildTools.exe` in your **Downloads folder**.
2. Double-click to run the installer.
3. When prompted, choose **"Continue"** to proceed with the installation.

#### Step 2: Select Workloads
In the installer window, you'll see various workloads. Select the following based on your needs:
1. Check **"Desktop development with c++"**.
2. Click the **"Install"** button.
3. Wait for the installation to complete (this may take some time depending on your internet speed).

# upgrade pip
A new release of pip is available
 To update, run:
```bash
python.exe -m pip install --upgrade pip
```

# Installing CrewAI
#### Python Version Requirements
CrewAI requires `Python >=3.10 and <3.13`. Here’s how to check your version:
```python
python --version
```
#### Installation
CrewAI is a flexible and powerful AI framework that enables you to create and manage AI agents, tools, and tasks efficiently. Let’s get you set up! 🚀
1. Install CrewAI
Install CrewAI with all recommended tools using either method:
```crewai
pip install 'crewai[tools]'
```
or
```crewai
pip install crewai crewai-tools
```
2. Upgrade CrewAI
If you have an older version of CrewAI installed, you can upgrade it:
```crewai
pip install --upgrade crewai crewai-tools
```
