#!/usr/bin/env python3
"""voyager_cli/main.py - CLI entry point with argparse subcommands."""

import argparse
from voyager_cli.storage import TaskStorage


def cmd_add(args):
    """Add a new task."""
    storage = TaskStorage()
    task_id = storage.add_task(args.title)
    print(f"Added task {task_id}: {args.title}")


def cmd_list(args):
    """List all tasks."""
    storage = TaskStorage()
    tasks = storage.get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task.done else "○"
        print(f"[{status}] {task.id}: {task.title}")


def cmd_done(args):
    """Mark a task as done."""
    storage = TaskStorage()
    try:
        storage.mark_done(args.task_id)
        print(f"Task {args.task_id} marked as done.")
    except ValueError as e:
        print(f"Error: {e}")


def cmd_timer(args):
    """Timer placeholder (not yet implemented)."""
    print("Timer feature coming soon!")


def main():
    parser = argparse.ArgumentParser(
        prog="voyager",
        description="Voyager CLI - Personal task and time management."
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # todo group (nested subparser)
    todo_parser = subparsers.add_parser("todo", help="Task management commands")
    todo_subparsers = todo_parser.add_subparsers(dest="todo_command", help="Todo subcommands")

    # todo add
    add_parser = todo_subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title/description")
    add_parser.set_defaults(func=cmd_add)

    # todo list
    list_parser = todo_subparsers.add_parser("list", help="List all tasks")
    list_parser.set_defaults(func=cmd_list)

    # todo done
    done_parser = todo_subparsers.add_parser("done", help="Mark a task as done")
    done_parser.add_argument("task_id", type=int, help="Task ID to mark done")
    done_parser.set_defaults(func=cmd_done)

    # timer (top-level subcommand)
    timer_parser = subparsers.add_parser("timer", help="Start a timer (placeholder)")
    timer_parser.set_defaults(func=cmd_timer)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return

    # Handle nested todo commands
    if args.command == "todo" and hasattr(args, 'todo_command') and args.todo_command:
        args.func(args)
    elif args.command != "todo":
        args.func(args)
    else:
        todo_parser.print_help()


if __name__ == "__main__":
    main()
