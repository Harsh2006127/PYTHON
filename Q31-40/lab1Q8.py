total_seconds = int(input("Enter seconds: "))


hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{hours} Hours, {minutes} Minutes, {seconds} Seconds")