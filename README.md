# Datadog + Vale Linter

The documentation team owned and maintained style guide utilizing the [Vale Linter][1].

## Setup

The files in this repository can be used as a [GitHub action][2] or locally.

### GitHub action

- Add the example [linting.yml file][3] to your repository's `.github/workflows` folder.
- (Optional) Update `linting.yml` styles and config files as necessary.
- (Optional) Add your custom `.vale.ini` file to your repository's root directory.

Example of linting with GitHub actions:
![GitHub actions linting][4]

### Local

- Install [Vale][5] locally.
- Optional for VS Code users:
    - Install `vale-vscode` through the [Marketplace][6].
    - Set `vale.core.useCLI` to true in the extension settings (Preferences > Extensions > Vale > Use CLI).
    - Restart VS Code.
- Download the latest release of [Docsmd][7].
- Unzip the file to your local repository's `.github/styles` folder.
- Add a [.vale.ini file][8] to your repository's root directory.
- Update your `.gitignore`:
    ```
    # Vale
    .github/styles  # required if the repo uses GitHub actions
    .vale.ini       # optional
    ```

Example of local linting with VS Code:
![VS Code linting][9]

## Development

### Updates

To update or add to already created style folders:

- Clone the repo.
- Update or add `style.yml` files as necessary.
- Push and merge the changes.
- Create `.zip` files for each style folder, for example:
    ```
    zip Docshtml.zip -r Docshtml
    zip Docsmd.zip -r Docsmd
    ```
- When everything looks good, create a [new release][10] and attach the style zip files to the release.

### Add

To add a new styles folder:

- Clone the repo.
- Add a folder to the root directory, for example: `Corpsite`
- Add at least one `style.yml` file.
- Push and merge changes.
- Create `.zip` files for each style folder, for example:
    ```
    zip Docshtml.zip -r Docshtml
    zip Docsmd.zip -r Docsmd
    zip Corpsite.zip -r Corpsite
    ```
- When everything looks good, create a [new release][10] and attach the style zip files to the release.

[1]: https://docs.errata.ai
[2]: https://github.com/errata-ai/vale-action
[3]: /examples/linting.yml
[4]: /examples/github-actions-linting.png
[5]: https://docs.errata.ai/vale/install
[6]: https://marketplace.visualstudio.com/items?itemName=errata-ai.vale-server
[7]: https://github.com/DataDog/datadog-vale/releases/latest/download/Docsmd.zip
[8]: examples/.vale.ini
[9]: /examples/vs-code-linting.png
[10]: https://github.com/DataDog/datadog-vale/releases
