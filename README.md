# 📚 Basic Python Functions Exercise

Welcome, students! 🚀 This exercise is designed to reinforce your understanding of basic Python functionalities and testing principles.

## 🎯 Objectives

* Understand and implement simple Python functions.
* Familiarize yourself with writing and understanding unit tests.

## 🔍 Overview

Your primary working file is `exercise.py`, which contains several functions for you to implement. Each function has its own specifications outlined in its docstrings.

You are encouraged to use the `driver()` function present in the `exercise.py` file to test out your implementations. 

## ✅ Tasks

### 1️⃣ Understand the Distributed Code

- Open `exercise.py` and `test.py` and familiarize yourself with the functions' stubs.
- Review each function's docstrings to understand its expected behavior.
- Run `exercise.py` using the command:

```bash
python exercise.py
```

To get a feel for the function

### 2️⃣ Implementing the Functions

Within `exercise.py`:

- Add your implementation for each function based on the description in the docstring.
- Uncomment the corresponding section in the `driver()` function to see your functions in action.
- Run `exercise.py` to ensure your implementation produces the expected output.

### 3️⃣ Implement Unit Tests

In `tests.py`:

- You will find stubbed test methods corresponding to each function in `exercise.py`.
- Your task is to implement these test methods to validate the correctness of the functions you've implemented.
- Ensure each of your tests is comprehensive, covering edge cases asked from you.

**Transitioning from `assert` to `assertEqual`**:
You've been accustomed to using the `assert` statement to perform checks. In unit testing, especially with the `unittest` framework, we transition to using methods like `assertEqual`.

Instead of:
```python
assert function_name(args) == expected_output
``` 

For this exercise, we will use the unittest framework, which means tests will be written in the format:

```python
self.assertEqual(function_name(args), expected_output)
``` 

They work quite similarly. We ran an example so you can follow it.

### 3️⃣ Committing and Pushing Changes using VSCode Codespaces

Once all the tests have completed:

1. **Stage Changes**: 
   - View your changes in the Source Control view.
   - Click on the `+` (plus) sign next to the files you wish to stage.
2. **Commit Changes**: 
   - Enter a descriptive commit message.
   - Press `Ctrl + Enter` (or `Cmd + Enter` on macOS) to commit the changes.
3. **Push Changes**: 
   - Click on the ellipsis `...` in the Source Control view.
   - Select **Push**.
4. **Verify you code has passed**: 


## 📘 Resources

- **Uni Tests *: Review foundational knowledge with Python’s CS50 Notes [Notes](https://cs50.harvard.edu/python/2022/notes/5/)

## 🤔 Need Help?

- **Clarifications**: Don’t hesitate to ask for clarifications regarding the functionality of the on Discord.
- **Debugging**: If you’re grappling with bugs or issues, seek help! Debugging is key to learning.
- **Answer**: We have a file called the_answer.py. Only look at it if you are stuck for some time (30 min+)

Should your functions exhibit unexpected behaviors or issues:
- Place breakpoints in your code within VSCode.
- Use the VSCode debugger to navigate through your code, inspect variables, and diagnose potential issues.
- Modify your code as needed, guided by your findings during debugging.
- [Debugger Tutorial](https://www.youtube.com/watch?v=7qZBwhSlfOo&t=7s)
