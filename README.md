# Building a "community-ready" repository

Do you have code that you'd like to share with others--maybe you've written a
model for your thesis, or perhaps you're required to do so by a journal--but you're
not sure of the best way to go about it?
We'll try to address this problem with the contents of this example repository.

We'll use Python because it's the standard language of CSDMS;
however, much of what we show can be translated to other languages.
We'll show how to properly package code
so that it can easily be installed and used by others.
We'll configure a GitHub repository
with files and services that will help make the code
[FAIR](https://www.nature.com/articles/s41597-022-01710-x)
(Findable, Accessible, Interoperable and Reusable)
and sustainable over time--a "community-ready" repository.

## Topics

The following topics address what could be included in a "community-ready" repository.
While we may not be able to cover all of these,
we list them for reference,
with links to resources for further exploration.

### Part 1: Setting up a repository

* Configuring *git* and GitHub ([ref](https://github.com/csdms/ivy/blob/main/lessons/git/index.md))
* Initializing a *git* repository on GitHub
* Choosing an open-source software license ([ref](https://github.com/readme/guides/open-source-licensing))
* Cloning the repository and setting up a local development environment ([ref](https://docs.python.org/3/library/venv.html), [ref](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/))

### Part 2: Packaging and sharing code

* Packaging, using guidance from the [Python Packaging Authority](https://packaging.python.org) (PyPA)
* Automating repository tasks with *nox*
* Linting and formatting code with *black*, *flake8*, and *pre-commit*
* Unit testing with *pytest*
* Continuous integration with GitHub Actions
* Building documentation with *sphinx*

### Part 3: Adding community health files

* Including instructions for contributors, and a code of conduct
* Crediting contributors
* Acknowledging funding support
* Creating a citation file with *cffinit* ([ref](https://citation-file-format.github.io/))
* Writing an informative README ([ref](https://onegoodtutorial.org/))
* Adding a Digital Object Identifier (DOI) with Zenodo

Participants will leave with a clear, practical template for sharing scientific software
in a way that supports reuse, citation, and long-term community engagement.

## Acknowledgements

The contents of this repository were developed for use in an educational clinic
at the 2026 CSDMS Annual Meeting.
Funding for this work was provided by the U.S. National Science Foundation (NSF)
under grant number [2148762](https://www.nsf.gov/awardsearch/showAward?AWD_ID=2148762),
*Collaborative Research: Facility: CSDMS: Engaging a thriving community of practice in Earth-surface dynamics*.
