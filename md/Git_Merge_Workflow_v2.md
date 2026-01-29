# Git Merge Workflow: Main to Feature Branches

## Overview

This guide explains how to keep your feature branch up-to-date with the latest changes from the `main` branch.

---

## Why Merge Main into Feature Branches?

When working on a feature branch, the `main` branch may receive updates from other team members. To avoid conflicts later and ensure your code works with the latest changes, you should regularly merge `main` into your feature branch.

```
Scenario:
┌─────────────────────────────────────────────────────────────┐
│  main:     A---B---C---D---E  (other team members pushed)   │
│                 \                                            │
│  feature:        F---G        (your work)                    │
│                                                              │
│  Goal: Bring changes D and E into your feature branch       │
└─────────────────────────────────────────────────────────────┘
```

---

## Method 1: Merge (Recommended for Beginners)

### Step-by-Step Process

#### 1. Ensure You're on Your Feature Branch
```bash
git checkout feature/employee-routes
```

**Output:**
```
Switched to branch 'feature/employee-routes'
```

---

#### 2. Check Your Current Status
```bash
git status
```

**Output:**
```
On branch feature/employee-routes
Your branch is up to date with 'origin/feature/employee-routes'.

nothing to commit, working tree clean
```

💡 **Important:** Commit or stash any uncommitted changes before merging!

If you have uncommitted changes:
```bash
# Option A: Commit your changes
git add .
git commit -m "wip: Save work in progress"

# Option B: Stash your changes (temporary save)
git stash save "WIP changes before merge"
```

---

#### 3. Fetch Latest Changes from Remote
```bash
git fetch origin
```

**Output:**
```
remote: Enumerating objects: 15, done.
remote: Counting objects: 100% (15/15), done.
remote: Compressing objects: 100% (8/8), done.
remote: Total 10 (delta 5), reused 8 (delta 2), pack-reused 0
Unpacking objects: 100% (10/10), done.
From https://github.com/username/employee-management-api
   a1b2c3d..e4f5g6h  main       -> origin/main
```

💡 **What `fetch` does:** Downloads changes from GitHub but doesn't apply them yet.

---

#### 4. Merge Main into Your Feature Branch
```bash
git merge origin/main
```

**Scenario A: Clean Merge (No Conflicts)**

**Output:**
```
Updating a1b2c3d..e4f5g6h
Fast-forward
 app/models.py    | 25 +++++++++++++++++++++++++
 app/database.py  | 15 +++++++++++++++
 main.py          | 10 ++++++++--
 3 files changed, 48 insertions(+), 2 deletions(-)
```

**Success!** Your branch now has all changes from main.

---

**Merge Conflicts**

**Output:**
```
Auto-merging app/models.py
CONFLICT (content): Merge conflict in app/models.py
Auto-merging main.py
CONFLICT (content): Merge conflict in main.py
Automatic merge failed; fix conflicts and then commit the result.
```

---

#### 5. Resolve Conflicts (If They Occur)

##### Check Which Files Have Conflicts
```bash
git status
```

**Output:**
```
On branch feature/employee-routes
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
        both modified:   app/models.py
        both modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")
```


#### 6. Complete the Merge

```bash
git commit -m "merge: Resolve conflicts with main branch"
```

**Output:**
```
[feature/employee-routes c7d8e9f] merge: Resolve conflicts with main branch
```

---

#### 7. Push Updated Branch to Remote

```bash
git push origin feature/employee-routes
```

**Output:**
```
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (8/8), 1.25 KiB | 1.25 MiB/s, done.
Total 8 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 3 local objects.
To https://github.com/username/employee-management-api.git
   a1b2c3d..c7d8e9f  feature/employee-routes -> feature/employee-routes
```

**Success!** Your feature branch is now updated with main and pushed to GitHub.

---

## Method 2: Rebase (Advanced)

### When to Use Rebase
- You want a cleaner, linear history
- Your feature branch hasn't been pushed to remote yet
- You're comfortable with Git

### Rebase Workflow

#### 1. Fetch Latest Changes
```bash
git fetch origin
```

#### 2. Rebase Your Branch onto Main
```bash
git rebase origin/main
```

**Clean Rebase Output:**
```
First, rewinding head to replay your work on top of it...
Applying: feat: Add mission model
Applying: feat: Add mission routes
```

**Conflict During Rebase:**
```
CONFLICT (content): Merge conflict in app/models.py
error: could not apply a1b2c3d... feat: Add mission model
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
```

#### 3. Resolve Conflicts

```bash
# Edit conflicted files
# Remove conflict markers
# Keep the changes you want

# Mark as resolved
git add app/models.py

# Continue rebase
git rebase --continue
```

#### 4. Force Push (Required for Rebase)

**Warning:** Only force push if you're the only one working on this branch!

```bash
git push origin feature/employee-routes --force-with-lease
```

---

## Complete Workflow Example

### Scenario: Student B Needs to Merge Main into Mission Feature

```bash
# Student B's workflow
cd employee-management-api

# 1. Switch to feature branch
git checkout feature/mission-routes

# 2. Save any uncommitted work
git status
git add .
git commit -m "wip: Save current work"

# 3. Fetch latest from GitHub
git fetch origin

# 4. Merge main into your branch
git merge origin/main

# 5. If conflicts occur, resolve them
# Edit conflicted files
# Remove <<<<<<< ======= >>>>>>> markers
# Keep both changes appropriately

# 6. Mark conflicts as resolved
git add app/models.py
git add app/database.py
git add main.py

# 7. Complete the merge
git commit -m "merge: Integrate latest changes from main"

# 8. Test your code
python -m pytest tests/

# 9. Push to GitHub
git push origin feature/mission-routes
```

---

## Visual Workflow Diagram

```
Before Merge:
═══════════════════════════════════════════════════════
main:           A---B---C---D---E
                     \
feature/mission:      F---G---H

After Merge:
═══════════════════════════════════════════════════════
main:           A---B---C---D---E
                     \           \
feature/mission:      F---G---H---M (merge commit)

M contains: Your changes (F, G, H) + Main changes (D, E)
```

---

## Useful Git Commands

### Check Merge Status
```bash
# See which branch you're on
git branch

# See if merge is in progress
git status

# View merge conflicts
git diff
```

### Abort a Merge
```bash
# If you want to start over
git merge --abort
```

### View Merge History
```bash
# See merge commits
git log --oneline --graph --all

# See what changed in merge
git show HEAD
```

### Compare Branches
```bash
# See what's in main but not in your branch
git log feature/employee-routes..origin/main

# See the actual changes
git diff feature/employee-routes..origin/main
```

---

## Best Practices

###  DO

1. **Commit before merging**
   ```bash
   git add .
   git commit -m "feat: Complete employee routes"
   git merge origin/main
   ```

2. **Merge frequently**
   - Don't wait weeks to merge main
   - Merge at least once per day if main is active

3. **Test after merging**
   ```bash
   git merge origin/main
   pytest tests/
   python main.py  # Make sure it runs
   ```

4. **Use descriptive merge commit messages**
   ```bash
   git commit -m "merge: Integrate mission routes from main"
   ```

5. **Communicate with team**
   - Let team know you're merging
   - Ask for help with conflicts

###  DON'T

1. **Don't merge with uncommitted changes**
   ```bash
   # BAD
   git merge origin/main  # While you have unsaved files
   
   # GOOD
   git add .
   git commit -m "wip: Save progress"
   git merge origin/main
   ```

2. **Don't force push shared branches**
   ```bash
   # BAD if others are using this branch
   git push --force origin feature/shared-branch
   ```

3. **Don't delete conflict markers accidentally**
   ```bash
   # BAD - leaving markers in code
   <<<<<<< HEAD
   class Mission:
   =======
   ```

4. **Don't panic during conflicts**
   - Read the conflict carefully
   - Understand both changes
   - You can always `git merge --abort`

---

## Troubleshooting

### Problem: "Your local changes would be overwritten by merge"

**Solution:**
```bash
# Commit your changes first
git add .
git commit -m "wip: Save current work"

# Then merge
git merge origin/main
```

---

### Problem: "Already up to date" but you know there are changes

**Solution:**
```bash
# Fetch to make sure you have latest refs
git fetch origin

# Check what's on main
git log origin/main

# Try merge again
git merge origin/main
```

---

### Problem: Too many conflicts, want to start over

**Solution:**
```bash
# Abort the merge
git merge --abort

# Clean your working directory
git reset --hard HEAD

# Try again with a fresh approach
git merge origin/main
```

---

### Problem: Accidentally committed conflict markers

**Solution:**
```bash
# Find the markers
grep -r "<<<<<<< HEAD" .

# Fix the files
# Then amend your commit
git add .
git commit --amend --no-edit

# Force push if already pushed
git push origin feature/your-branch --force-with-lease
```

---

## Summary Checklist

### Before Creating a Pull Request

- [ ] Switch to your feature branch
- [ ] Commit all your changes
- [ ] Fetch latest from origin
- [ ] Merge origin/main into your branch
- [ ] Resolve any conflicts
- [ ] Test your code
- [ ] Push to origin
- [ ] Create PR on GitHub

### Complete Command Sequence

```bash
git checkout feature/your-branch
git add .
git commit -m "feat: Complete your feature"
git fetch origin
git merge origin/main
# (resolve conflicts if any)
git add .
git commit -m "merge: Integrate latest main changes"
python -m pytest tests/
git push origin feature/your-branch
```

---

## Quick Reference Card

| Task | Command |
|------|---------|
| Switch to feature branch | `git checkout feature/name` |
| Save current work | `git add . && git commit -m "wip"` |
| Fetch latest changes | `git fetch origin` |
| Merge main into feature | `git merge origin/main` |
| Check conflict status | `git status` |
| Mark conflict resolved | `git add <file>` |
| Complete merge | `git commit -m "merge message"` |
| Abort merge | `git merge --abort` |
| Push changes | `git push origin feature/name` |
| View merge history | `git log --graph --oneline` |

---

**Remember:** Merging is normal! Don't be afraid of conflicts—they're just Git asking you to make a decision about code. 🚀
