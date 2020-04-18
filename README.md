# GUI

## Creae standalone OSX application with py2app

### Create a setup.py file, ignore it when there's already this file

```shell
$ py2applet --make-setup src/tkinter_stopwatch.py --iconfile images/stopwatch.png
Wrote setup.py
```

### Clean up your build directories and Building for deployment

```shell
rm -rf build dist && python3 setup.py py2app
```

### References

[py2app - Create standalone Mac OS X applications with Python](https://py2app.readthedocs.io/en/latest/index.html)

## Useful command line

* Delete all `pycache` directory

```shell
find . -type d -name __pycache__ -exec rm -r {} +
```
