import ems
import torch 

@ems.task
def main(config, *args):
  a = config.params.a
  b = config.params.b  

  score = - (a ** 2 + b)

  # test cuda device
  c = torch.tensor([1., 2.]).cuda()
  print("Cuda available:", torch.cuda.is_available(), torch.cuda.device_count())
  print("Cuda tensor:", c)

  return {"minus_score":score}

if __name__ == "__main__":
  main()