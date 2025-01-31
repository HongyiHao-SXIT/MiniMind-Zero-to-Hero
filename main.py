class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def mark_as_completed(self):
        self.completed = True

    def __str__(self):
        status = "已完成" if self.completed else "未完成"
        return f"{self.description} - {status}"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        task = Task(description)
        self.tasks.append(task)
        print(f"任务 '{description}' 已添加。")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            task.mark_as_completed()
            print(f"任务 '{task.description}' 已标记为已完成。")
        else:
            print("无效的任务索引。")

    def display_tasks(self):
        if not self.tasks:
            print("待办列表为空。")
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
        print(f"总任务数: {len(self.tasks)}")
        print(f"已完成任务数: {completed_count}")
        print(f"未完成任务数: {incomplete_count}")
        print(f"完成度: {self.get_completion_percentage():.2f}%")


def main():
    todo_list = ToDoList()
    while True:
        print("\n请选择操作:")
        print("1. 添加任务")
        print("2. 标记任务为已完成")
        print("3. 显示所有任务")
        print("4. 查看完成度和项目分析")
        print("5. 退出")
        choice = input("请输入选项编号: ")

        if choice == "1":
            description = input("请输入任务描述: ")
            todo_list.add_task(description)
        elif choice == "2":
            todo_list.display_tasks()
            index = int(input("请输入要标记为已完成的任务索引: "))
            todo_list.mark_task_completed(index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            todo_list.analyze_projects()
        elif choice == "5":
            print("退出程序。")
            break
        else:
            print("无效的选项，请重新输入。")


if __name__ == "__main__":
    main()