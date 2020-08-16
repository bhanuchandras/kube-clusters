resource "local_file" "Inventory" {
content = templatefile("hosts.tpl",
	{
  	ins = "${google_compute_instance.default[*].network_interface[0].access_config[0].nat_ip}"
	})
	filename="inventory"
}
