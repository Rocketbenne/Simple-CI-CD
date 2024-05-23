# Simple CI/CD-Setup

This is a simple Project, which should help setting up a simple CI/CD-System that creates a workflow, which can install dependencies, run tests a lint with a single version of Python.

### Step 1
---

Create a Project on GitHub.

### Step 2
---

Create and apply an access token in GitHub. This is optional and only required if the access to the pipeline should be limited, so that not everyone can modify the pipeline.
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
Create the yml-file which controls the workflow of the pipeline.

note for later. if secret added, also needed some lines of code in yml file