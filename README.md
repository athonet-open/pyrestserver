## How to build

```
python setup.py sdist
```
take the .tar.gz pip inside `dist/` folder 

## How to install and run

```
pip install pyrestserver-1.0.0.tar.gz
```
at least `python 3.6` is required. You can install it inside a virtualenv

You can run server using binary `py-rest-server`



## How to test

`http --check-status PUT http://127.0.0.1:8080/data msg=Hello`

`http --check-status GET http://127.0.0.1:8080/data`