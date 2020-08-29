resource "local_file" "Inventory" {
content = templatefile("hosts.tpl",
	{
  	ins_n = "${google_compute_instance.kube-nodes[*].network_interface[0].access_config[0].nat_ip}"
  	ins_m = "${google_compute_instance.kube-master[*].network_interface[0].access_config[0].nat_ip}"
  	user = var.username
	})
	filename="inventory"
}
resource "local_file" "env_var" {
content = templatefile("var.tpl",
	{
  	user = var.username
	})
	filename="env_variables"
}
