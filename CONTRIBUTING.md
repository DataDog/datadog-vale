# Contributing

First of all, thanks for contributing!

This document provides some basic guidelines for contributing to this repository. To propose improvements, feel free to submit a pull request.

## Submitting issues

GitHub issues are welcome, so feel free to submit style requests! Make sure to add enough details to explain your use case. Are you having an issue with the Datadog product? Contact [Datadog Support][1].

## Pull Requests

Have you updated an existing rule or want to propose a rule for the [Documentation Site Style Guide][2]? 

In order to ease/speed up our review, here are some items you can check for when submitting your pull request:

- Keep commits small and focused, and rebase your branch if needed.
- Write meaningful commit messages and pull request titles that are concise but explanatory.


## Usage

Rules are stored in YAML files in the `Docshtml` directory to lint on HTML, and in the `Docsmd` directory to lint on Markdown files. Make sure all files are lowercase.

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

For more information about updating and contributing to this repository, see the [Development section][4].

[1]: https://docs.datadoghq.com/help/
[2]: https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md
[3]: https://github.com/DataDog/datadog-vale/blob/main/Docsmd/gender.yml
[4]: https://github.com/DataDog/datadog-vale#development