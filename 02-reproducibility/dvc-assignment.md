# `dvc`: Data-as-code

## Everything-as-code
In this program, you will repeately see the phrase "Everything-as-code" - that is one of the *"Best practices", as it brings the benefits of:

- **Reproducibility (consitency)**: Everything you do is code, that a machine can run it with exactly the same step-by-step execution
- **Scalability**: As long as the code is shared, anyone (and machine) can run it. We can scale-up bring your code and run in a bigger machine, or scale-out bring your code and run it in multiple machines
- **Version control**: Track how things change other time (Git)
- **Reusability**: Reuse your code and data (just up and run)


## Data-as-code
You must have used `Git` in your job (or at least last assignment) to track your changes, contribute to a repo, and pull the updates from upstream.

There is an IMPORTANT rule!!

> **Rule**: Never commit data files (and also credentials, secret files) to `Git`.

> **Question**: Why should you not commit data files to `Git`?

```
[...] YOUR ANSWER HERE [...]
```

And, that is the reason why we have `.gitignore` files in our data folders to keep all paths/filenames that we do not want to commit and push to `Git`.

> You can check all `.gitignore` files in the data folders 

Then, how should we version control our data? If only we could colaborate and work on data files as easy as we could `git something`?

That's why `dvc` is created, and we would experiment with it in this assignment.

> `dvc` actually comes with more offers: data pipelines, model registry, metrics tracking (similar to `MLflow`). Sadly, they are not as good as other available alternatives. We would focus only on data versioning functionalities, though you can check their docs: https://dvc.org/doc


## How it work?

You might notice that the repo have these new updated files/folder:

`.dvc`: this is a hidden folders with 

- `.dvc/config`: the most important file to config `dvc`, this includes the path of remote storage. We use google-storage. You can open GCP project `analytics-training-hub` and check this bucket.

```
[core]
    remote = storage
    autostage = true
['remote "storage"']
    url = gs://dvc-data-storage
```

`dvc-data`: there is no data files there (as all `CSV` are included in `.gitignore`)

- `*.csv.dvc`: though you see several of these files. Check the contents

```
outs:
- md5: 06a8be1aaa6200ea1f710ef8e3acb055
  size: 785
  path: stories-sample.csv
```

This is not the data itself, but the representatives (placeholders) of the data. The contents are metadata associating with one version of data. `md5` is actually the hash of the data file (similar to hash id of commit in Git).

What `dvc` actually does for us:

1. Add data files to `.gitignore`
2. Replace with representative metadata `.csv.dvc` files
3. Push versions of data files into cloud storage

The version control part is handled by `git`:

4. Git add new changes in `.csv.dvc` files (if you enable auto-staging, this is automatic: `dvc config core.autostage true`)
5. Git commit new changes in `.csv.dvc` files
6. Everyone pull/push that new changes in `.csv.dvc` files 
7. With the metafiles, everyone can interact with different data version stored in cloud storage

> Everything hopefully will be clearer with the assignment below.


# Assignment

## Install `dvc`

Our familiar commands (please check typos in `requirements.txt`)

```bash
pip install -r requirements.txt
```

Or, you can run it line by line
```bash
pip install dvc
pip install dvc-gs
```

## On existing `dvc` set-up project

I have already set up `dvc` for this project, with all config and `.csv.dvc` files as you can see. Let's pull all actual `csv` data files to your local machine:

### 1 - Check the status 

Compare local with remote data versioning storage (`gs`):

```
dvc status
```

This will list for you call the files that are different from the remote storage (with the current hash id on `.csv.dvc` files).

### 2 - Pull data files from remote storage

As we will interact with `GCP` google storage, we would need to set authentication credentials.

> To use `gcloud`, you would need to install Google Cloud API [Docs: Guide-me](https://cloud.google.com/sdk/docs/install-sdk)

```
gcloud auth login
```
Once we already login:
```
dvc pull
```

> Now, you will see that three new files have already added to the data

Let's open `stories-sample.csv` and check! You will notice that it only have few lines. Check the git history (in Git CLI `git log` or Sourcetree GUI), you will notice a commit said "Mistakenly delete thousands of lines of data", with Commit ID `d8d603`.

![git-mistake](./images/git-mistake.png)

### 3 - Checkout data version before deleting

We want to revert to commit with tag `data.v.1.0.1`, Commit ID `d508e80`.

```
git checkout data.v.1.0.1 dvc-data/stories-sample.csv.dvc
```
Or
```
git checkout d508e80 dvc-data/stories-sample.csv.dvc
```
It will inform: `Update 1 path from ...`

Once the `.csv.dvc` file is updated, you can check the status again:

```
dvc status
```
And pull the data version before deleting:
```
dvc pull
```

Open `stories-sample.csv` and check! You will notice that it has been restored to number of lines before deleting.

Once you have been satisfied with this version of data, REMEMBER to commit the changes in `.csv.dvc` files:

```
git status
```

You will see `dvc-data/stories-sample.csv.dvc` has been modified and committed (as we checkout the older version before deleting mistake). Commit it:

```
git commit -m "fix: revert to the data version before deleting"
```


### 4 - Add/update data

1. Now, let's change any dataset or add a new dataset. To update new changes to `dvc`:

```
dvc add /path/to/data/file.csv
```
Notice that new files would be created/modified, you would need to `git add .`, unless you choose `auto-staging` before.
```
dvc config core.autostage true
```
2. REMEMBER that `dvc` only generate new metafiles, it does not version control. You need to `git commit` changes:
```
git commit -m "<YOUR-MESSAGE>"

# Can add tag to make it easy to refer back
git tag -a "data.v.20220727" -m "message here"
```
3. Now, we are ready to push new changed data to remote storage
```
dvc push
```

# Extra
> There is OUT OF SCOPE of this assignment, but you can try

## Init `dvc` repo

In case, you want to create a new git repo with `dvc`:
```bash
dvc init
```
Add the remote storage (could be s3, gs, Azure, Google Drive, or even local):
```bash
dvc remote add -d storage s3://<bucket>/<key>/
```

## Reuse data across repo

The benefit also comes from the fact that we could reuse and share the data files across the repo for different projects

1. Go to personal settings of Bitbucket, get App Password. Copy the Password (Token)
![](./images/git-app-pass.png)

2. Set credentials
```
export GIT_USERNAME=""
export GIT_TOKEN=""
```

3. Create a new folder in your laptop, and run this:
> Remember that you should have `dvc` and `dvc-gs` on the environment
```
dvc get --rev <tag|branch|commit-id> \
	-v https://${GIT_USERNAME}:${GIT_TOKEN}@bitbucket.org/maianhdang/analytics-training-samples.git \
	dvc-data/stories-sample.csv
```
Voila! Now, the datasets should be available on the directory that you are working.

4. To list all dvc data in a repo, run this:
```
dvc list -R --rev <tag|branch|commit-id> --dvc-only https://${GIT_USERNAME}:${GIT_TOKEN}@bitbucket.org/maianhdang/analytics-training-samples.git
```
