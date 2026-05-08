from voyager_cli.colors import Colors


def print_task(task):
    status = Colors.green("✓") if task.done else Colors.red("○")
    pri_colors = {"high": Colors.red, "medium": Colors.yellow, "low": Colors.blue}
    pri = pri_colors.get(task.priority, lambda x: x)(task.priority)
    print(f"[{status}] {task.id}: {task.title} | {pri} | [{task.category}]")
