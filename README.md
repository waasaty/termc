# 🚀 TermC

A tiny Python library that makes terminal apps look way cooler with almost no effort.

No more boring `print()` spam.
No more ugly CLI menus.
Just clean banners, colorful messages, menus, separators, and stylish prompts.

---

## 📦 Installation

<!-- ```bash
pip install termc
```

Or clone the repository: -->

```bash
git clone https://github.com/waasaty/termc.git
```

---

## 🚀 Quick Start

```python
import termc

termc.termcConfig.program_name("MyCoolApp")

termc.header()

termc.info("Application started")
termc.success("Everything works!")
termc.warn("Something looks suspicious...")
termc.error("Oops, an error occurred")
termc.dbg("Debug message")
```

Output:

```text
╭─────────────╮
│ MyCoolApp   │
╰─────────────╯

[i] information
[✓] success
[!] warning
[✗] error
[~] debug
```

---

## 📝 User Input

Create nice-looking input prompts:

```python
import termc

termc.prompt_header()

name = termc.prompt_mid("Enter your name")
age = termc.prompt_bot("Enter your age")
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
termc.menu(
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
termc.banner("""
Welcome to
My Awesome App
""")
```

Output:

```
╭────────────────╮
│ Welcome to     │
│ My Awesome App │
╰────────────────╯
```

---

## 🔧 Configuration

Change the displayed program name:

```python
termc.termcConfig.program_name("SuperApp")
```

Now prompts and headers will use:

```text
username@SuperApp
```

Change the preset:
```python
termc.termcConfig.preset("default")
```
Available presets: ```default, mono, ocean, sunset```


---

## 💡 Why termc?

Because writing:

```python
print("[INFO] Application started")
```

for the 500th time gets boring.

termc gives your terminal projects a cleaner and more professional look while keeping everything simple.

---

## 🤝 Contributing

Found a bug?
Have an idea?
Open an issue or submit a pull request.

Contributions are always welcome.

---

## 📜 License

MIT License

---
Do whatever you want, just don't claim you wrote it ;)