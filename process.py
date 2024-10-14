"""
LeetCode Problem Data Processor

This script processes LeetCode problem data from raw files and converts it into a structured format.
It handles markdown parsing, file reading, and JSON output generation.

Usage:
    python leetcode_data_processor.py [--raw_problemset_dir DIR] [--output_file FILE] [--force_process]

Author: Tianyang Liu
Date: Oct 14, 2024
"""

import json
import os
import re
import argparse
from tqdm import tqdm
from markdownify import markdownify as md

def normalize_markdown(content: str) -> str:
    """
    Normalize markdown content by removing excessive newlines.

    Args:
        content (str): The markdown content to normalize.

    Returns:
        str: Normalized markdown content.
    """
    lines = content.split('\n')
    normalized_lines = []
    last_line_empty = False
    
    for line in lines:
        if line.strip() == '':
            if not last_line_empty:
                normalized_lines.append('')
                last_line_empty = True
        else:
            normalized_lines.append(line)
            last_line_empty = False
    
    return '\n'.join(normalized_lines).strip('\n')

def split_markdown_by_sections(markdown_content: str) -> list:
    """
    Split markdown content into sections based on h2 headers.

    Args:
        markdown_content (str): The markdown content to split.

    Returns:
        list: A list of dictionaries containing section titles and content.
    """
    pattern = r'^##\s*(.*?)$(.*?)(?=^##|\Z)'
    matches = re.finditer(pattern, markdown_content, re.MULTILINE | re.DOTALL)
    
    sections = []
    for match in matches:
        section_title = match.group(1).strip()
        section_content = match.group(2).strip()
        sections.append({
            'title': section_title,
            'content': normalize_markdown(md(section_content))
        })
    
    return sections

def parse_title_string(title_string: str) -> dict:
    """
    Parse the title string to extract problem number, title, and link.

    Args:
        title_string (str): The title string to parse.

    Returns:
        dict: A dictionary containing parsed information or None if parsing fails.
    """
    match = re.match(r'\[(\d+)\. (.+)\]\((.+)\)', title_string)
    if match:
        return {
            'problem_number': match.group(1),
            'problem_title': match.group(2),
            'link': match.group(3)
        }
    return None

def find_png_links(parsed_data: str) -> list:
    """
    Find PNG links in the parsed data.

    Args:
        parsed_data (str): The parsed data to search for PNG links.

    Returns:
        list: A list of PNG links found in the data.
    """
    png_pattern = r'(https://assets\.leetcode\.com/.+?\.png)'
    png_links = re.findall(png_pattern, parsed_data)
    return png_links if png_links else []

def process_problem(problem_dir: str, problem_num: str) -> dict:
    """
    Process a single LeetCode problem.

    Args:
        problem_dir (str): The directory containing problem files.
        problem_num (str): The problem number.

    Returns:
        dict: A dictionary containing processed problem data or None if processing fails.
    """
    file_paths = {
        'readme': os.path.join(problem_dir, "README.md"),
        'information': os.path.join(problem_dir, "information.json"),
        'cpp_template': os.path.join(problem_dir, "Solution.cpp"),
        'java_template': os.path.join(problem_dir, "Solution.java"),
        'python_template': os.path.join(problem_dir, "Solution.py")
    }

    # Check if all required files exist
    if not all(os.path.exists(path) for path in file_paths.values()):
        print(f"Missing files for problem {problem_num}, skipping...")
        return None

    with open(file_paths['readme'], "r", encoding="utf-8") as f:
        readme_content = f.read()
    
    sections = split_markdown_by_sections(readme_content)
    hints = next((s['content'] for s in sections if s['title'].lower() == 'hints'), None)
    problem_title, problem_statement = next(((s['title'], s['content']) for s in sections if s['title'].lower() != 'hints'), (None, None))
    problem_title_dic = parse_title_string(problem_title)
    png_links = find_png_links(problem_statement)

    with open(file_paths['information'], 'r') as information_file:
        information = json.load(information_file)
    
    difficulty = information['difficulty']

    templates = {}
    for lang, path in [('cpp', file_paths['cpp_template']),
                       ('java', file_paths['java_template']),
                       ('python', file_paths['python_template'])]:
        with open(path, 'r') as f:
            templates[lang] = f.read()
    
    return {
        'number': problem_num,
        'title': problem_title_dic['problem_title'],
        'link': problem_title_dic['link'],
        'difficulty': difficulty,
        'statement': problem_statement,
        'templates': templates,
        'hints': hints,
        'contains_png': bool(png_links),
        'png_links': png_links
    }

def main(raw_problemset_dir: str, output_file: str, force_process: bool = False):
    """
    Main function to process LeetCode problems and save them to a file.

    Args:
        raw_problemset_dir (str): Directory containing raw problem data.
        output_file (str): Output file for processed problems.
        force_process (bool): If True, process all problems regardless of previous processing.
    """
    processed_problems = set()
    if not force_process and os.path.exists(output_file):
        with open(output_file, 'r') as f:
            for line in f:
                problem = json.loads(line)
                processed_problems.add(problem['number'])
        print(f"Found {len(processed_problems)} previously processed problems.")

    crawl_log_path = os.path.join(raw_problemset_dir, 'crawled_problems.log')
    with open(crawl_log_path, 'r') as f:
        crawl_logs = [json.loads(line) for line in f]

    data = []
    for crawl_log in tqdm(crawl_logs, desc="Processing problems"):
        problem_num = crawl_log['number']
        
        if crawl_log['status'] == 'failed' or (not force_process and problem_num in processed_problems):
            continue

        problem_path = next((d for d in os.listdir(raw_problemset_dir) if d.startswith(f"{problem_num}.")), None)
        if problem_path is None:
            continue

        problem_dir = os.path.join(raw_problemset_dir, problem_path)
        problem_data = process_problem(problem_dir, problem_num)
        
        if problem_data:
            data.append(problem_data)

    # Append new data to the existing file
    mode = 'a' if not force_process else 'w'
    with open(output_file, mode) as f:
        for problem in data:
            json.dump(problem, f)
            f.write('\n')

    print(f"Processed {len(data)} new problems. Total problems in dataset: {len(processed_problems) + len(data)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LeetCode Problem Data Processor")
    parser.add_argument("--raw_problemset_dir", default="./raw-problemset", help="Directory containing raw problem data")
    parser.add_argument("--output_file", default="./problemset.jsonl", help="Output file for processed problems")
    parser.add_argument("--force_process", action="store_true", help="Force process all problems, ignoring previously processed data")
    args = parser.parse_args()

    main(args.raw_problemset_dir, args.output_file, args.force_process)