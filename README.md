# README #

This is the content of tutorials and notebooks/code samples for analytics-training-hub:

- [Session 1: Lean Analytics - BigQuery & notebooks](./bigquery-notebooks/README.md): `2022-09-02`

### Git ###

1. Fork this repository to your personal Bitbucket workspace ("Fork" = producing a personal copy of someone else's project) 
2. Work and colab with Git. See: [Git-CLI Cheatsheets]('./cheatsheets/git-cli.md)


### How do I get set up? ###

1. Install Anaconda
2. Have an IDE (i.e. VSCode)
3. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
4. Make sure you have the [GCP service account](https://cloud.google.com/iam/docs/service-accounts) **credential json key** to programmatically access BigQuery (Ask your Admin). Put it on `credentials/`

3. Create Conda environments. See: [Conda-CLI Cheatsheets]('./cheatsheets/conda-cli.md)

```
conda create python=3.8 --name analytics-training-samples
conda activate !$
```

4. Install dependencies

```
pip install -r requirements.txt
```


### Flipped learning ###

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


### Rules ###
* You owns your progress, experience, and the outcomes 
* **Rewards**: NO. You learn for your skills and knowledge
* **Punishments**: NO. You learn for your skills and knowledge

