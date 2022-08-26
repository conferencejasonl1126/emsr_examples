# EMS Client documentation

## APIs in Run.py 

* [run_configurations()](#run_configurations)

* [get_results()](#get_results)

* [get_best_config()](#get_best_config)


## APIs in task definition

* [task](#task)
* [report_metric()](#report_metric)


## APIs in pipeline definition

* [pipeline](#pipeline)
* [create_task()](#create_task)
* [ComputationInstance()](#computationinstance)
* [Dep()](#dep)


## run_configurations()

  Given search space and pipeline DAG, this function runs pipelines paralelly, with each configuration in search space.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.run_configurations(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
  )
  ```

  **Parameter**
    
  * pipeline_dag (string)[Required] 

    The python file name of your pipeline dag definition.

  * search_space (List of Dict)[Required]
    
    The configuration value list. Each element in the list is a dictionay, where the key value is `params`. The `params` maps to a dictionary containing the experimental parameter keys names and values. 

  **Return Type**

  &emsp;None


## get_results()


  Given search space and pipeline DAG, this function return the reported metric in all run pipelines.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.get_results(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
  )
  ```

  **Parameter**
    
  * pipeline_dag (string)[Required] 

    The python file name of your pipeline dag definition.

  * search_space (List of Dict)[Required]
    
    The configuration value list. Each element in the list is a dictionay, where the key value is `params`. The `params` maps to a dictionary containing the experimental parameter keys names and values. 

  **Return Type**

  &emsp;List of Dict.

  &emsp;**Return Syntax**
  ```ruby
  [{"score":1},{"score":20},{"score":0}]
  ```

## get_best_config()

  Given search space and pipeline DAG, this function return best configuration, with the minimum or maximum reported metric value.

  **Usage Syntax**

  ```ruby
  search_space = [ 
  { "params":{"a": 0, "b": 1,}, }, 
  { "params":{"a": 0, "b": 20,}, },
  { "params":{"a": 1, "b": 10,}, },
  ]
  pipeline_dag = "pipeline_v2"

  # Run experiments
  ems.get_best_config(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
    metric = "score",
    mode = "min",
  )
  ```

  **Parameter**
    
  * pipeline_dag (string)[Required] 

    The python file name of your pipeline dag definition.

  * search_space (List of Dict)[Required]
    
    The configuration value list. Each element in the list is a dictionay, where the key value is `params`. The `params` maps to a dictionary containing the experimental parameter keys names and values. 

  * metric (string)[Required] 

    The key value name of reported metric dictionary in the pipelines.

  * mode (string)[Required] 

    min or max. Currently only support minimum mode and maximum mode.

  **Return Type**

  &emsp;Dict.

  &emsp;**Return Syntax**
  ```ruby
  { "params":{"a": 0, "b": 1,} }
  ```

## report_metric()

  Report metric in the task. For example, developer can report training loss in training loops.

  **Usage Syntax**

  ```ruby
  @ems.task
  def main(config, args):
    a = config.params.a
    b = config.params.b
    score = a ** 2 + b

    ems.report_metric(
      report_result={"score":score},
      result_path=args.config_result_path
    )
    return 

  if __name__ == "__main__":
    main()
  ```

  **Parameter**
    
  * report_result (Dict)[Required] 

    A dictionary of reported keys and values. 

  * result_path (String)[Required]
    
    A file path, given from `args` input.

  **Return Type**

  &emsp;None

## ComputationInstance()

  Computation resource specification. It contain cpu number, gpu number and memory size.

  **Usage Syntax**

  ```ruby
  gpu_instance = ems.ComputationInstance(vcpus=15, gpus=1, memory=15, gpu_type="tesla_t4", cloud_cmd="m-batch")
  ```

  **Parameter**
    
  * vcpus (Int)[Required] 

    The number of cpu.

  * gpus (Int)[Required]
    
    The number of the gpu.

  * memory (Int)[Required]
    
    The memory size, based on Gi. 

  * gpu_type (str)[Optional]
    
    The type of the gpu. Only support tesla_t4, tesla_a100, tesla_v100

  * cloud_cmd (str)[Optional]
    
    The type of the cluster. Only support m-kube, m-ray, m-batch

  **Return Type**

  &emsp;ems.ComputationInstance


## create_task()

  Create a task in the pipeline flow. Developer can specify the executed module name, version number, task dependency and computation resource. 

  **Usage Syntax**

  ```ruby
  cpu_instance = ems.ComputationInstance(vcpus=15, gpus=0, memory=15)
  
  flow = [ems.create_task(name="add", ver=pipeline_name, 
    path="add", computation=cpu_instance, deps={}),]
  ```

  **Parameter**
    
  * name (String)[Required] 

    Name of the task. It is used when specifying depdendency.

  * ver (String)[Required] 

    A version string of the task. It can be `pipeline_name`. For example, if task is for training model and evaluating model, it would better be  `pipeline_name`. If given a random string, it means the task is shared among different pipelines. For example, if preprocess task is preprocessing the same raw data for all pipeline, it should be executed once and preprocess resulted can be used for all other pipelines. Then the `ver` of this task can be a random string but not `pipeline_name`.

  * path (String)[Required] 

    The file path to an executable python module. The path should be relative path to the `tasks` folder. 

  * computation (ComputationInstance)[Required]
    
    The computation resource including cpu number, gpu number and memory size for the task.

  * deps (Dict)[Required]
    
    The dependency of the task. For example,`deps={"train": ems.Dep("mnist/train"),})`.

  **Return Type**

  &emsp;ems.Task, but not ems.task decrator.


## Dep()

  A task Dependency. It should be used in the create_task() function.

  **Usage Syntax**

  ```ruby
  ems.create_task(name="mnist/train", ver=pipeline_name, path="mnist/train", 
      computation=gpu_instance, deps={}),
  ems.create_task(name="mnist/eval", ver=pipeline_name, path="mnist/eval", 
      computation=gpu_instance, deps={"train": ems.Dep("mnist/train"),}),
  ```

  **Parameter**
    
  * name (string)[Required] 

    The name of the dependency task.

  **Return Type**

  &emsp;ems.Dep

## task

  task decrator should be used in task entrypoint function.

  **Usage Syntax**

  ```ruby
  import ems

  @ems.task
  def main(config, args):
    a = config.params.a
    b = config.params.b

    score = a ** 2 + b
    return {"score":score}

  if __name__ == "__main__":
    main()
  ```

  **Parameter**
    
  * config (dataclass)[Required] 

    The dataclass containing the configuration values.

  * args (argparser)[Required] 

    Several important argument is parsed in the `args`. `args.task_result_path` and `args.{dependency_task_name}` are two important arguments in experiments. These two arguments are list of string. Specifically,  `args.task_result_path[0]` is the folder for saving task generated result. For example use should save trained model in `args.task_result_path[0]`. If the a model training task (name=A) is depending on a data preprocess task(name=B). Then task A can get result from task B by reading files in the `args.B[0]` folder.

  **Return Object**

  &emsp;Dict. The return object is the reported metric. 


## pipeline

  The pipeline decrator should be used in the pipeline DAG python file.

  **Usage Syntax**

  ```ruby
  import ems

  version_seed = "0001"

  @ems.pipeline
  def pipeline_flow(pipeline_name):
    cpu_instance = ems.ComputationInstance(vcpus=15, gpus=0, memory=15)
    flow = [ems.create_task(name="add", ver=pipeline_name, 
      path="add", computation=cpu_instance, deps={}),]
    return flow
  ```

  **Parameter**
    
  * pipeline_name (String)[Required] 

    The unified version of pipeline name. With the same configuration and pipeline DAG file name, the `pipeline_name` is the same. This is used for configuration management.

  **Return Object**

  &emsp;List of ems.Task. 
