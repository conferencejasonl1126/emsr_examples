import ems

def main():
  # Define list of configuration, each configuration is a configuration files
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

  # Get experiment results
  results = ems.get_results(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
  )
  print("Reported metrics",results)

  # Analyze results
  best_config = ems.get_best_config(
    pipeline_dag = pipeline_dag,
    search_space = search_space,
    metric = "score",
    mode = "min",
  )
  print("Best config:",best_config)

  return

if __name__ == "__main__":
  main()

