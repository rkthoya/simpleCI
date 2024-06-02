# simpleCI
A simple distributed continuous integration system, that runs against a local git repository.

# How it works
The CI system involves 3 main components: an observer a dispatcher and a test runner.
The observer checks a repository for any changes (commits), and notifies the dispatcher upon a change.
The dispatcher then dispatches a test runner against the specific commit.

# How to run the CI
## Setup
To work, the CI requires a repo to check against. Create a folder and start a local git repository in it.

`mkdir demo_repo`
`git init`

demo_repo serves as a main repository from which the CI pulls, check for commits and runs tests.
The observer.py module does the checking for new changes. We need at least one commit in the main repo, and for this we can use the example tests in the our project repo.

Copy the tests/ folder from the code base to demo_repo and then make a commit:

`git add tests/`
`git commit -m "add tests"`

observer.py will needs its own copy of the code to check for changes from the main repo. Back in the project codebase: 

`git clone /path/to/demo_repo demo_repo_observer_clone`

The same goes for test_runner which needs a clone to checkout the commit it needs to test.

`git clone /path/to/demo_repo demo_repo_runner_clone`

## Running the code
Start the dispatcher module first (it defaults to running on port 8888):

`python dispatcher.py`

Then start the test runner in new shell, so it registers itself with the dispatcher:

`python test_runner.py <path/to/demo_repo_runner_clone>`

Finally, start the observer in yet another new shell:

`python observer.py --dispatcher-server=localhost:8888 <path/to/demo_repo_observer_clone>`

Trigger some tests by making a new commit in the main repo:

`cd /path/to/demo_repo`
`touch new_file`
`git add new_file`
`git commit -m "new file" new_file`

observer.py will rregister the new commit and notify the dispatcher. The output can be seen in the respective shells. Once the dispatcher receives the test results, it stores them in a test_results/ folder in the project's code base, using the commit id as the file name.
