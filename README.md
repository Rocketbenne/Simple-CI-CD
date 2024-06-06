# Simple CI/CD-Setup

This is a simple Project, which should help set up a simple CI/CD-System that creates a workflow, which can install dependencies, run tests, check for errors and more with a single version of Python.

### Step 1
---

Create a Project on GitHub.

### Step 2
---

Create and apply an access token in GitHub. 

This is optional and only required if the access to the pipeline should be limited, so that not everyone can modify the pipeline.

This is needed if the pipeline should be able to commit and push to the repository as GitHub Actions else does not have the possibility of changing repository-content. 

If this is not needed for your project, skip to **Step 3**

- To create an access token first click on your profile photo, then on **Settings**. 

- In the sidebar click on **<> Developer settings**.

- Again in the left sidebar click on **Personal access token**. 

- From the drop-down menu choose the option **Tokens (classic)**.

- Now click on **Generate new token** and give it a name. Choose your desired Expiration date of the token and under **Select scopes** choose **workflow**. At the bottom of the page click on **Generate token**. Then copy the new token to your clipboard.

- Now that we have created the access token, we need to apply it to the project.

- Move to you repository and click on the **Settings** tab.

- In the left Sidebar click on **Secrets and variables** and select **Actions** from the drop-down menu.

- Click on **New repository secret**, enter a name for the secret and paste the access token in the **Secret** field.

### Step 3
---

Set up GitHub Actions.

This step creates a basic workflow in the project with a short and simple yml-file
to control and set up the workflow.

- In GitHub move to your Project

- Select the **Actions** Tab

- Search for **Python application** and click on **configure**. This opens up the 
standart yml-file, which controls the workflow of the Pipeline. 

- To save the file and create the first instance of this workflow-program click on
**Commit changes** in the top right corner.

The following steps can be done in GitHub or locally and then pushed onto GitHub.

### Step 4
---

Set up the yml-file to specify the workflow and test your code.

In the following the automatically created yml-file is described and expanded.

- Set actions on which the workflow starts.
```
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]
```
For push and pull-requests on the branch main the workflow activates.

- Choose permissions for actions in the repository.
```
permissions:
  contents: write
```
The permission for contents allowes the Pipeline to either do nothing, read or write to files in the repository. In our case we change the permission from read to write as we later want to change the contents of a csv-file. 

- Create the different steps of the Pipeline.
```
- name: Checkout code
  uses: actions/checkout@v4
```
This clones the repository onto the virtual machine, which runs the workflow.

```
- name: Verify directory contents
  run: ls -la
```
This lists the contents of the directory in the virtual machine. We can use this as a debugging tool and to confirm that all the files and directories available on the virtual machine.

```
- name: Set up Python 3.10
  uses: actions/setup-python@v3
  with:
    python-version: "3.10"
```
Python gets set up on the virtual machine. It is also possible to set up more versions of Python here so that the program can be tested for multiple Python-versions.

```
- name: Install dependencies
  run: |
  python -m pip install --upgrade pip
  pip install flake8 pytest numpy matplotlib
  if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
```
This step installes all the needed dependencies. Using Python we install pip and using pip we can install all needed dependencies for our program. 

Flake is used to detect Python syntax errors and other errors. Pytest is later used to test the output of our program. 

In our case the needed dependencies for the program (numpy, matplotlib) were added manually. This process can also be done in a file called 'requirements.txt'.

```
- name: execute py script
  run: python test.py
```
This step simply runs the program named 'test.py'.
```
- name: Check for changes
  run: |
    if git diff --quiet --exit-code; then
      echo "No changes detected in the repository. Skipping commit."
      exit 0
    else
      echo "Changes detected in the repository. Proceeding with commit."
      exit 1
    fi
  id: check_changes
  continue-on-error: true
```
The next section of the code checks if there were made any changes to the repository, if any files were written to or created. If so, it sets a variable which will later be used when setting up commits.

```
- name: Configure Git
  run: |
    git config --global user.name 'github-actions[bot]'
    git config --global user.email 'github-actions[bot]@users.noreply.github.com'
```
This sets up a user to commit and push changes.

```
- name: Commit and push changes
  if: steps.check_changes.outcome == 'failure'
  env:
    CI_CD_SECRET: ${{ secrets.CI_CD_SECRET }}
  run: |
    git add Test-Program.png Test_Program.csv
    git commit -m "Autmatic commit: Add genereated csv and jpg files"
    git push https://${CI_CD_SECRET}@github.com/${{ github.repository }} HEAD:${{ github.ref }}
```

Using the secret created before, we can let the workflow do the standart add, commit and push procedure to upload all changed files. This will only be done if any files have been changed using the variable from before. 

If the pipeline pushed to the repository we need to pull the repository locally afterwards as we no longer have the latest version of the repository.

```
- name: Lint with flake8
  run: |
    # stop the build if there are Python syntax errors or undefined names
    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
    # exit-zero treats all errors as warnings. The GitHub editor is 127 chars wide
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
```
Using the installed dependency 'Flake' we check if there are Python syntax errors in the repository. 

```
- name: Test with pytest
  run: |
    pytest
```
This starts the program used for testing.

For this to work we now need to write a program which includes the tests.

### Step 5
---

Now we want to implement the file which tests the program. 

- First we create a new folder called **tests**.

- In this folder we create a python script beginning with **test_**, in our case we name it **test_compare_csv.py**.

- We also create a csv file, which contains the correct output of our program.

- We include the **pytest** library to be able to mark this file as our pytest-script.

- In our case we also include the **csv** library to be able to work with csv-files. Then we write a function to read the csv_file.

- The testing of the programm comes now. By defining both paths to the reference and the output of our program we can read out both of these csv-files. 

- The assert statement throws an error if the statement made is not correct. In our case if the contetns of the csv-files differ, an error gets thrown and the test is not succesful. This also automatically describes the type of error which lead to the difference.

- Lastly we define this script as our main pytest-script using this piece of code:
```
if __name__ == '__main__':
  pytest.main()
```

- Now everything should be set up and ready to be expanded. 