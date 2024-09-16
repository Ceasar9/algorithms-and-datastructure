# algorithms-and-datastructure
Algorithms and Data-Structures in Python


## Requirements

1- Setup virtual environment:
 - create a virtual environment using `virtualenv`: 
 <br>`virtualenv --python=python3.xx venv`
 - activate the virtual environment. In linux OS: 
 <br>`source venv/bin/activate`

2- Install custom packages from git:
 - ### Method 1 (recommended):
    - add custom packages into dependecty file, e.g. `requirements-dist.txt` (if already not included). for example:
        - `-e git+ssh://git@github.com/Ceasar9/utils_general_alg.git@7f374b26685ac53d9f9ea84377a4f6e6be23aaf3#egg=utils_general_alg` 
        <br>(alternatives for 'ssh' would be using 'https' or 'git'):
        - `-e git+git://git.myproject.org/SomeProject#egg=SomeProject` or
        - `-e git+https://git.myproject.org/SomeProject#egg=SomeProject`
    - then, install all dependencies at once:
        - `pip install -r requirements-dist.txt`
 - ### Method 2 (manual): 
    - create a directory in your root project: 
    <br>`mkdir dist`
    - change directory to the already created `dist/` dirctory with `cd dist` and clone the custom packages. For example: 
    <br>`git clone git@github.com:Ceasar9/utils_general_alg.git`
    - install custom packages in the `dist/` (NOTE - make sure the virtual environment is activated): for example `pip install -e utils_general_alg/.` 
    <br>(NOTE: for private and protected repos may need to enter password.)
