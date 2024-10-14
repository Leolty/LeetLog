# 💻 LeetLog

LeetLog contains a collection of the most recent LeetCode problems, intended **solely for research and educational purposes**. This dataset includes problems posted after May 2024.

## 📊 Dataset

The main dataset is stored in `problemset.jsonl`, a JSON Lines file where each line represents a single LeetCode problem.

> For easier reading, individual problem statements are also available as markdown files in the [`leetcode_problems`](./leetcode_problems) directory. A web application is also provided to browse and view the problems interactively. For more details on using the app, see the [Web Application](#web-application) section.

### ⏳ Time Coverage

The dataset includes problems posted after May 2024. Please note that exact posting times are not included, as they are unavailable. If you need to filter problems based on a specific time cutoff, you may estimate the posting time by visiting the corresponding LeetCode problem page and checking the timestamp of the most recent discussion.

### 🗂️ Data Structure

Each problem entry in the dataset contains the following attributes:

- `number`: The unique LeetCode problem number
- `title`: The title of the problem
- `link`: The URL link to the problem on LeetCode
- `difficulty`: The problem's difficulty level (Easy, Medium, Hard)
- `statement`: The full problem statement
- `templates`: Code templates for multiple programming languages (C++, Java, Python)
- `hints`: Hints for solving the problem (if available)
- `contains_png`: A boolean indicating whether the problem includes PNG images
- `png_links`: A list of URLs to PNG images used in the problem (if applicable)

### 📖 Example

Here’s an example of a single problem entry in the dataset:

```json
{
    "number": 3138,
    "title": "Minimum Length of Anagram Concatenation",
    "link": "https://leetcode.com/problems/minimum-length-of-anagram-concatenation/",
    "difficulty": "medium",
    "statement": "You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.\n\nReturn the **minimum** possible length of the string `t`.\n\nAn **anagram** is formed by rearranging the letters of a string. For example, \"aab\", \"aba\", and, \"baa\" are anagrams of \"aab\".\n\n**Example 1:**\n\n**Input:** s \\= \"abba\"\n\n**Output:** 2\n\n**Explanation:**\n\nOne possible string `t` could be `\"ba\"`.\n\n**Example 2:**\n\n**Input:** s \\= \"cdef\"\n\n**Output:** 4\n\n**Explanation:**\n\nOne possible string `t` could be `\"cdef\"`, notice that `t` can be equal to `s`.\n\n**Constraints:**\n\n* `1 <= s.length <= 105`\n* `s` consist only of lowercase English letters.",
    "templates": {
        "cpp": "class Solution {\npublic:\n    int minAnagramLength(string s) {\n        \n    }\n};",
        "java": "class Solution {\n    public int minAnagramLength(String s) {\n        \n    }\n}",
        "python": "class Solution:\n    def minAnagramLength(self, s: str) -> int:\n        "
    },
    "hints": "1\\. The answer should be a divisor of `s.length`.\n2\\. Check each candidate naively.",
    "contains_png": false,
    "png_links": []
}
```

## 🛠️ Processing Script

The `process.py` script is used to process raw crawled data and generate the `problemset.jsonl` file.

⚠️ **Note:** This script is provided for **personal reference only** and **cannot be run** without the raw crawled data, which is not included in this repository due to potential licensing issues.

To use the script:

```
python process.py [--raw_problemset_dir DIR] [--output_file FILE] [--force_process]
```

- `--raw_problemset_dir`: Directory containing raw problem data (default: "./raw-problemset")
- `--output_file`: Output file for processed problems (default: "./problemset.jsonl")
- `--force_process`: Force processing of all problems, ignoring previously processed data.

## 📘 Problem Display Scripts

### Display LeetCode Problems

This script processes the `problemset.jsonl` file and saves each problem as a separate Markdown file in a specified directory `./leetcode_problems`. This allows for easy reading and browsing of individual problems.

Usage:
```
python display_leetcode_problems.py [--input_file FILE] [--output_dir DIR]
```

- `--input_file`: Input JSONL file (default: "./problemset.jsonl")
- `--output_dir`: Output directory for Markdown files (default: "./leetcode_problems")

### Web Application

This is a Flask web application that provides a user-friendly interface for browsing and displaying LeetCode problems from the dataset.

To run the web application:
1. Clone the repository and `cd` into the repository directory.
2. Install required packages: `pip install flask markdown`
3. Run the script: `python app.py`
4. Open a web browser and go to `http://localhost:5000`


## ⚖️ Disclaimer

This dataset is for educational and research purposes only. All problem statements and related content are the property of LeetCode. Please refer to LeetCode's terms of service for usage rights and restrictions.
