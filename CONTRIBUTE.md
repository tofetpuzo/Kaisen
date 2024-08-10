### To contribute to this project

1. First [fork this repository](https://github.com/tofetpuzo/Kaisen). (If you are or intend to be a collaborator, uncheck "fork only master", because for versioned docs you'll need gh-pages branch too.) Clone it to your system and install the development dependencies.

### clone repository

$ git clone "https://github.com/tofetpuzo/Kaisen"

# change directory

$ cd Kaisen

### install development dependencies

$ poetry install

1. create a new branch locally
   `git checkout -b "your_preferred_branch_name"` follow this convention

2. create an python-env using this command
   `python -m venv /path/to/new/virtual/environment`
   In window use `c:\>python -m venv c:\path\to\myenv`
   On mac use `source venv/bin/activate`

3. Make sure any code written a test is added and passes locally
   you can use this command `pytests .`

4. After all done create a new [Pull request](https://github.com/tofetpuzo/Kaisen/pulls)
