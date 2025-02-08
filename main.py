import json


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


class UserManager:
    def __init__(self, file_path="users.json"):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                user_data = json.load(file)
                return {user['username']: User(user['username'], user['password']) for user in user_data}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def save_users(self):
        user_data = [{'username': user.username, 'password': user.password} for user in self.users.values()]
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(user_data, file, ensure_ascii=False, indent=4)

    def register(self, username, password):
        if username in self.users:
            print("This username already exists. Please choose another one.")
            return False
        self.users[username] = User(username, password)
        self.save_users()
        print("Registration successful!")
        return True

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print("Login successful!")
            return True
        print("Incorrect username or password. Please try again.")
        return False


class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "Completed" if self.completed else "Incomplete"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"Task '{description}' has been added.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_as_completed()
            print(f"Task '{task.description}' has been marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("The to - do list is empty.")
        else:
            for i, task in enumerate(self.tasks):
                print(f"{i}. {task}")

    def get_completion_percentage(self):
        if not self.tasks:
            return 0
        completed_count = sum(task.completed for task in self.tasks)
        return (completed_count / len(self.tasks)) * 100

    def analyze_projects(self):
        completed_count = sum(task.completed for task in self.tasks)
        incomplete_count = len(self.tasks) - completed_count
        print(f"Total tasks: {len(self.tasks)}")
        print(f"Completed tasks: {completed_count}")
        print(f"Incomplete tasks: {incomplete_count}")
        print(f"Completion rate: {self.get_completion_percentage():.2f}%")


def main():
    user_manager = UserManager()
    logged_in = False
    username = ""

    while not logged_in:
        print("\nPlease select an operation:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Please enter the option number: ")

        if choice == "1":
            username = input("Please enter a username: ")
            password = input("Please enter a password: ")
            user_manager.register(username, password)
        elif choice == "2":
            username = input("Please enter your username: ")
            password = input("Please enter your password: ")
            logged_in = user_manager.login(username, password)
        elif choice == "3":
            print("Exiting the program.")
            return
        else:
            print("Invalid option. Please try again.")

    todo_list = ToDoList()
    while True:
        print("\nPlease select an operation:")
        print("1. Add a task")
        print("2. Mark a task as completed")
        print("3. Display all tasks")
        print("4. View completion rate and project analysis")
        print("5. Exit")
        choice = input("Please enter the option number: ")

        if choice == "1":
            description = input("Please enter the task description: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.display_tasks()
            try:
                index = int(input("Please enter the index of the task to mark as completed: "))
                todo_list.mark_task_completed(index)
            except ValueError:
                print("Invalid input. Please enter a valid integer index.")
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.analyze_projects()
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
