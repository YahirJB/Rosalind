#Initializing the variable to store highest GC content and its label
max_gc_content = 0.0
max_gc_label = ""

# Function to calculate GC-content
def calculate_gc(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    return (gc_count / total_bases) * 100.0

# Reading the input
current_label = ""
current_seq = ""

# Read each line from the txt
while True:
    try:
        line = input()
    except EOFError:
        break # exits once it has no more inputs

    if line.startswith(">"):
        # If a line starts with '>', its a laber for the next sequence
        if current_label:
            # calculate GC for the previous
            gc_content = calculate_gc(current_seq)
            if gc_content > max_gc_content:
                max_gc_content = gc_content
                max_gc_label = current_label
            # resets
            current_label = ""
            current_seq = ""
        current_label = line.strip()[1:] # Removes '>' and leading
    else:
        # If not a label line its part of the sequence
        current_seq += line.strip()

# Calculate GC-content for the last seq if its there
if current_label:
    gc_content = calculate_gc(current_seq)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_label = current_label

# Prints out highest seq with label and GC-content
print(max_gc_label)
print(max_gc_content)
