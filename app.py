from flask import Flask, render_template, request, jsonify
import json
import markdown

app = Flask(__name__)

# Load all problems into memory
problems = {}
with open('problemset.jsonl', 'r') as f:
    for line in f:
        problem = json.loads(line)
        problems[problem['number']] = problem

# Get the range of available problem numbers
available_numbers = sorted(problems.keys())
min_number = min(available_numbers)
max_number = max(available_numbers)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', min_number=min_number, max_number=max_number, available_numbers=available_numbers)

@app.route('/problem/<int:problem_number>', methods=['GET'])
def get_problem(problem_number):
    problem = problems.get(problem_number)
    if problem:
        # Convert Markdown to HTML
        problem['statement'] = markdown.markdown(problem['statement'])
        return jsonify(problem)
    else:
        return jsonify({"error": "Problem not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)