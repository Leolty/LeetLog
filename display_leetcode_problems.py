import json
import os
from pathlib import Path

def display_leetcode_problems(input_file, output_dir):
    # Create the output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(input_file, 'r') as f:
        for line in f:
            problem = json.loads(line)
            
            # Create a markdown file for each problem
            file_name = f"{problem['number']:04d}_{problem['title'].replace(' ', '_')}.md"
            file_path = Path(output_dir) / file_name
            
            with open(file_path, 'w') as out_file:
                out_file.write(f"# {problem['number']}. {problem['title']}\n\n")
                out_file.write(f"Difficulty: {problem['difficulty']}\n\n")
                out_file.write(f"Link: {problem['link']}\n\n")
                out_file.write(f"Contains PNG: {'Yes' if problem['contains_png'] else 'No'}\n\n")
                
                if problem['png_links']:
                    out_file.write("PNG Links:\n")
                    for link in problem['png_links']:
                        out_file.write(f"- {link}\n")
                    out_file.write("\n")
                
                out_file.write("## Problem Statement\n\n")
                out_file.write(f"{problem['statement']}\n\n")
                
                if problem['hints']:
                    out_file.write("## Hints\n\n")
                    for hint in problem['hints'].split('\n'):
                        out_file.write(f"- {hint.strip()}\n")
                    out_file.write("\n")
                
                out_file.write("## Code Templates\n\n")
                for lang, template in problem['templates'].items():
                    out_file.write(f"### {lang.capitalize()}\n")
                    out_file.write(f"```{lang}\n{template}\n```\n\n")

if __name__ == "__main__":
    input_file = "problemset.jsonl"
    output_dir = "leetcode_problems"
    display_leetcode_problems(input_file, output_dir)
    print(f"Problems have been written to {output_dir}")