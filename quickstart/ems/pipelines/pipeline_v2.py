import ems

version_seed = "0001"

@ems.pipeline
def pipeline_flow(pipeline_name):
  """return a List of task"""
  kube_instance = ems.ComputationInstance(vcpus=1, gpus=0, memory=1, cloud_cmd="m-kube")
  ray_instance = ems.ComputationInstance(vcpus=1, gpus=0, memory=1, cloud_cmd="m-ray")

  flow = [
    ems.create_task(name="add", ver=pipeline_name, path="add", computation=kube_instance, deps={}),
    ems.create_task(name="minus", ver=pipeline_name, path="minus", computation=ray_instance, 
                    deps={"add": ems.Dep("add"),}),
  ]

  return flow
