# The Collaborative Word List
coming soon ...

## Contributing

1. Clone the repo locally
2. Checkout a new branch: `git checkout -b arbitrary-branch-name`
3. Make your changes to `xwordlist.dict`
4. Add and commit your changes `git commit -am "Description of your changes"`
5. Push your changes to a remote branch `git push -u origin arbitrary-branch-name`
6. Open the link in your terminal to open a new pull request with your changes in a browser
7. Once status checks pass, press the green `Merge Pull Request` button in the pull request
8. If checks fail, click through the red X's to see what the errors were

### Status Checks

After a push to any branch (including `main`), an automatic trigger will run the following on any changes:

* Ensure the list is the correct format (above)
* Ensure there are no duplicates
* Capitalize all words and remove trailing/leading spaces
* Sort the list by score descending, and then alphabetically within a given score
* Run a quick test to make sure it's roughly the size expected (> 425,000 entries)

If the above checks fails, the action as a whole will fail and the changes can't be merged.

## Format

The dictionary is in the format below with no headers:

```
word;score
word;score
word;score
```

## Technical Details of this Repo

### Sorting the dictionary

This script is run by the github action: `./script/sort.py`

### Github Action Configuration

The code to run the github action is in `.github/workflows`
