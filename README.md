# nbinteract-tutorial
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
