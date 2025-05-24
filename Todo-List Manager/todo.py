import argparse
import json
import os

TODO_FILE = "todos.json"

# Load todos from file or initialize if not found
def load_todos():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    else:
        return []

# Save todos back to file
def save_todos(todos):
    with open(TODO_FILE, "w") as f:
        json.dump(todos, f, indent=2)

# Add a new task
def add_todo(task):
    todos = load_todos()
    todos.append({"task": task, "done": False})
    save_todos(todos)
    print(f'Added task: "{task}"')

# List all tasks
def list_todos():
    todos = load_todos()
    if not todos:
        print("No tasks found.")
        return
    for i, todo in enumerate(todos, 1):
        status = "✓" if todo["done"] else " "
        print(f"{i}. [{status}] {todo['task']}")

# Mark a task as done
def mark_done(index):
    todos = load_todos()
    if index < 1 or index > len(todos):
        print("Invalid task number.")
        return
    todos[index - 1]["done"] = True
    save_todos(todos)
    print(f'Marked task {index} as done.')

# Main function with argparse
def main():
    parser = argparse.ArgumentParser(description="Todo List Manager")
    subparsers = parser.add_subparsers(dest="command")

    # add command
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("task", help="The task description")

    # list command
    subparsers.add_parser("list", help="List all tasks")

    # done command
    parser_done = subparsers.add_parser("done", help="Mark a task as done")
    parser_done.add_argument("index", type=int, help="Task number to mark done")

    args = parser.parse_args()

    if args.command == "add":
        add_todo(args.task)
    elif args.command == "list":
        list_todos()
    elif args.command == "done":
        mark_done(args.index)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
