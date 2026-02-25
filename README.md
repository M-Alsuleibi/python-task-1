## Time & Planning Summary
I read the task and thought of splitting each core requirement into separate modules, to apply single responsibility principle.
For each requirement I thought what is the high-level logic I would use:
- Req. A- OOP
- Req. B- csv read and write
- Req. C- menu loop with core logic empedded inside it
- Req. D- use try..expect, handle user bad input

My initial time plan was for each requirement like this:
1. Initial CLI, folder structure and basic Class - 1 hour
2. csv related logic - 1 hour
3. core logic methods + reflecting each method to cli - 3 hours
4. testing various edge cases and check exceptions maybe not handled - 1 hour
5. filling readme file with summary and how-to-run info- 30 minutes
- Total Time: 6.5 hours
## How to Run

### 1. Clone the repo
```
git clone git@github.com:M-Alsuleibi/python-task-1.git
cd python-task-1
```
### 2. Create and activate virtual environment
```
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows
```
### 3. Run the program
```
python main.py
```