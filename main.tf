provider "google" {
 credentials = file("CREDENTIALS_FILE.json")
 project     = local.project_id
 region      = local.region_id
}

provider "google-beta" {
  credentials = file("CREDENTIALS_FILE.json")
  project     = local.project_id
  region      = local.region_id
}



resource "google_compute_instance" "default" {
  machine_type = local.machine_id
  zone         = local.zone_id
  count	       = 3
  name 	       = "vm-kube-bhanu-${count.index}"
  boot_disk {
	 initialize_params {
	     image = "centos-cloud/centos-7"
	   }
  }

  network_interface {
    network = "default"
    access_config {
      // Ephemeral IP
	network_tier ="STANDARD"
    }
  }

  tags=["bhanu","poc","kube","centos"]
}

output "instance_ips" {
  value = ["${google_compute_instance.default[*].network_interface[0].access_config[0].nat_ip}"]
}
