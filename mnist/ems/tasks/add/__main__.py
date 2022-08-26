import ems

@ems.task
def main(config, args):
  a = config.params.a
  b = config.params.b

  score = a ** 2 + b

  print("*"*20)
  print(args.task_result_path)
  
  return {"score":score}

if __name__ == "__main__":
  main()