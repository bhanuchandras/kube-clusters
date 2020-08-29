locals {
  project_id   = "bhanu-k8s-proj"
  region_id    = "asia-east1"
  zone_id      = "asia-east1-a"
  machine_id   = "g1-small"
  m_machine_id   = "e2-standard-2"
  owner        = "BhanuChandra"
  user        = "bhanuchandra.sabbavarapu"
}
variable "username" {
  type        = string
  description = "The id of the machine image (AMI) to use for the server."
}

