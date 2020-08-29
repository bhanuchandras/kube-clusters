ad_addr: 35.206.214.244 
cidr_v: 172.16.0.0/16

packages:
- kubeadm
- kubectl

services:
- docker
- kubelet
- firewalld

ports:
- "6443/tcp"
- "10250/tcp"

user: ${user}

token_file: join_token
