max_gc_content = 0.0
max_gc_label = ""

def calculate_gc(sequence):
    gc_count = sequence.count('G') + sequence.count('C')
    total_bases = len(sequence)
    return (gc_count / total_bases) * 100.0

current_label = ""
current_seq = ""

while True:
    try:
        line = input()
    except EOFError:
        break

    if line.startswith(">"):
        if current_label:
            gc_content = calculate_gc(current_seq)
            if gc_content > max_gc_content:
                max_gc_content = gc_content
                max_gc_label = current_label
            current_label = ""
            current_seq = ""
        current_label = line.strip()[1:]
    else:
        current_seq += line.strip()

if current_label:
    gc_content = calculate_gc(current_seq)
    if gc_content > max_gc_content:
        max_gc_content = gc_content
        max_gc_label = current_label

print(max_gc_label)
print(max_gc_content)
