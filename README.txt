# Thea

## About
TODO

## User Guide
TODO

## Developer Setup

### Get the Code
The code lives on GitHub, so let's clone it from there.
```
cd path/to/project
git clone git@github.com:mikewalker92/theaV2.git
```
TODO - update this to point at the main thea repo once it's merged in.

### Install Dependencies
Thea has a few dependencies, which we will need to install before getting started.
- python3
- [Iris](http://scitools.org.uk/iris/)
- [PyQt5](http://pyqt.sourceforge.net/Docs/PyQt5/)
TODO - provide a full list here.

I suggest using Conda (or MiniConda) to manage the dependencies, as it makes it very simple to install Iris, allows you
keep an isolated dev environment and integrates nicely with PyCharm.

Let's start by installing MiniConda. Download the installer from [here](https://conda.io/miniconda.html), and then
follow [these](https://conda.io/docs/install/quick.html) instructions for whatever OS you have.

Now lets create a new virtual environment to install everything into. We'll use python3, and name the environment
'thea'
```conda create --name thea python=3```

Next lets activate our new environment.
```source activate thea```

We are ready to start installing our dependencies.
```
conda install -c conda-forge iris
pip install pyqt5
pip install matplotlib
pip install mockito
pip install numpy
```
TODO - find a way to automate all of this.

### Start the Application
I highly recommend PyCharm, as it's fast, gives intelligent code completion, navigation, easy debugging, test running etc. It's not
a requirement for the project, but I'll be assuming that you have it for the rest of the README.

- install [PyCharm](https://www.jetbrains.com/pycharm/download/) (the community
edition will do just fine if you don't have access to Ultimate)
- Open the project. (PyCharm should automatically sort everything out for you)
- Double check that PyCharm has picked up on your conda environment. Go to Preferences -> Project -> Project Interpreter
and make sure it is pointing at the python version from your conda environment.
- Run ```main.py``` (right click on the 'main.py' file, then click 'run')
- The Application should start up in a new window.

### Run the Tests
In PyCharm, all tests can be run by right clicking the 'tests' directory, and then clicking 'Run'.

## Code Structure
TODO

## Troubleshooting
TODO