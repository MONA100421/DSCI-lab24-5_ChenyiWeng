[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CrI0ZZ6G)
[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=16219592&assignment_repo_type=AssignmentRepo)
# DSCI 510 Fall 24 (32427R) Lab Assignment 5
Welcome to the ___Lab Assignment 5___! Please implement all the functions present in `lab5.py` and use the testing script provided to make sure your functions produce correct results.

## Testing your solution
- **Locally**
    ```bash
    # To install dependencies on your local machine
    pip install -r requirements.txt

    # Finally, run the test suite
    pytest -v
    ```
- **GitHub Actions**
    - Commit & Push your latest version of changes
        ```bash
        git add .                                   # Stage the new changes
        git commit -m "update: lab5.py"         # Commit the changes
        git push                                    # Push the new changes
        ```
    - Now, you can see the evalution report under the `Actions` section of your repository.
    - Everytime you push a new version of your code, a `GitHub Actions` workflow will be triggered and run.

## Evaluation Report
- Click on the latest workflow run to see the latest evaluation report generated.
    > Here you are tested on public test cases (a part of the test suite)
- Check the greyed Annotations saying `Autograding complete` with a test score.
    > This is not the **actual score** for your assignment. It means you pass all the public test cases.
- The assignment will be tested on private test suite after the _deadline_.
    > Private test cases may also include tricky and edge cases for you shall implement proper logic to handle them well.