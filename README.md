# nbinteract-tutorial to Run the Jupyter Notebook in Binder server to make Interactive webpages
I implemented the computation of file distribution analysis by implementing the file distribution time formula in a custom python function code on a Jupyter notebook. The main advantage of using Jupyter notebook is that it will help to bring interactivity and dynamic computation. 

It will also help you implement the use of sliders for dynamically regulating the File size, uplink speed, downlink speed and latency. Once the code is implemented in Jupyter notebook it needs to be converted to a webpage so that it can be accessed by the users.

So I have used nbinteract which is Python package that provides a command-line tool to generate interactive web pages from Jupyter notebooks. It allows Jupyter widgets to remain interactive even when the notebook is converted to static HTML by using Binder servers as the computational backend. 

Nbinteract also provides Python functions for simple, interactive plots. These interactions are driven by data, not callbacks, allowing authors to focus on the logic of their programs. It is used by data scientists to create interactive blog spots and also for students who work on data analysis that contain interactive demo. The ipywidgets library helps in developing interactive webpages for graph plotting. We use binder server to render webpages from Jupyter notebook. 

We Provide a URL or a GitHub repository that contains Jupyter notebooks, as well as a branch, tag, or commit hash.

Launch will build your Binder repository. If you specify a path to a notebook file, the notebook will be opened in your browser after building. Binder will search for a dependency file, such as requirements.txt or environment.yml, in the repository's root directory. The dependency files will be used to build a Docker image. 

If an image has already been built for the given repository, it will not be rebuilt. If a new commit has been made, the image will automatically be rebuilt. A JupyterHub server will host the repository's contents. It offers you a reusable link and badge to the live repository that we can easily share with others. 

We go to the link http://mybinder.org/ and paste in the URL of the repository that has been created. It should look like: https://github.com/grdhrc/nbinteract-tutorial . 

After this we open a notebook interface, click on New -> Terminal. This should open a terminal prompt. Run the following commands: pip install nbinteract which Installs nbinteract, then we use the command nbinteract init  which initializes nbinteract and installs the packages present in the requirements.txt file

We then execute the following commands 
git add -A
git commit -m "Setup nbinteract"
git push origin master
The above commands are executed so that it initializes the nbinteract package and pushes the configuration files to GitHub. Next in order to convert a notebook into an HTML file, start a terminal and run the following command
nbinteract notebookname.ipynb
This generates a corresponding html file which contains the logic of the python script executed in the Jupyter notebook and then push the files into github by executing the following commands
git add -A
git commit -m "Publish nb"
git push origin master
I have used github as my repository in this project as binder server require the notebook files to be stored in github so that they can be fetched by the binder server online and can be rendered into a webpage. I have incorporated the study material for users in the form of interactive YouTube videos by implementing iframes and I have also used html and JavaScript to embed images in the Jupyter notebook which was later rendered into the webpage.


nbinteract
nbinteract is a Python package that provides a command-line tool to generate interactive web pages from Jupyter notebooks. It allows Jupyter widgets to remain interactive even when the notebook is converted to static HTML by using Binder servers as the computational backend.

nbinteract also provides Python functions for simple, interactive plots. These interactions are driven by data, not callbacks, allowing authors to focus on the logic of their programs.

nbinteract is useful for:

Data scientists that want to create simple interactive blog posts without having to know / work with Javascript.
Instructors that want to include interactive examples in their textbooks.
Students that want to publish data analysis that contains interactive demos.

Converting Notebooks¶
From the command line:

# Run on the command line to convert the notebook into a publishable HTML page.
#
# nbinteract {NOTEBOOK.ipynb} -s {BINDER_SPEC}
#
# Replace {BINDER_SPEC} with a Binder spec in the format
# {username}/{repo}/{branch} (e.g. SamLau95/nbinteract-image/master).
# The branch is optional; if omitted, defaults to `master`
#
# Replace {NOTEBOOK.ipynb} with the name of the notebook file to convert.
#
# For example:
nbinteract homepage.ipynb -s SamLau95/nbinteract-image
After initializing a GitHub repo and running nbinteract init, you may omit the Binder spec and simply write:

nbinteract homepage.ipynb

Motivation:
nbinteract aims to enable authors and educators to easily create and share interactive web pages.

Interactive explanations of concepts are useful for communicating and explaining tricky concepts. Consider these explanations for linear regression and conditional probability, for example.

However, making an interactive webpage often requires significant knowledge of web technologies and especially Javascript. While Jupyter widgets allow authors to generate interactive interfaces directly in a Jupyter notebook, sharing these demos typically requires readers to run the notebook. This causes issues when the reader's computer lacks (correct versions of) the packages needed to completely run the notebook.

nbinteract provides a single binary that converts Jupyter notebooks into HTML pages. The resulting HTML pages can be shared with the public, keeping any interactivity created using Jupyter widgets. For example, the interactive parts of this website are entirely generated from notebooks using nbinteract.

In addition, nbinteract provides a Python package. Once imported, nbinteract provides helper methods that allow users to create simple interactive visualizations with single function calls.

Installing Locally¶
If you prefer to work on your local machine, you need to install the nbinteract package. To install the package, run the following commands in your terminal:

pip install nbinteract

# The next two commands can be skipped for notebook version 5.3 and above
jupyter nbextension enable --py --sys-prefix bqplot
jupyter nbextension enable --py --sys-prefix widgetsnbextension

Next you need to follow the steps in the link to setup github repository:
https://www.nbinteract.com/tutorial/tutorial_github_setup.html

Creating an Account and Repo¶
To begin, visit https://github.com/ and create an account. If you already have an account, you should log in.

Then, create a new repo. You may do this using the GitHub UI or visiting https://github.com/new . Name the repo nbinteract-tutorial. If you'd like a different name, feel free to name it something else; just keep in mind that we will use this repo name in later parts of the tutorial.

Make sure your repo is public, and click the checkbox to initialize your repo with a README. Your page should look like:

gh-repo-setup

Now, click on the Settings link for the repo near the top of the page, scroll down to the GitHub Pages section, and select the master branch as the GitHub pages source. Click the Save button to save your changes.

gh-pages-setup

Now, any file you upload to this repo will have a public URL. For example, the README.md file in the repo has the following URL:

{username}.github.io/nbinteract-tutorial/README.md
Where {username} is replaced with your GitHub username. For example, if my username is SamLau95, my URL is:

SamLau95.github.io/nbinteract-tutorial/README.md
If you can visit that URL and the page contains text (and not a 404 error) you've set up your GitHub repo correctly.

Cloning Your Repo¶
Now, visit http://mybinder.org/ and paste in the URL to your repo. It should look like:

https://github.com/{username}/nbinteract-tutorial
Where {username} is replaced with your GitHub username.

Launch the Binder server to open Jupyter.

If you are working locally, you should instead run the following commands in your terminal:

# Clone the repo
git clone https://github.com/{username}/nbinteract-tutorial

# Move into the repo directory
cd nbinteract-tutorial

# Start Jupyter
jupyter notebook
Initializing nbinteract¶
Via the notebook interface, click on New -> Terminal. This should open a terminal prompt. Run the following commands:

# Installs nbinteract
pip install nbinteract

# Initializes nbinteract. When prompted, create a requirements.txt file. Since we aren't
# adding additional packages in this tutorial, re-run the command to finish initialization.
nbinteract init

git add -A
git commit -m "Setup nbinteract"
git push origin master
This initializes the nbinteract package and pushes the configuration files to GitHub.

If you are working locally, skip the pip install command above and run the remaining commands in your terminal.

Publishing A Webpage¶
To convert a notebook into an HTML file, start a terminal and run the following command.

nbinteract tutorial.ipynb
This generates a tutorial.html file with the contents of the notebook created in the previous section. Now, push your files to GitHub by running:

git add -A
git commit -m "Publish nb"
git push origin master
After pushing, you now have a URL you can view and share:

{username}.github.io/nbinteract-tutorial/tutorial.html
Where {username} is replaced with your GitHub username. For example, if my username is SamLau95, my URL is:

SamLau95.github.io/nbinteract-tutorial/tutorial.html
Publishing to a different URL¶
To change the URL of the page you publish, you can rename your notebook before you convert it. For example, if you rename tutorial.ipynb to hello.ipynb and convert the notebook, the resulting URL becomes:

{username}.github.io/nbinteract-tutorial/hello.html
To change the path segment before the filename (in this case, nbinteract-tutorial) you can create a new GitHub repo with the subpath name you want. Then, you may create and convert notebooks in this repo. For example, if you create a new repo called blog-posts and convert a notebook called tutorial.ipynb, the resulting URL becomes:

{username}.github.io/blog-posts/tutorial.html
Workflow¶
You have learned a simple workflow to create interactive webpages:

Write a Jupyter notebook containing Python functions
Use interact to create UI elements to interact with the functions.
Run nbinteract {notebook} in a terminal to generate an interactive webpage using your notebook code.
Publish your webpage to GitHub pages to make it publicly accessible.
