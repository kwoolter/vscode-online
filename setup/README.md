# Get the environment ready
## Install Python
Go to the 'Extensions' search (Ctrl+Shift+x)
Search for 'Python' and install

## Installing pip

Get the intstaller by running this in a terminal...
- `mkdir setup`
- `cd setup`
- `curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py`

Open a terminal and :

- `cd setup`
- `python3 get-pip.py --user`

To upgrade:
- `python3 -m pip install -U pip --user`
- `python3.8 -m pip install -U pip --user`


OR use other versions of python as per section below

## Call python from terminal
Once you open a terminal there are a few options:
- `python` - python2.7
- `python3` - python 3.5.4
- `python3.8` - python 3.8

## Installing packages
`pandas` installs various useful python packages:
`python3 -m pip install pandas --user`

Other useful packages:
`colorama`
`readline` - got an error installing this :(

## VSCODE settings
In the `.vscode` directory of the workspace edit the `settings.json` file so that your preferred version of python is picked by default:
`
{
    "python.pythonPath": "/opt/python/latest/bin/python3.8"
}
`

NB: I can't remember how this directory and file were created

## Connecting you workspace to GitHub

- Create a new repo on gitHub e.g. `new_repo_name`
- From VS online terminal run:
`git remote add origin https://github.com/kwoolter/new_repo_name.git`

This will add the remote which should appear in the `settings.json` file

    "githubPullRequests.remotes": [
        "origin",
        "upstream",
        "https://github.com/kwoolter/vscode-online.git"
    ]
