input_file = "br-sem-acentos.txt"
output_file = "words.pl"

with open(input_file, "r") as file:
  lines = file.readlines()

parenthesized_lines = [f"palavra({line.strip().lower()})." for line in lines]

with open(output_file, "w") as file:
  file.write("\n".join(parenthesized_lines))