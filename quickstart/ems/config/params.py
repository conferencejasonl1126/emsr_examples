"""Exepriment configs."""
import dataclasses

@dataclasses.dataclass
class ParamsConfig:
  """Data class containing config for experiments."""
  a: int = 2
  b: int = 1