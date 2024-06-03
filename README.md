# simpleCI
A simple local continuous integration (CI) system, that runs against a git repository.

# How it works
This project strips down a CI system to its core basic components, which in this case are:
- a repository **observer** that watches a repo for any changes.
- a **dispatcher** that recieves notifications about changes in the repo from the observer, then assigns the commits to a test runner.
- a **test runner** which runs tests against a given commit/change to the codebase.

The components each run as a separate independent process and communicate through sockets in order to mimic a distributed/networked system. It also runs locally 

# How to run the CI
## Setup
To work, the CI requires a repo to check against. Create a folder and start a local git repository in it.

`mkdir demo_repo`
`git init`

demo_repo serves as a main repository from which the CI pulls, checks for commits and runs tests.
update demo_repo by copying the tests/ folder from this codebase into it then commit the change:

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

observer.py will register the new commit and notify the dispatcher. The output can be seen in the respective shells. Once the dispatcher receives the test results, it stores them in a test_results/ folder in the project's code base, using the commit id as the file name.
