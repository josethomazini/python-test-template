# Python-Test-Template

This is a template for a python project with pytest and coverage enabled.

## Developer

```
Using Ubuntu 19.10, Python 3.7, PIP, virtualenv-wrapper and VSCode.
```

### Download this repo:

```
cd ~/Documents/projects
git clone git@github.com:josethomazini/python-test-template.git
```

### Create a virtualenv for the project:

```
mkvirtualenv python-test-template
```

### Add an auto-change folder whenever accessing the virtualenv:

```
cdvirtualenv
echo 'cd ~/Documents/projects/python-test-template' >> bin/postactivate
```

### Test it:

```
workon python-test-template
```

### Install the developer's requirements:

```
pip install -r requirements/dev.txt
```

### Open it in VSCode:

```
code .
```

### Save it into a new workspace:

```
File > Save Workspace as > ~/Documents/workspaces/python-test-template.code-workspace
```

### Add the virtualenv as the workspace's python path:

- CTRL + SHIFT + p
- Python: Select Interpreter
- Choose the virtualenv of python-test-template

Now, whenever you open the VSCode integrated terminal it will start the virtualenv.

### Run all the tests at once using the integrated terminal:

Ensure the virtualenv is activated.

```
scripts/run_tests.sh
```

### Start the watcher to run all the tests whenever you save a python file:

Ensure the virtualenv is activated.

```
scripts/watcher.sh
```

### Coverage Report

After running the tests you may want to generate the coverage reports. The folder will be created inside the repo. It can help you understand which workflows need to be tested.

```
coverage html
```

---

# Modify this template as you wish. Happy coding!
