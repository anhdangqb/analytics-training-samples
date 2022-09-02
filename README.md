# README #

[<img src="https://deepnote.com/buttons/launch-in-deepnote.svg">](https://deepnote.com/launch?url=https://github.com/anhdangqb/analytics-training-samples)

Notebooks and code samples for analytics flipped-learning tutorials. This codified my enthusiasm for continuous learning, exploring, and refining my mindset, skillet, toolset as a data practitioner:

### 🚩 Contents ###

- [Session 1: Lean Analytics - BigQuery & notebooks](./bigquery-notebooks/README.md): `2022-08-31`
- [Session 2: Reproducibility - `dvc` & `elyra`](./02-reproducibility/README.md): `2022-09-16`

### 💡 How to use this repo ###

This repo is a collection of notebooks and code samples for analytics flipped-learning tutorials. The contents are organized by session, I recommend to take them in the numbering orders, because the latter will be related and most of the times reusing the output of previous session. 

You can [Fork the repo](#fork-and-fit), follow instructions in [How to set up?](#how-to-set-up).

Then, you are ready!

For each session:

1. Read the README.md files: give the context, and links to assignment and solutions
2. Highly recommend to work on the assignment by yourself first (the guidance is given along the way to help you solve it)
    - Tag for each assignment: `ass.v<major>.<minor>.<fix>` 
    - Tag for each solution: `sol.v<major>.<minor>.<fix>`
    - You can checkout by tags and work from any checkpoint. See [Git-CLI Cheatsheets](./cheatsheets/git-cli.md)
3. Then, you can refer to the solutions (this is only to give you a common frame of reference)
    - It's important to just read the code (and understand)
    - Run line by line and see the output
    - Understand the structure of code as a whole
4. Continue to work on the frame of solutions
    - Modify, add more complexity, customize it your own way
    - Optimize or fix any issue/typos
    - If you want, contribute your work to this repo. See: [CONTRIBUTION](#contribution)



### 🚧 Fork and Git ###

1. Fork this repository to your personal Bitbucket workspace ("Fork" = producing a personal copy of someone else's project) 
2. Work and colab with Git. See: [Git-CLI Cheatsheets](./cheatsheets/git-cli.md). Related topics that you would need to use:

    - Work with fork repository
    - Checkout by tags versions of assignments/solutions 

```
git checkout tags/ass.v1.0.1 -b ass-1
```


### 📥 Contribution ###

If you find any issue/problem, when working with the repo, please raise the issue. 

Even better, you can fix/modify/add (typos, better rephrase of the docs, better solutions, etc.) from your fork repository and contribute back to the original repo.

> See: [CONTRIBUTION.md](./CONTRIBUTION.md)


### 📦 How to set up? ###

1. Install Anaconda (or miniconda)
2. Have an IDE (i.e. VSCode)
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Make sure you have the [GCP service account](https://cloud.google.com/iam/docs/service-accounts) **credential json key** to programmatically access BigQuery (Ask your Admin). Put it on `credentials/`

3. Create Conda environments. See: [Conda-CLI Cheatsheets](./cheatsheets/conda-cli.md)

```
conda create python=3.x --name analytics-training-samples
conda activate !$
```

4. Install dependencies

```
pip install -r requirements.txt
```


### 🍰 Flipped learning ###

> To maximize the gain of our time and customize the experience for learners from diversed backgrounds, we will practice **"Flipped Learning"** 

* Every 2-week, there would be a new **assignment**. Don't be panic! The guidances and helpful materials would be given.
* You will use the guidance (and Google, and StackOverflow, etc.) to solve all questions in the assignment
* Study group, team work, idea exchange are welcomed!
* **Check-in**: We will have 1 Friday session (mid-point) that I will be available to help (1-1 or group meeting). 
    * Discuss any question related to the assignment
    * If you have code, you can bring, we can review code together
    * You can ask any other questions related to DS, industry, etc.

> The idea is after completing the assignment, you have known anything you need to know about the topics.

* After 2-week, we will have a training session (which has nothing new). We use the session to reinforce what you have learnt through the assignment, retrospectives about different approaches
* After training session, you could come and polish the assignment 

The loop repeats!


### 🚨 Rules ###
* You owns your progress, experience, and the outcomes 
* **Rewards**: NO. You learn for your skills and knowledge
* **Punishments**: NO. You learn for your skills and knowledge


### 📝 Materials ###
- [DATAcracy](https://anhdang.gitbook.io/datacracy/)
- [DATAcracy - ATOM class repo](https://github.com/anhdanggit/atom-assignments)
- [Lean Analytics - Readings and code samples](https://publish.obsidian.md/danghuynhmaianh/00-Work/Lean-Analytics/Tutorials/5-Analytics+Frameworks) - Pass: `danghuynhmaianh`
- If you are not familiar with Python, please take these (by orders):
    - [Kaggle Python](https://www.kaggle.com/learn/python)
    - [Kaggle Pandas tutorial](https://www.kaggle.com/learn/pandas)
    - [Kaggle Pandas Data cleaning tutorial](https://www.kaggle.com/learn/data-cleaning)
    - [Kaggle Seaborn Data Viz tutorial](https://www.kaggle.com/learn/data-visualization)
- If you are not confident with your Python, practice make perfect. This is an amazing place: [Exercism.org](https://exercism.org/tracks/python)

