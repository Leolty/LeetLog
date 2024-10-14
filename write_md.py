import json
import os
from pathlib import Path

def parse_problems(input_file, output_dir):
    # Create the output directory if it doesn't exist
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    with open(input_file, 'r') as f:
        for line in f:
            problem = json.loads(line)
            
            # Create a subdirectory for each difficulty level
            difficulty_dir = Path(output_dir) / problem['difficulty']
            difficulty_dir.mkdir(exist_ok=True)
            
            # Create a markdown file for each problem
            file_name = f"{problem['number']:04d}_{problem['title'].replace(' ', '_')}.md"
            file_path = difficulty_dir / file_name
            
            with open(file_path, 'w') as out_file:
                out_file.write(f"# {problem['number']}. {problem['title']}\n\n")
                out_file.write(f"Difficulty: {problem['difficulty']}\n\n")
                out_file.write(f"Link: {problem['link']}\n\n")
                out_file.write("## Problem Statement\n\n")
                out_file.write(f"{problem['statement']}\n\n")
                
                if problem['hints']:
                    out_file.write("## Hints\n\n")
                    for hint in problem['hints'].split('\n'):
                        out_file.write(f"- {hint.strip()}\n")
                
                out_file.write("\n## Code Templates\n\n")
                for lang, template in problem['templates'].items():
                    out_file.write(f"### {lang.capitalize()}\n")
                    out_file.write(f"```{lang}\n{template}\n```\n\n")

if __name__ == "__main__":
    input_file = "problemset.jsonl"
    output_dir = "leetcode_problems"
    parse_problems(input_file, output_dir)
    print(f"Problems have been parsed and written to {output_dir}")