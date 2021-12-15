# Datadog + Vale Linter

The documentation team owned and maintained style guide utilizing the [Vale Linter](https://docs.errata.ai).

## Setup

The files in this repository can be used as a [GitHub action](https://github.com/errata-ai/vale-action) or locally.

### GitHub action

- Add the example [linting.yml file](/examples/linting.yml) to your repository's `.github/workflows` folder.
- (Optional) Update `linting.yml` styles and config files as necessary.
- (Optional) Add your custom `.vale.ini` file to your repository's root directory.

Example of linting with GitHub actions:
![GitHub actions linting](/examples/github-actions-linting.png)

### Local

- Install [Vale](https://docs.errata.ai/vale/install) locally.
- Optional for VS Code users:
    - Install `vale-vscode` through the [Marketplace](https://marketplace.visualstudio.com/items?itemName=errata-ai.vale-server).
    - Set `vale.core.useCLI` to true in the extension settings (Preferences > Extensions > Vale > Use CLI).
    - Restart VS Code.
- Download the latest release of [Docsmd](https://github.com/DataDog/datadog-vale/releases/latest/download/Docsmd.zip).
- Unzip the file to your local repository's `.github/styles` folder.
- Add a [.vale.ini file](examples/.vale.ini) to your repository's root directory.
- Update your `.gitignore`:
    ```
    # Vale
    .github/styles  # required if the repo uses GitHub actions
    .vale.ini       # optional
    ```

Example of local linting with VS Code:
![VS Code linting](/examples/vs-code-linting.png)

## Development

- Clone the repo.
- Update or add `style.yml` files as necessary.
- Push and merge the changes.
- Create `.zip` files for each style folder, for example:
    ```
    zip Docshtml.zip -r Docshtml
    zip Docsmd.zip -r Docsmd
    ```
- When everything looks good, create a [new release](https://github.com/DataDog/datadog-vale/releases) and attach the style zip files to the release.
