watchmedo shell-command \
 --patterns="*.py" \
 --recursive \
 --command='clear && pytest -n 3 --cov sources' \
 .
