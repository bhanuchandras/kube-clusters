import googleapiclient.discovery
from google.oauth2 import service_account
from flask import Flask, json
import os
import time

api = Flask(__name__)

#Globals
credentials = service_account.Credentials.from_service_account_file('./CREDENTIALS_FILE.json')
compute = googleapiclient.discovery.build('compute', 'v1',credentials=credentials)
project = "bhanu-k8s-proj"
zone = "asia-east1-a"
name = "vm-kube-master-0"
bucket = "bhanu-k8s-proj"

#Home
@api.route('/', methods=['GET'])
def home():
    return "Welcome,you are on!"

@api.route('/list', methods=['GET'])
def list_instances():
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else "No_items"

#Delete Instance
def delete_instance(compute, project, zone, instance):
    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=instance).execute()

#wait for deletion
def wait_for_operation(compute, project, zone, operation):
    print('Waiting for operation to finish...')
    while True:
        result = compute.zoneOperations().get(
            project=project,
            zone=zone,
            operation=operation).execute()
        if result['status'] == 'DONE':
            print("done.")
            if 'error' in result:
                raise Exception(result['error'])
            return "DELETE SUCCESSFUL"
        time.sleep(1)

@api.route('/delete/', methods=['GET'])
def main():
    instances = list_instances()
    output = ""
    if not instances=="No_items":
        for instance  in instances:   
          print instance
          operation = delete_instance(compute, project, zone, instance["id"])
          result = wait_for_operation(compute, project, zone, operation['name'])        
        print('Instances in project %s and zone %s:' % (project, zone))
        for instance in instances:
          print(' - ' + instance['name'] + instance["id"])
          output+=instance['name']+"||"+instance["id"]+"--"
        return output
    else:
        print("no Hosts present")
        return "No instances present"

if __name__ == '__main__':
    api.run(host='127.0.0.1', port=8001)
    
