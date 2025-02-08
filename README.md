# To-Do List Management System (with Login and Registration Functions)

## I. Project Overview
This project is a to - do list management system equipped with login and registration functions. Users are required to register and log in first. After successful login, they can use various functions of the to - do list, such as adding tasks, marking tasks as completed, viewing the task list, and analyzing task completion rates. User information and to - do task information are stored in the `users.json` file respectively to ensure data persistence.

## II. Functional Features

### 1. User Management Functions
- **Registration**: Users can enter a username and password to register. The system will check if the username already exists. If not, the user information will be saved in the `users.json` file.
- **Login**: Registered users can log in to the system using their username and password. The system will verify the entered information.

### 2. To - Do List Management Functions
- **Add Task**: After logging in, users can enter a task description to add a new task to the to - do list.
- **Mark Task as Completed**: Users can view the to - do list and mark a specified task as completed based on its index.
- **Display All Tasks**: Users can view all tasks in the current to - do list, including task descriptions and completion statuses.
- **View Completion Rate and Project Analysis**: The system will count the total number of tasks, the number of completed tasks, the number of incomplete tasks, and calculate the task completion percentage.

## III. Code Structure

### 1. Class Design
- **User Class**: Represents a user, containing two attributes: `username` and `password`.
- **UserManager Class**: Responsible for user registration, login, and file storage and retrieval of user information.
    - `load_users` method: Loads user information from the `users.json` file.
    - `save_users` method: Saves user information to the `users.json` file.
    - `register` method: Checks if the username already exists. If not, it registers a new user.
    - `login` method: Verifies if the entered username and password are correct.
- **Task Class**: Represents a to - do task, containing two attributes: `description` and `completed`.
    - `mark_as_completed` method: Marks the task as completed.
    - `__str__` method: Returns a string representation of the task, including the task description and completion status.
- **ToDoList Class**: Represents a to - do list, containing a list of tasks named `tasks`.
    - `add_task` method: Adds a new task to the list.
    - `mark_task_completed` method: Marks a specified task as completed based on its index.
    - `display_tasks` method: Displays all tasks in the to - do list.
    - `get_completion_percentage` method: Calculates the task completion percentage.
    - `analyze_projects` method: Counts the total number of tasks, the number of completed tasks, the number of incomplete tasks, and outputs the completion rate.

### 2. Main Program
- `main` function: The entry point of the program. It first enters the registration and login interface. After the user logs in successfully, it enters the to - do list management interface.

## IV. Usage Instructions

### 1. Environment Requirements
This project is written in Python. Make sure you have installed the Python 3.x environment.

### 2. Running Steps
1. **Download the Code**: Download the project code to your local machine.
2. **Run the Program**: Open the terminal or command prompt, navigate to the directory where the project code is located, and run the following command:
```bash
python main.py
```
3. **Registration and Login**: After the program starts, the registration and login interface will be displayed. You can choose the following operations:
    - **Register**: Enter `1`, and then enter a username and password to register.
    - **Login**: Enter `2`, and then enter your registered username and password to log in.
    - **Exit**: Enter `3` to exit the program.
4. **To - Do List Management**: After successful login, the to - do list management interface will be displayed. You can choose the following operations:
    - **Add Task**: Enter `1`, and then enter a task description to add a new task to the list.
    - **Mark Task as Completed**: Enter `2`. The system will display the current to - do list. You need to enter the index of the task you want to mark as completed.
    - **Display All Tasks**: Enter `3` to view all tasks in the current to - do list.
    - **View Completion Rate and Project Analysis**: Enter `4` to view the task completion rate and related statistical information.
    - **Exit**: Enter `5` to exit the program.

## V. Notes
- User information is stored in the `users.json` file. Make sure the program has read and write permissions for this file.
- When entering the task index, please enter a valid integer; otherwise, an "Invalid input" prompt will appear.
- If the username you enter during registration already exists, the system will prompt you to choose another username.

## VI. Contribution and Feedback
If you find any issues with the code or have suggestions for improvement, welcome to submit Issues or Pull Requests. Also, you are welcome to contribute new functions and optimization solutions to the project. 