## Overview

The [Datadog Documentation team][13] implements, maintains, and owns a style guide utilizing the [Vale Linter][1]. This repository contains a set of linting rules for Vale based on the [Documentation Style Guide][10].

## Setup

1. Clone this repository.
1. Install Vale with `brew install vale` (macOS) or `choco install vale` (Windows). 
1. Set the `StylesPath` parameter to `styles/Datadog` in your `.vale.ini`file.
1. Run `vale .` from the root folder of the repository, or specify a file to lint on using `vale /path/to/some/directory`.

## Usage

Rules are stored in YAML files, and you can set `Docshtml` to lint on HTML, and `Docsmd` to lint on Markdown files in your `.vale.ini` file. Make sure all files are lowercase.

For example, this [`gender.yml` rule][3] raises an error when Vale detects a gendered pronoun in a Markdown file:

```yml
extends: existence
message: "Use a gender-neutral pronoun instead of '%s'."
link: "https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md#gender"
level: error
ignorecase: true
tokens:
  - he/she
```

The files in this repository contain settings for the Vale linter (defined in `.vale.ini`) and style rules published by the Datadog Docs team (defined in `styles/Datadog`). These can be used as a [GitHub Action][2] or locally.

### GitHub Action

1. Add the example [linting.yml file][3] to your repository's `.github/workflows` folder.
1. (Optional) Update `linting.yml` styles and config files as necessary.
1. (Optional) Add your custom `.vale.ini` file to your repository's root directory.

Example of linting with GitHub Actions:<br>
![GitHub Actions linting][4]

### Local

1. Install [Vale][5] locally.
1. Optional for VS Code users:
    * Install `vale-vscode` through the [Marketplace][6].
    * Set `vale.core.useCLI` to true in the Extension Settings (**Preferences** > **Extensions** > **Vale** > **Use CLI**).
    * Restart VS Code.
1. Download the latest release of the [source code][7].
1. Unzip the file to your local repository's `.github/styles` folder.
1. Add a [.vale.ini file][8] to your repository's root directory.
1. Update your `.gitignore`:
   ```
   # Vale
   .github/styles  # required if the repo uses GitHub Actions
   .vale.ini       # optional
   ```

Example of local linting with VS Code:<br>
![VS Code linting][9]

## License

Code—including sample code—in this repository is licensed under the [Apache 2.0 license][11].

[1]: https://docs.errata.ai
[2]: https://github.com/errata-ai/vale-action
[3]: /examples/linting.yml
[4]: /examples/github-actions-linting.png
[5]: https://vale.sh/docs/vale-cli/installation/
[6]: https://marketplace.visualstudio.com/items?itemName=errata-ai.vale-server
[7]: https://github.com/DataDog/datadog-vale/releases/
[8]: examples/.vale.ini
[9]: /examples/vs-code-linting.png
[10]: https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md
[11]: https://github.com/DataDog/datadog-vale/blob/main/LICENSE
[13]: https://github.com/DataDog/documentation