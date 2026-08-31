---
name: completed-assignment
description: Complete a homework assignment from assignments/<id>/ and store the finished, tested solution in Completed Assignment/<Assignment-Name>/. Use this skill whenever the user wants to complete, solve, implement, or finish a homework assignment or exercise.
---

# Complete a Programming Assignment

Use this skill to complete a homework assignment from `assignments/<id>/` and store the finished work in `Completed Assignment/<Assignment-Name>/`. Follow these steps for every new assignment that the user wants to complete.

If the assignment isn't clear, ask the user and let them choose from the list of folders under `assignments/`.

## Step 1: Create a Dedicated Branch

Before starting any work, create a new git branch named exactly the same as the assignment's subfolder in `assignments/` (e.g. `assignments/fastapi-rest-apis` → branch `fastapi-rest-apis`).

```bash
git checkout main
git pull
git checkout -b <assignment-subfolder-name>
```

If a branch for the assignment already exists (e.g. from a previous partial attempt), reuse it instead of creating a duplicate — confirm with the user before renaming or deleting any existing branch tied to an open PR.

## Step 2: Review the Assignment

1. Read `assignments/<id>/README.md` to understand the objective and every task's requirements.
2. Read `assignments/<id>/starter-code.py` (or equivalent) to see the scaffolding to build on.

## Step 3: Create the Completed Assignment Folder

Create `Completed Assignment/<Assignment-Name>/` (title-cased, matching the assignment's theme) and copy the starter code there as the basis for the implementation. Do not modify the original files under `assignments/`.

## Step 4: Implement the Solution

Fill in each task from the README directly in the copied starter code, keeping function/route signatures intact so the assignment's expected interface is preserved. Add a `__main__` block or example usage only if it helps demonstrate the solution (e.g. plain scripts); skip it for frameworks like FastAPI where `uvicorn` runs the app.

## Step 5: Write and Run Tests

Add a `test_starter_code.py` in the same completed-assignment folder covering each task:

- For plain functions/scripts: use `pytest` with `unittest.mock.patch` to simulate `input()` where needed.
- For FastAPI (or other web frameworks): use `TestClient` (or the framework's equivalent) to exercise each route, including error/edge cases (e.g. 404, 422).

Load the module under test via `importlib.util.spec_from_file_location`, since assignment filenames use hyphens (e.g. `starter-code.py`) and aren't valid Python module names for a normal `import`.

Run the tests and confirm they all pass before considering the assignment done:

```bash
cd "Completed Assignment/<Assignment-Name>"
python3 -m pytest -v
```

## Step 6: Manual Verification

Provide the user a way to manually exercise the solution:

- Plain scripts: `python3 starter-code.py` and walk through expected prompts/output.
- FastAPI apps: `uvicorn starter-code:app --reload`, then test via `curl` or the `/docs` Swagger UI.

## Step 7: Commit and Push

Commit the new `Completed Assignment/<Assignment-Name>/` folder on the assignment's branch and push it. Open a pull request from that branch into `main` (title matching the assignment, e.g. "Python-Basics").

## Notes

- Never rename/delete a branch that has an open PR without explicit user confirmation — it can orphan the PR.
- Merging a PR is a shared-repo action; always confirm with the user before merging, and use the `gh` CLI (`gh pr merge <number> --squash`) or the GitHub web UI, since no merge tool is available by default in this environment.
