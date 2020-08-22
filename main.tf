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



resource "google_compute_instance" "kube-nodes" {
  machine_type = local.machine_id
  zone         = local.zone_id
  count	       = 2
  name 	       = "vm-kube-node-${count.index}"
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

  tags=["bhanu","poc","kube","centos","nodes"]
}
resource "google_compute_instance" "kube-master" {
  machine_type = local.m_machine_id
  zone         = local.zone_id
  count	       = 1
  name 	       = "vm-kube-master-${count.index}"
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

  tags=["bhanu","poc","kube","centos","master"]
}

output "instance_ips" {
  value = ["${google_compute_instance.kube-nodes[*].network_interface[0].access_config[0].nat_ip}"]
}
