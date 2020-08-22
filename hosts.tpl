[nodes] 
%{ for addr in ins_n ~}
${addr} ansible_connection=ssh  ansible_ssh_user=bhanucs2020   ansible_ssh_private_key_file=~/.ssh/google_compute_engine
%{ endfor ~}
[master] 
%{ for addr in ins_m ~}
${addr} ansible_connection=ssh  ansible_ssh_user=bhanucs2020   ansible_ssh_private_key_file=~/.ssh/google_compute_engine
%{ endfor ~}
