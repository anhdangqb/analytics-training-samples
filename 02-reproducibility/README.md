# Reproducibility: `dvc` and `elyra` #

The good news is the assigment of this time is lighter than the previous one [01-bigquery-notebook](../01-bigquery-notebooks/README.md).

In the last assignment, you have moved from working on `BigQuery UI` to notebook, though it might feel uncomfortable at first, the benefits will become clearer over time. Now, you have been able to:

- Programmatically parse SQL strings and convert BigQuery common queries into functions for the benefit of **reusabibilty**
- **Hybrid**: more freedom and variety in tools: SQL, Python, pandas, ducks and others to create a powerful and flexible workbench for your data tasks
- **Versioning**: you can easily track changes of your notebooks (SQL, Python codes, outputs) and share them with other data co-workers or stakeholders

From the last assignment, more or less, you have built *a simple yet end-to-end data pipeline* (which could be very potential to reuse multiple times or even put into production). For the next several sessions, we could focus on that simple and core pipeline, making it more elegantly organized, more efficient, convenient and sustainable with the introduction of other tools and frameworks.

This assignment will focus on the next component of *"Best practices"*: **Reproducibility**.


## 🚩 Assignments ##

- [dvc-assignment](./dvc-assignment.md)
- [elyra-assignment](elyra-assignment/elyra-assignment.md)

## 💡 Discussions ##
> This is sharing. You DO NOT need to prepare anything in advance. Just share the current way you work.

1. Have you ever been stuck with a hand-over repo from someone else with multiple data files (you have no clue, which one to use), and multiple notebooks (you have no clue, which one to run first)?
2. Have you ever handed over the same repo as (1) to someone else?
3. How to improve the data tracking/sharing (that we know which version to use, and timely update the lastest version)?
4. How to explain others how to run your series of notebooks?

## 📝 References ##
* [dvc - Data and Model Versioning](https://dvc.org/doc/use-cases/versioning-data-and-model-files/tutorial)
* [Elyra - Run generic pipelines in Jupyterlab](https://github.com/elyra-ai/examples/tree/main/pipelines/introduction-to-generic-pipelines) 