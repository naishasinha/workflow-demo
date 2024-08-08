# workflow-demo
A demo repository for practicing GitHub Actions using YAML.
***
**Topics:** Branch Protection, Creating a Workflow, Testing Workflows, Github secrets + Environment Variables, Cron (Timed) Functions <br>

**Workflow objective:** every time we try to make a change to the repository, we want to automatically run all tests in `code_test.py`

**Daily Commit:** runs the cron functions within the workflows, enabling the script to run everyday

***
**Relevant Git/Terminal Commands:** <br>
1. Pull changes from main branch: <br> `git pull origin main`
3. Create a new branch: <br> `git checkout -b [branch-name]`
4. Add and create commit: <br> `git add .` <br> `git commit -m "add commit"`
5. Push commit to origin branch: <br> `git push origin [branch-name]`
6. Test locally before triggering workflow: <br> `python -m unittest discover -s . -p '*_test.py'`
