# Git cheatsheet #

> There are many commands of Git, and things could get complicated. Though, I find myself repeatly using the below commands. 

The list could be appended. For now, you might just be just fine only knowing the below Git commands:

### Basics ###

1. Create new branch for any new feature (in this cases, every topic)
```
git checkout -b feat/<name>
```

2. Push newly created branch to remote: 
```
git push --set-upstream origin feat/<name>
```

3. List all existing branchs
```
git branch -a
```

3. Work & code. Check your changed files wit: 
```
git status
```

4. Add changes to staging: 
```
git add .
```

5. Commit to the branch: 
```
git commit -m "YOUR MESSAGE"
```
6. Update any changes in remote (you have not been updated)
```
git pull
```
7. Push changes to remote (Bitbucket)
```
git push
```

### Conflict resolving ###

> After `git push`, the **Merge Request** (MR) is created for review and approve. To be mergeable, you should solve the conflict if any. It could be resolved on IDE (VSCode), GUI ([SourceTree](https://bitbucket.org/blog/introducing-sourcetree-git-client-microsoft-windows) for Bitbucket) or by CLI as below:

1. Rebase your branch to the target branch (that you want to merge to)
```
git rebase origin/<target>
```

2. Solve one-by-one conflicts interactively
```
git rebase --continue
```

### Fork repository ###
Pull/push from upstream repo (Forked)
```
cd LOCAL_REPO
git remote add upstream https://maianhdang@bitbucket.org/maianhdang/analytics-training-samples.git
```
then: (like "git pull" which is fetch + merge)
```
git fetch upstream
git merge upstream/main main
```
or, better, replay your local work on top of the fetched branch, like a "git pull --rebase"
```
git rebase upstream/main
```
Or, you can use the fork sync in Bitbucket UI (Docs: [Sync your fork](https://support.atlassian.com/bitbucket-cloud/docs/fork-a-repository/))

### Tag/Checkout versions ###
Tag convention: `ass.v1.0.0`: type.major.minor.patch 

- type: `ass` (assignment), `sol` (solution), `data` (data)
- major: breaking changes 
- minor: new features
- patch: bug fixes

Check if the local has all updated tags
```
 git fetch --all --tags --prune
```
Check all existing tags
```
git tag --list
```
Search by pattern (for example, assignment 1 version)
```
git tag --list 'ass.v1*' 
```
If you want to revert to a old version (for example, want to solve the assignment without seeing the solution)
```
git checkout tags/ass.v1.0.1 -b ass-1
```