def print_file():
    keyboard.write(base_file_output)
    keyboard.add_hotkey('ctrl+z', lambda: ask_save())
def input_file():
    return sys.stdin.read()
def ask_save():
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        console.input("                   [bold red]Nanopy[/bold red] | {}                   \n[light red]Save changes ?[/light red]\nYes(Y) or No(N)\n-> ".format(file))
    except KeyboardInterrupt:
        os.system('cls' if os.name=='nt' else 'clear')
try:# Imports
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
    file = sys.argv[1]
    os.system('cls' if os.name=='nt' else 'clear')
    os.system('mode 400,150')
    base_file = open(file, 'r')
    base_file_lines = base_file.readlines()
    base_file_output = "\r".join(base_file_lines)
    userInput = rich.print("                   [bold red]Nanopy[/bold red] | {}                   ".format(file))
    threading.Thread(target=input_file).start()
    threading.Thread(target=print_file).start()
    
except KeyboardInterrupt:
    os.system('cls' if os.name=='nt' else 'clear')
    try:
        console.input("                   [bold red]Nanopy[/bold red] | {}                   \n[light red]Save changes ?[/light red]\nYes(Y) or No(N)\n-> ".format(file))
    except KeyboardInterrupt:
        os.system('cls' if os.name=='nt' else 'clear')
    