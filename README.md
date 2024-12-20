# Quiz Generator Project

## Project Presentation

The goal of this project is to code a quiz that generates exercises directly from a code base. The principle involves creating multiple lists in JSON format and implementing them under different names, either based on difficulty or chapter. With a selection menu for difficulty levels, users can progressively enhance their learning.

This project will use JSON and Python to create a quiz based on keys defined in JSON files, allowing the Python code to retrieve information about the questions, possible answers, and correct answers. To the basic quiz, additional features will be added, such as the option to choose the difficulty level and a replay button, to explore the customizable options that can be implemented in the quiz.

---

## Code Description

### General Overview
The code uses several commands to manage the quiz. First, the `json` module is imported to enable the loading and manipulation of JSON files containing the quiz questions, using the `open` and `json.load` commands.

The `load_quiz` function loads data from a JSON file and handles errors when the file is not found.

The quiz is executed using the `run_quiz` function. `while` and `for` loops are used to prompt the user to select the number of questions and display them one by one.

`try-except` blocks handle input errors.

With input, the player can choose the difficulty, provide answers, and replay the quiz if desired.  
`if-elif-else` conditions are used to verify input validity and make decisions, such as loading the appropriate JSON file based on the selected difficulty.

The main program structure is defined by the `if __name__ == "__main__":` block, which executes the main function when the script is run.

---

### Main Code Descriptions

#### Implementation of JSON Files
JSON files store the quiz questions in a structured format. Each JSON file represents a difficulty level (e.g., easy, medium, hard).  

Structure of the JSON file:
```json
[
  {
    "question": "Your question?",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Option 2"
  }
]
