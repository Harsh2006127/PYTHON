try:
    file = open("data.txt", "r")
    content = file.read()
    print("File Content:")
    print(content)
    file.close()

except FileNotFoundError:
    print("Error: File not found")

except PermissionError:
    print("Error: Permission denied")

except IOError:
    print("Error: Input/Output error occurred")

except Exception as e:
    print("Other Error:", e)