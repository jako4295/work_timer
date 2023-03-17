# Work Timer
As of now this app is **only tested on Ubuntu 20.04**, but should work on later versions of Ubuntu as well.

Feel free to contact the authors:
1. [Jakob Olsen](https://github.com/jako4295)
2. [Jacob Mørk](https://github.com/Jacob-EWE)
3. [Anders Lauridsen](https://github.com/ahll19)

# Table of contents
- [Work Timer](#work-timer)
- [Table of contents](#table-of-contents)
- [1. Installation Guide](#1-installation-guide)
  - [1.1. Dependencies](#11-dependencies)
    - [Python](#python)
  - [1.2. Cloning](#12-cloning)
  - [1.3. Installing](#13-installing)
- [2. User Guide](#2-user-guide)
- [3. Uninstalling](#3-uninstalling)
  - [3.1. Bash Aliases](#31-bash-aliases)
  - [3.2. Desktop Entry](#32-desktop-entry)
  - [3.3. Git repository](#33-git-repository)
- [4. Roadmap](#4-roadmap)


# 1. Installation Guide
## 1.1. Dependencies
### Python
This tool depends on python for both installation, and running the app. The dependencies are
1. `python3-venv`
2. `python3-tk`
3. `python3-pip`
4. `build-essential` 
5. `libssl-dev`
6. `libffi-dev`
7. `python3-dev`
8. `git`

To install these dependencies run the following commands
```
sudo apt update && sudo apt upgrade -y
```
```
sudo apt install python3-venv python3-tk python3-pip build-essential libssl-dev libffi-dev python3-dev git -y
```

## 1.2. Cloning
To clone the repository move to a folder where you want the app to live. In this example we'll create a folder called `.Programs` in the home directory of the logged in user.

1. Open a terminal
2. Run <br>`mkdir .Programs && cd .Programs`
3. Clone the repository with <br>`git clone https://github.com/jako4295/work_timer.git`
4. Go into the directory <br>`cd work_timer`
5. Run the installer <br>`python3 install.py`

## 1.3. Installing
Each installation is user specific, and will only work for the user which installs the app.

The installer script will prompt you for a directory, where it will store the logs of your timers. The prompt will always use the currently logged in user's home directory as a start. As an example you can just write `work timers`, and the installer will create a directory in your home folder called `work timers`, where timers will be stored.

After the script has run a `config.ini` file will be created in the git repository directory, where you can change the folder location. This is not recommended however. We recommend re-installing the app, as of now, and saving your currently held logs in another directory. Moving the location of the git repository will also break the app.

A `timer` alias will be created in your `.bash_aliases` file in your home directory. Running this command in a new terminal will launch the app, with the possibility of debugging the app in the currently opened terminal. A desktop entry will also be created in your `~/.local/share/applications` directory, which can also be edited in order to change the name of the app, or the icon.

# 2. User Guide
To use the app simply launch it, and press **start working** or **stop working** when you start or stop working, respectively. When you want to create a timesheet to save your worked hours simple press the **Create Timesheet**, and a timesheet will be saved in the directory which you specified during the install.

# 3. Uninstalling
## 3.1. Bash Aliases
In your home directory edit your `.bash_aliases` file, and remove the line which starts with `alias timer="bash..."`. This will stop your shell from calling the `run` script in your git repo.

## 3.2. Desktop Entry
Delete the Work timer `.desktop` file in your `.local/share/applications` directory in your home directory. This will remove Work Timer from your app menu.

## 3.3. Git repository
Remove the git repository from where you cloned it in the first place.

# 4. Roadmap
- [ ] Create a settings menu
  - [ ] Allow users to specifiy output format
  - [ ] Allow theme changes
  - [ ] Change timer logs directory
- [ ] Generalize install script to handle dependencies
- [ ] Add support for other Linux distributions
- [ ] Add Live timer to the GUI
- [ ] Archiving Support
- [ ] Select which months to create convert to timesheet
- [ ] Edit time logs
  - [ ] Potentially add a calander to the GUI

- [x] Create a MVP working GUI