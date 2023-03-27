# bpc-rails-demo-pytest

This project was inspired by [Test Framework with Pytest and Page Object Model](https://github.com/aifakhri/web-app-testing-framework-example). However, I wanted to use [pipenv](https://github.com/pypa/pipenv) to manage dependencies.



1. Install [pyenv](https://github.com/pyenv/pyenv)
```
brew update
brew install pyenv
```

2. Install python
```
pyenv install 3.11.2
pyenv global 3.11.2
```

3. [Install](https://pipenv.pypa.io/en/latest/installation/#installing-pipenv) [pipenv](https://github.com/pypa/pipenv)
```
install pipenv --user
```

Per the docs:
Note:
This does a `user installation`_ to prevent breaking any system-wide
packages. If `pipenv` isn't available in your shell after installation,
you'll need to add the user site-packages binary directory to your `PATH`.

On Linux and macOS you can find the user base binary directory by running
`python -m site --user-base` and adding `bin` to the end. For example,
this will typically print `~/.local` (with `~` expanded to the
absolute path to your home directory) so you'll need to add
`~/.local/bin` to your `PATH`. You can set your `PATH` permanently by
`modifying ~/.profile`_.

---

Updated .zshrc:
```
# pipenv
export PATH=~/.local/bin:$PATH
```

4. Run tests:
```
pipenv run pytest
```

