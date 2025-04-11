import re
input_file = 'yoji_input.txt'  # Replace with the path to your input file
output_file = 'flashcard_output.txt'


def format_text(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as polluted_file, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in polluted_file:
            idiom = line[:4]
            rest_of_line = line[5:].strip()
            reading, definition = rest_of_line.split('] ', 1)
            reading = reading.strip('[')
            # /(n) --> match the leading /( and all chars until )  --> get rid of the part-of-speech note garbage
            definition = re.sub(r'/\([^)]*\)', '', definition).strip()
            formatted_line = f"{reading}\t{idiom}\t{definition}\n"
            outfile.write(formatted_line)

format_text(input_file, output_file)
print(f"{input_file} formatted into --> {output_file}")
