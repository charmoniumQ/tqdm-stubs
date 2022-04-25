# How to setup the development environment

## With Nix

[Nix] is a language-agnostic package manager that installs packages locally. [Nix Flakes] are a way
of specifying dependencies to Nix declaraively. Currently, they are [installed separately][install
nix flakes].

```sh
$ sh <(curl -L https://nixos.org/nix/install) --daemon
$ nix-env -iA nixpkgs.nixFlakes
$ echo 'experimental-features = nix-command flakes' >> ~/.config/nix/nix.conf
```

- `nix develop` to get a shell.
- `nix develop --command ipython` to run a command, such as `ipython`, in the project's environment.

[nix]: https://nixos.org/
[nix flakes]: https://nixos.wiki/wiki/Flakes
[install nix flakes]: https://nixos.wiki/wiki/Flakes#Installing_flakes

## With Nix and direnv

In addition to Nix, I suggest also installing [direnv] and [nix-direnv]. Then simply `cd`ing to the
project will activate the project-specific environment.

```sh
$ nix-env -iA nixpkgs.direnv nixpkgs.nix-direnv
$ echo 'eval "$(direnv hook bash)"' >> ~/.bashrc
$ echo 'source $HOME/.nix-profile/share/nix-direnv/direnvrc' >> ~/.direnvrc

$ # optional, for prompt
$ echo 'PS1="\$PREPEND_TO_PS1$PS1"' >> ~/.bashrc
```

- `cd /path/to/project` to get a shell.
- `nix develop --command ipython` to run a command, such as `ipython`, in the project's environment.

Consider adding this line in your shell's initfile so you can see when `direnv` is
activated. `PS1="\$PREPEND_TO_PS1$PS1"` Note that the sigil (dollar sign) in `$PREPEND_TO_PS1` is
quoted but the one in `$PS1` is not, so `PS1` is evaluated when the shell initializes, but
`PREPEND_TO_PS1` is evaluated before every prompt.

[direnv]: https://direnv.net/
[nix-direnv]: https://github.com/nix-community/nix-direnv

## With Poetry

Nix can be trouble to set up, so here is how to use the project without Nix. [Poetry] is a wrapper
around `pip`/`virtualenv`, and it will manage dependencies from PyPI, but *you* have to manage
external dependencies, e.g. installing the right version of Python, C libraries, etc.

```
$ sudo apt install -y python3 python3-pip
$ python -m pip --user --upgrade install poetry
$ if ! grep "$HOME/.local/bin" <(echo $PATH) ; then echo 'PATH=$HOME/.local/bin:$PATH' >> .bashrc fi
```

- `poetry shell` to get a shell.
- `poetry run ipython` to run a command, such as `ipython`, in the project's environment.

[poetry]: https://python-poetry.org/

# How to use development tools

Once in the development environment, use `./script.py` to run development tools. See the [template repository] for details. In the order of frequency of use,

- `./script.py fmt` runs code formatters.

- `./script.py test` runs tests and code complexity analysis.

- `./script.py all-tests` runs the usual tests and more. This is intended for CI.

- `./script.py docs` builds the documentation locally.

- `./script.py publish` publishes the package to PyPI and deploys the documentation to GitHub pages.

[autoimport]: https://lyz-code.github.io/autoimport/
[isort]: https://pycqa.github.io/isort/
[black]: https://black.readthedocs.io/en/stable/
[mypy]: https://mypy.readthedocs.io/en/stable/
[pylint]: https://pylint.org/
[pytest]: https://docs.pytest.org/en/7.0.x/
[coverage.py]: https://coverage.readthedocs.io/en/6.1.1/index.html
[radon]: https://radon.readthedocs.io/en/latest/
[proselint]: http://proselint.com/
[rstcheck]: https://github.com/myint/rstcheck
[twine]: https://twine.readthedocs.io/en/stable/
[tox]: https://tox.wiki/en/latest/
[bump2version]: https://github.com/c4urself/bump2version
[template repository]: https://github.com/charmoniumQ/sams-cookiecutter-pypackage/blob/main/README.md
