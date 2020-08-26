# kube-clusters

Creating a working document on how to build the projects / Infrasture in GCP with different tooling.

While building any app or infra the basic components can be VM's or physical servers. At this moment GCP provides only VM on demand. Although cloud providers like Oracle/IBM provides Physicals as well.

As inital Step we can do use using Terraform create 3 VM's. This can be done by web UI or gcloud command line, but terraform give cloud abstraction, so that the same command can be used aganist google/AWS/Azure/oracle etc.

Step 1:

Once you clone the repo you repo on to your cloud shell you can run the following.
```
terraform init 
terraform plan 
terraform apply 
```
Which will create the VM's in project. once you create and explored on how it is done we can run
```
terraform destroy 
```
this will delete all the resources which we created. This can be done easily in terraform. without remembering what all are created. That is beauty of infra as code.

Post provisioning the VM's 
run

```
gcloud compute ssh <<VM NAM>>
```

which will ask for zone and then will create the ssh passprase. which we will be using for ansible configurations.

you need to update the ansible  ``` env_variable ``` file with your user id in the cloud sheell

post that you can run ansible-playbook command to spin the kubernetes clusters.

```
ansible-playbook pre-req.yaml master.yaml nodes.yaml
```


