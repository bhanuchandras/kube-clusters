[server] 
%{ for addr in ins ~}
${addr} ansible_connection=ssh  ansible_ssh_user=bhanucs2020   ansible_ssh_private_key_file=~/.ssh/google_compute_engine
%{ endfor ~}
