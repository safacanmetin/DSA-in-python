def read_and_reverse():
    print("Enter lines of text. Type 'END' on a new line to stop input:")
    lines = []
    while True:
        line = input()
        if line == "END": 
            break
        lines.append(line)
    for line in reversed(lines):
        print(line)

read_and_reverse()
