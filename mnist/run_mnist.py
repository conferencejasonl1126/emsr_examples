import ems

def main():
  # Define list of configuration, each configuration is a configuration files
  search_space = [ 
  { "params":{"batch_size": 64, "lr": 1.0, "seed": 1234}, }, 
  { "params":{"batch_size": 64, "lr": 0.8, "seed": 1234}, }, 
  { "params":{"batch_size": 128, "lr": 1.0, "seed": 1234}, }, 
  ]
  pipeline_dag = "pipeline_v4"

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
  return

if __name__ == "__main__":
  main()

