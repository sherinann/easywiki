# easywiki

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6c54f548720e48cabf01792181e97860)](https://www.codacy.com/app/sherinannthomas1/easywiki?utm_source=github.com&utm_medium=referral&utm_content=sherinann/easywiki&utm_campaign=badger)

this is a python script to access information about any subject from wikipedia through command line

# Requirements
* python 3
* bs4

# How to install

* From pypy
```
    pip install easywiki
```

* From downloaded package
```
    pip install path/to/package
    eg.
        pip install download/easywiki.tar.gz
```

# How to set up.

* Download source:
```
    $ git clone https://github.com/sherinann/easywiki.git
```

* Install requirements
```
    $ pip3 install -r requirements.txt
```

Now to build the application

* Create a distribution
```
    $ python3 setup.py sdist 
```

* Go to the directory
```
    $ cd dist
```

* Install the package using pip3

    * example:
    ```
        $ pip3 install easywiki-1.0.0dev.tar.gz
    ```
