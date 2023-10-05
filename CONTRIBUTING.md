# Contributing

First of all, thanks for contributing! This document provides some basic guidelines for contributing to this repository. To propose improvements, feel free to submit a pull request.

## Opening issues

GitHub issues are welcome, so feel free to open an issue about an existing style rule. Make sure to add enough details and examples to explain your use case clearly.

For example, if you'd like the [`words.yml` rule][7] to flag on the word "Dirrty", open an [issue][8] and include a justification in the description such as, "Dirrty is the name of a 2002 Christina Aguilera song from her album _Stripped_. If an instance of "Dirrty" appears in the documentation, it is most likely a typo." 

Are you having an issue with the Datadog product? Contact [Datadog Support][1].

## Submitting rules

Are you interested in contributing your team's product-specific terminology and vocabulary to the [Documentation Site Style Guide][2]? 

1. Create a folder such as `[Product Name]-Names` and add it to the [`Styles/Datadog` folder][4].
2. Update the [CODEOWNERS file][5] with your team's GitHub handle.
3. Update the `StylesPath` to point to the approriate directory in your team repository's [`.vale.ini` file][6].

In order to ease and speed up our review, here are some items you can check for when submitting your pull request:

- Keep commits small and focused, and rebase your branch if needed.
- Write meaningful commit messages and pull request titles that are concise but explanatory.

If you are a Datadog employee, share your pull request in #documentation and a writer on the team will take a look. 

[1]: https://docs.datadoghq.com/help/
[2]: https://github.com/DataDog/documentation/blob/master/CONTRIBUTING.md
[3]: https://github.com/DataDog/datadog-vale/blob/main/Docsmd/gender.yml
[4]: https://github.com/DataDog/datadog-vale/tree/main/styles/Datadog
[5]: https://github.com/DataDog/datadog-vale/blob/main/.github/CODEOWNERS
[6]: https://github.com/DataDog/documentation/blob/master/.vale.ini
[7]: https://github.com/DataDog/datadog-vale/blob/main/styles/Datadog/words.yml
[8]: https://github.com/DataDog/datadog-vale/issues
