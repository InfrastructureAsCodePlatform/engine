## Installation & Configuration
Before you can run hooks, you need to have the pre-commit package manager installed.
```bash
pip3 install pre-commit
```
Install [tflint](https://github.com/terraform-linters/tflint)
```bash
curl https://raw.githubusercontent.com/terraform-linters/tflint/master/install_linux.sh | bash
```

Install [markdown-link-check](https://github.com/tcort/markdown-link-check)
```bash
sudo npm install -g markdown-link-check
```

Run pre-commit install to set up the git hook scripts.
```bash
pre-commit install
```
That’s it! Now every time you commit a code change (.tf file), the hooks in the hooks: config will execute.

After formatting you need to  ```git add file_modified``` to commit formatter changes.

If you want to delete existing pre-commit hooks, execute command below:
```bash
pre-commit uninstall
```
