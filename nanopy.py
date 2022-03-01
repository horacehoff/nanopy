def print_file():
    # Type the file and listen for incoming keybinding event(s)
    keyboard.write(base_file)
    keyboard.add_hotkey('ctrl+z', lambda: ask_save())
def input_file():
    # 'input the console'
    return sys.stdin.read()
def ask_save():
    # If Ctrl+Z is pressed, clear the console and ask for confirmation as to whether save the file or not
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        os.system('cls' if os.name=='nt' else 'clear')
        console.input("                   [bold red]Nanopy[/bold red] | {}                   \n[light red]Save changes ?[/light red]\nYes(Y) or No(N)\n-> ".format(file))
    except KeyboardInterrupt:
        os.system('cls' if os.name=='nt' else 'clear')
try:
    # Imports
    try:
        import sys, os
        import rich
        from rich.console import Console
        import keyboard
        import threading
        console = Console()
    except:
        # Install 'rich' module if missing and re-launch nanopy with the exact same arguments
        print("Libraries missing, installing and relaunching Nanopy...")
        import subprocess
        subprocess.call(["pip", "install", "rich"], stdout = open(os.devnull, "w"), stderr = subprocess.STDOUT)
        print("\033[A                                                          \033[A")
        os.system(" ".join(sys.argv))
    # If no file name/path is passed, print a 'guide' on how to use Nanopy
    if len(sys.argv) == 1:
        rich.print("[bold  underline red]Nanopy - Usage[/bold underline red]\nnanopy [bold green]{file}[/bold green]\nExample: [reverse]nanopy my-file.txt[/reverse]")
        exit()
    # Read given file
    file = sys.argv[1]
    base_file = "\r".join(open(file, 'r').readlines())
    # Clear terminal and print nanopy's interface
    os.system('cls' if os.name=='nt' else 'clear')
    rich.print("                   [bold red]Nanopy[/bold red] | {} | [reverse]Ctrl+Z[/reverse] to exit".format(file))
    # Start two threads, one which types the file, and another one which 'inputs the console'
    threading.Thread(target=input_file).start()
    threading.Thread(target=print_file).start()
    
except KeyboardInterrupt:
    # If Ctrl+X is pressed, clear the console and ask for confirmation as to whether save the file or not
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        console.input("                   [bold red]Nanopy[/bold red] | {}                   \n[light red]Save changes ?[/light red]\nYes(Y) or No(N)\n-> ".format(file))
    except KeyboardInterrupt:
        os.system('cls' if os.name=='nt' else 'clear')
    