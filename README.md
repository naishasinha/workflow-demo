# workflow-demo
A demo repository for practicing GitHub Actions/YAML.
***
**Topics:** branch protection, creating a workflow, testing workflows, github secrets + environment variables <br>
**Workflow objective:** every time we try to make a change to the repository, we want to automatically run all tests in `code_test.py`
***
**Relevant Git Commands:** <br>
1. Pull changes from main branch: `git pull origin main`
3. Create a new branch: `git checkout -b [branch-name]`
4. Add and create commit: `git add .` `git commit -m "add commit"`
5. Push commit to origin branch: `git push origin [branch-name]`
6. Test locally before triggering workflow: `python -m unittest discover -s . -p '*_test.py'`
