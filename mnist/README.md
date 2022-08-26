# EMS Client Documentation
![](./docs/overview-16.png)


## Mnist example

We use a pytorch example of trainng mnist dataset, [link](https://github.com/pytorch/examples/blob/main/mnist/main.py). For using it with ems, we need to do folllowing modifications.

  1. delete argsparser, 

  2. replace argsparse argument by params.py
  
  3. replace argsparser as config.params in the `__main__.py`

Then, we use following command to run it.

```
ems-run --client_name="client2" --entrypoint="python run_mnist.py"
```


## EMS Files Tree

To use EMS to seach the space for good values, we need to implement several files. The file tree looks like this

```
├── ems
│   ├── config/params.py
│   ├── tasks/mnist/train/__main__.py
│   ├── tasks/mnist/eval/__main__.py
│   └── pipelines/pipeline_v4.py
├── run_mnist.py
```

## More

## APIS

Detailed API documentation is in [link](docs/API.md).

