# `elyra`: Notebook-to-Pipeline-as-Code

We have mentioned the pain of reproducing notebooks: order of running, dependencies, input/output, etc.

Sometimes, even ourselves confused when we have to run the series of notebooks again on new data inputs.

In this assignment, we will experiment with `elyra` a tool that enables as to visual edit pipeline from notebooks. 

- First of all, this gives us a clear functionalities of packaging multiple notebooks in one `*.pipeline` (JSON) file that we can share, reproduce and reuse notebooks
- This would be the first step to think about our codes as a pipeline 
- **Pipeline-as-a-code**: though it is very GUI-oriented, at the end `elyra` ouputs our pipeline as a code: `starter.pipeline` (`JSON` is also a code. You will see more and more tools and framework using `JSON`/`YAML` to describe everything-as-code)


## Install `elyra`
Docs: [elyra - installation](https://elyra.readthedocs.io/en/latest/getting_started/installation.html)
```
pip3 install --upgrade elyra
```

## Open jupyterlab
Elyra should be installed on your jupyterlab:
```
jupyter lab
```
Go to `02-reproducibility/elyra-assignment/`, open `starter.pipeline`, on the UI:

1. Run Pipeline (top menu). The UI will not show the progress, you can either check it on Terminal (where you start `jupyter lab`) or on the output cells of the notebook.
2. Right-click on each note, select `Open Properties`
3. Now, let's go to each notebook and read the code (it's simple)

> Source: Along the way, this elyra tutorial might be helpful [elyra - Intro to Generic Pipelines](https://github.com/elyra-ai/examples/tree/main/pipelines/introduction-to-generic-pipelines)


## Run `elyra` as CLI
Now, exit Jupyterlab. On the repo, you can run this command line to trigger the pipeline:

```bash
elyra-pipeline run 02-reproducibility/elyra-assignment/starter.pipeline
```

> We will appreciate anything offering CLI. As with CLI, we can automate (via cron, airflow, etc.)

# Assignment

Take some of your codes/notebooks in [Assignment#1](../../01-bigquery-notebooks/README.md) and refactor it into a pipeline.

With data outputs from your pipeline, use `dvc` to version them.

1. How things different comparing to your familiar way of working with notebooks?
2. How to make it more efficient?