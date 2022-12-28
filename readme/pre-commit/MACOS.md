## Installation & Configuration
**_*  In order to make install process easy and quick on macOS you should use Homebrew. Installation instructions can be
found [here](../HOMEBREW.md) *_**

Just execute command below in order to install it on your laptop
```zsh
brew install pre-commit
```

Alternative way of installation is to use `pip3`
```zsh
pip3 install pre-commit
```

Additional packages which will be used in pre-commit hooks
Install [tflint](https://github.com/terraform-linters/tflint)
```zsh
brew install tflint
```

Install [markdown-link-check](https://github.com/tcort/markdown-link-check)
```zsh
brew install node
npm install -g markdown-link-check
```

Run pre-commit install to set up the git hook scripts.
```zsh
pre-commit install
```
That’s it! Now every time you commit a code change (.tf file), the hooks in the hooks: config will execute.

After formatting you need to  ```git add file_modified``` to commit formatter changes.

If you want to delete existing pre-commit hooks, execute command below:
```zsh
pre-commit uninstall
```
