# Contributing to pygeosys


## Styleguides

This project follows the PEP8 style guide. You can use flake8/black for linting and formatting. 

We have defined a couple of rules to ignore.
In `.vscode` directory, add the following in your `settings.json` file :
```
{
    "python.linting.flake8Enabled": true,
    "python.linting.enabled": true,
    "python.linting.flake8Args": ["--ignore=E501"]
}
```

## Git commit messages 

1. Use the present tense ("Add feature" not "Added feature")
2. Use the imperative mood in the subject line ("Add the thing", not "Adds the thing")
3. Limit the subject line to 50 characters
4. Capitalize the subject line
5. Do not end the subject line with a period
6. Separate subject from body with a blank line
7. Do not put references to issues in the subject, but at the bottom of the body