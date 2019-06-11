# Lead Auto Loader

The program needs to be written to be run with Powershell.

Powershell has Python 3 and 2 installed.

We will have to have 2.7.9 installed which has pip installed by default.

To run a program with Python 2 use:

    py -2 test.py

To run pip with that specific version of python use:

    py -2 -m pip

We are going to be using a cross platform (Windows and UNIX) file locking system called portalocker.

To install portalocker with powershell and pip firstly pip needs to be upgraded.

Use this command to upgrade pip:

    py -2 -m pip install -U pip

Now pip is updated.

To install portalocker run this command:

    py -2 -m pip install portalocker