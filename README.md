# 🚀 SysCLI

A tiny Python library that makes terminal apps look way cooler with almost no effort.

No more boring `print()` spam.
No more ugly CLI menus.
Just clean banners, colorful messages, menus, separators, and stylish prompts.

---

## 📦 Installation

```bash
pip install syscli
```

Or clone the repository:

```bash
git clone https://github.com/waasaty/SysCLI.git
```

---

## 🚀 Quick Start

```python
import SysCLI

SysCLI.Config.program_name("MyCoolApp")

SysCLI.print_header()

SysCLI.print_info("Application started")
SysCLI.print_succes("Everything works!")
SysCLI.print_warn("Something looks suspicious...")
SysCLI.print_error("Oops, an error occurred")
SysCLI.print_dbg("Debug message")
```

Output:

```text
╭─────────────╮
│ MyCoolApp   │
╰─────────────╯

[i] information
[✓] succes
[!] warning
[✗] error
[~] debug
```

---

## 📝 User Input

Create nice-looking input prompts:

```python
import SysCLI

SysCLI.input_start_header()

name = SysCLI.input_middle("Enter your name")
age = SysCLI.input_bottom("Enter your age")
```

Example:

```text
╭─ waasaty@MyCoolApp [12:12:12]
├─❯ Enter your name:
╰─❯ Enter your age:
```

---

## 📋 Menus

```python
SysCLI.print_menu(
    "Main Menu",
    [
        "Start",
        "Settings",
        "Exit"
    ]
)
```

Output:

```text
╭───────────────╮
│ Main Menu     │
├───────────────┤
│ 1. Start      │
│ 2. Settings   │
│ 3. Exit       │
╰───────────────╯
```

---

## 🎨 Banners

```python
SysCLI.print_banner("""
Welcome to
My Awesome App
""")
```

---

## 🔧 Configuration

Change the displayed program name:

```python
SysCLI.Config.program_name("SuperApp")
```

Now prompts and headers will use:

```text
username@SuperApp
```

---

## 💡 Why SysCLI?

Because writing:

```python
print("[INFO] Application started")
```

for the 500th time gets boring.

SysCLI gives your terminal projects a cleaner and more professional look while keeping everything simple.

---

## 🤝 Contributing

Found a bug?
Have an idea?
Open an issue or submit a pull request.

Contributions are always welcome.

---

## 📜 License

MIT License

Do whatever you want, just don't claim you wrote it 😄