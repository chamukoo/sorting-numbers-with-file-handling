# Programmed by: Lee Anne Y. Angeles

sort_file = open("SortNos.txt", "w")                          # Open file in write mode
even_file = open("even_nos.txt", "w")
odd_file = open("odd_nos.txt", "w")

for x in range(1, 21):                                        # Iterates from 1 to 20
    x = str(x)                                                # Converts integer to string
    sort_file.write(x)                                        # Write number to an output file
    sort_file.write(" ")                                      # Space to separate numbers
sort_file.close()                                             # Close text file

count_even = 0                                                # Stores the total count of even numbers
for y in range(1, 21):                                        # Iterates from 1 to 20
    if y % 2 == 0:                                            # Count the even numbers
        y = str(y)                                            # Identify even numbers
        count_even += 1                                       # Convert integer to string
        even_file.write(y)                                    # Write even numbers in an output file
        even_file.write(" ")                                  # Space to separate numbers
even_file.write("\n")                                         # Separate even numbers and count of even numbers by line
even_file.write(str(count_even))                              # Write the total count of even numbers in an output file
even_file.close()                                             # Close file

count_odd = 0                                                 # Stores the total count of odd numbers
for z in range(1, 21):                                        # Iterates from 1 to 20
    if z % 2 == 1:                                            # Identify odd numbers
        count_odd += 1                                        # Count the odd numbers
        z = str(z)                                            # Convert integer to string
        odd_file.write(z)                                     # Write odd numbers in an output file
        odd_file.write(" ")                                   # Space to separate numbers
odd_file.write("\n")                                          # Separate even numbers and count of even numbers by line
odd_file.write(str(count_odd))                                # Write the total count of even numbers in an output file
odd_file.close()                                              # Close file
