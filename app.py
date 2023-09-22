from flask import Flask, render_template,request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/solution', methods=['GET','POST'])
def solve_sudoku():
    if request.method=='POST':
        # Create a 2D array to store the input values
        sudoku_grid = [[0 for _ in range(9)] for _ in range(9)]

        for row in range(1, 10):
            for col in range(1, 10):
                input_id = f"{row}{col}"
                input_value = request.form.get(input_id, '')
                if input_value.isdigit():
                    sudoku_grid[row - 1][col - 1] = int(input_value)

        # Print or process the sudoku_grid
        for row in sudoku_grid:
            print(row)
        return render_template('solution.html')
        # Extract input values from the form and populate the 2D array 
    else:
        return render_template('index.html')

