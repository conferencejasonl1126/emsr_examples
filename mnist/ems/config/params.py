"""Exepriment configs."""
import dataclasses

@dataclasses.dataclass
class ParamsConfig:
  """Data class containing config for experiments."""
  batch_size: float = 4
  test_batch_size: int = 64
  epochs: int = 14
  lr: float = 1.0
  gamma: float = 0.7
  no_cuda: bool = False
  dry_run: bool = False
  seed: int = 1234
  log_interval: int = 10
  save_model: bool = True
  
