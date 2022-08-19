# Conda CLI cheatsheet #

> There are many commands of Conda, and things could get complicated. Though, I find myself repeatly using the below commands. 

The list could be appended. For now, you might just be just fine only knowing the below Git commands:

### Basics ###

1. List all available environment
```
conda env list
```

2. Create new environment
```
conda create --name <env-name> python=3.x --yes
```

3. Conda activate a specific environment
```
conda activate <env-name>
```

4. Conda deactivate a specific environment
```
conda deactivate <env-name>
```

5. List all installed package and their version in the active environment
```
conda list
```

6. Delete an environment
```
conda env remove --name <env-name>
```
