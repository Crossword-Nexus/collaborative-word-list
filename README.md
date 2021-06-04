# The Collaborative Word List

The collaborative word list is a scored word list for crossword constructors.  Help us make it the best possible list by joining and contributing your words and scores.

## Contributing

If you'd like to contribute, please e-mail us (crosswordnexus@gmail.com) with a request to be added as a contributor to the repository.

The best way to get started is to watch this YouTube video which should teach you everything you need to know.
https://www.youtube.com/watch?v=n0py3nm4itI

### Using GitHub Desktop
1. Clone the repo locally.  The easiest is to choose "clone by URL" and using this URL.
2. Create a new branch.  It can really be named anything, but the easiest is to use your name.
3. Make your changes to the word list.
4. Commit your changes to the branch.  Add a little note if you'd like to let us know what you've changed.
5. Click the "Push Origin" button to push your changes to the remote branch.
6. Click the "Create Pull Request" button to open a browser window with the new pull request.
7. Click the green button to merge the pull request.

Once the initial steps are done, you can either keep your branch open or make a new branch every time.  If the latter, you'll have to update from main every time before you start making changes to your list, or you risk having tons of conflicts that will be impossible to resolve.

### Using the GitHub command line interface

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

* Ensure the list is the correct format (below)
* Ensure there are no duplicates
* Capitalize all words and remove trailing/leading spaces
* Sort the list alphabetically
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
