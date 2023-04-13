# Overview
Generate CloudFormation for Lambda to be used with Serverless Framework.

# Preparation

```shell
pdm install
```

# Example

```shell
export FUNC_PATH='functions'
export SUFFIX='.js'
export SLS_FUNC_PATH='functions'
export PREFIX='ServiceName'
pdm run python3 index.py
```

After execution, export.yml is generated.
