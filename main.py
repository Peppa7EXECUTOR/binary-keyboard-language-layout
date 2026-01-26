import keyboard


print(r'''
 ____  _                      
| __ )(_)_ __   __ _ _ __ _   _
|  _ \| | '_ \ / _` | '__| | | |
| |_) | | | | | (_| | |  | |_| |
|____/|_|_| |_|\__,_|_|   \__, |
                          |___/ 
      
 _               _                         _
| | _____ _   _ | |__   ___   __ _ _ __ __| |
| |/ / _ \ | | || '_ \ / _ \ / _` | '__/ _` |
|   <  __/ |_| || |_) | (_) | (_| | | | (_| |
|_|\_\___|\__, ||_.__/ \___/ \__,_|_|  \__,_|
           |___/


MIT License, Project by Peppa7EXECUTOR
      ''')

ASCII_TO_BINARY = {chr(i): f"{i:08b}" for i in range(128)}

CONTROL_NAMES = {0: "NUL", 1: "SOH", 2: "STX", 3: "ETX", 4: "EOT", 5: "ENQ", 6: "ACK", 
                 7: "BEL", 8: "BS", 9: "TAB", 10: "LF", 11: "VT", 12: "FF", 13: "CR",
                 14: "SO", 15: "SI", 16: "DLE", 17: "DC1", 18: "DC2", 19: "DC3", 
                 20: "DC4", 21: "NAK", 22: "SYN", 23: "ETB", 24: "CAN", 25: "EM", 26: "SUB",
                 27: "ESC", 28: "FS", 29: "GS", 30: "RS", 31: "US", 127: "DEL"}

buffer = ""
caps_on = False
pause_button = False

def print_binary(event):
    global buffer, caps_on, pause_button
    key = event.name

    if key == "f1":
        print("\nBye Bye!")
        keyboard.unhook_all()
        return
    if key == "f3":
        pause_button = not pause_button
        print("Paused" if pause_button else "Resumed")
        return
    if pause_button:
        if key == "space":
            keyboard.write(" ")
        elif key == "enter":
            keyboard.write("\n")
        elif key == "tab":
            keyboard.write("\t")
        elif key == "backspace":
            keyboard.send("backspace")
        elif len(key) == 1:
            keyboard.write(key)
        return
    
    if key == "caps lock":
        caps_on = not caps_on 
        return
    
    if key == "space":
        char = " "
    elif key == "enter":
        char = "\n"
    elif key == "tab":
        char = "\t"
    elif key == "backspace":
        if buffer.endswith(" "):
           buffer = buffer.rstrip()
           last = buffer.split(" ")[-1]
           keyboard.write("\b" * (len(last) + 1))
           buffer = " ".join(buffer.split(" ")[:-1]) + " "
        return
    elif len(key) == 1:
        char = key.upper() if caps_on else key
    else:
        return 

    binary = ASCII_TO_BINARY.get(char)
    if binary:
        code = ord(char)
        label = CONTROL_NAMES.get(code, char)
        
        print(f"[{label}] {binary}")
        keyboard.write(binary + " ")
        buffer += binary + " "

keyboard.on_press(print_binary, suppress=True)
keyboard.wait()