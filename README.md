# Calculator
Beeware Desktop App

# Prerequisites for running BeeWare:
Python 3.5 or higher
Git, a version control system. You can download Git from from <a href="git-scm.org">git-scm.org</a><br>
.
WiX Toolset, a set of utilities for building Windows installers. An installer can be obtained from <a href="https://wixtoolset.org/releases/"> the WiX Toolset website</a><br>

#setting up virtual environment<br>
`md beeware-tutorial`<br>
`cd beeware-tutorial`<br>
`py -m venv beeware-venv`<br>
`beeware-venv\Scripts\activate.bat`<br>

We need to install briefcase. Briefcase is a BeeWare tool that can be used to package your application for distribution to end users - but it can also be used to bootstrap a new project.<br>
`python -m pip install briefcase`<br>
briefcase new command to create our application MyCalculator<br>
`briefcase new`<br>

Briefcase will ask us for some details of our new application<br>
Formal Name - Accept the default value:<br>
App Name - Accept the default value: <br>
Bundle - If you own your own domain, enter that domain in reversed order. (For example, if you own the domain “cupcakes.com”, enter com.cupcakes as the bundle). If you don’t own your own domain, accept the default bundle (com.example)<br>
Project Name - Accept the default value: <br>
Description - Accept the default value (or, if you want to be really creative, come up with your own description!)<br>
Author - Enter your own name here<br>
Author’s email - Enter your own email address. This will be used in the configuration file, in help text, and anywhere that an email is required when submitting the app to an app store.<br>
URL - The URL of the landing page for your application. Again, if you own your own domain, enter a URL at that domain (including the https://). Otherwise, just accept the default URL (https://example.com/helloworld). This URL doesn’t need to actually exist (for now); it will only be used if you publish your application to an app store.<br>
License - Accept the default license (BSD). <br>
GUI framework - Accept the default option, Toga (BeeWare’s own GUI toolkit).<br>

file system is generated which look like:

beeware-tutorial
    beeware-venv
        ...<br>
    MyCalculator/<br>
        LICENSE<br>
        README.rst<br>
        pyproject.toml<br>
        src/<br>
            MyCalculator/<br>
                resources/<br>
                    MyCalculator.icns<br>
                    MyCalculator.ico<br>
                    MyCalculator.png<br>
                __init__.py<br>
                __main__.py<br>
                app.py<br>
#running app in developer mode<br>
`cd MyCalculator`<br>
`briefcase dev`<br>

This will open the window having calculator GUI.<br>
#packaging for distribution in window<br>
`briefcase create`<br>
#building application<br>
`briefcase build`<br>
#building installer<br>
`briefcase build`<br>
Once this step completes, the windows folder will contain a file named MyCalculator-0.0.1.msi. If you double click on this installer it will install with usual procedure of installation on window.
