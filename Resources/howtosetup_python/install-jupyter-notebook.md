

## Getting Started With Python

Installing Jupyter Notebook in Windows 11 is a straightforward process. First, you’ll need to install Python, then use pip to install Jupyter Notebook. Once that’s done, you can launch Jupyter Notebook and start working on your projects. [Read Source](https://www.solveyourtech.com/how-to-install-jupyter-notebook-in-windows-11-a-step-by-step-guide/)

| STEPS                       | COMMANDS                                                    |
| --------------------------- | ----------------------------------------------------------- |
| Search for Python Package   | `winget search python`                                    |
| Download the Latest Package | `winget install --id Python.Python.3.12 --source winget` |
| Upgrade Pip                 | `python.exe -m pip install --upgrade pip`                 |
| Install Jupyter Notebook    | `pip install notebook`                                    |
| Launch Jupyter Notebook     | `jupyter notebook`                                        |

### Step 1: Install Python

First, download Python from the official Python website and run the installer.

Or Simply Open Command Prompt ( Terminal ) run the below Command

```powershell
`winget install --id Python.Python.3.12 --source winget`
```

> Note

```
When you install Python, make sure to check the box that says “Add Python to PATH.” This step is crucial because it allows you to run Python and pip commands from the command line without additional configuration.
```

### Step 3: Install pip and Upgrade

verify if pip is already installed by typing `pip --version` . If not, install it by typing `python -m ensurepip --upgrade`.


| FOLLOW THESE STEPS         | COMMAND                                     |
| -------------------------- | ------------------------------------------- |
| Verify If PIP is Installed | `pip --version`                           |
| Install Python PIP         | ``python -m ensurepip --upgrade``           |
| Upgrad PIP If Needed       | `python.exe -m pip install --upgrade pip` |

>  Note 
>
> Pip is the package installer for Python, and it’s what you’ll use to install Jupyter Notebook. If pip is already installed, you can skip this step.


### Step 4 : Install Jupyter Notebook

Below command will install Jupyter Notebook using pip.

| FOLLOW THESE STEPS       | col2                     | col3 |
| ------------------------ | ------------------------ | ---- |
| install jupyter notebook | `pip install notebook` |      |
| Launch Jupyter Notebook  | `jupyter notebook`     |      |
