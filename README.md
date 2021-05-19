# The Collaborative Word List
coming soon ...

## Format

The dictionary is in the format below with no headers:

```
word;score
word;score
word;score
```

## Technical Details of this Repo

### Sorting the dictionary

After a push to any branch, the below script is run:

`./script/sort.py`

This script will:

* Ensure the list is the correct format (above)
* Ensure there are no duplicates
* Capitalize all words and remove trailing/leading spaces
* Run a quick test to make sure it's roughly the size expected (> 425,000 entries)

If the above checks fails, the action as a whole will fail and no auto-updates will be applied.

## Github Action Configuration

The code to run the github action is in `.github/workflows`. It runs and auto-fixes pushes to any branch, including `main`.
