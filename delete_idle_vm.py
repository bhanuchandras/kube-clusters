import os
import time
import googleapiclient.discovery
from google.oauth2 import service_account


# [START list_instances]
def list_instances(compute, project, zone):
    result = compute.instances().list(project=project, zone=zone).execute()
    return result['items'] if 'items' in result else None
# [END list_instances]


# [START delete_instance]
def delete_instance(compute, project, zone, name):
    return compute.instances().delete(
        project=project,
        zone=zone,
        instance=name).execute()
# [END delete_instance]


# [START wait_for_operation]
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
            return result

        time.sleep(1)
# [END wait_for_operation]


# [START run]
def main(project, bucket, zone, instance_name, wait=True):
    credentials = service_account.Credentials.from_service_account_file('./CREDENTIALS_FILE.json')
    compute = googleapiclient.discovery.build('compute', 'v1',credentials=credentials)
    instances = list_instances(compute, project, zone)
    if instances is not None:
      for instance  in instances:
        operation = delete_instance(compute, project, zone, instance["id"])
        wait_for_operation(compute, project, zone, operation['name'])        

      print('Instances in project %s and zone %s:' % (project, zone))
      for instance in instances:
        print(' - ' + instance['name'] + instance["id"])
        output+=instance['name']+"||"+instance["id"]+"--"
      return output
    else:
      print("no Hosts present")
      return "None instances present"

# [END run]


if __name__ == '__main__':
    main("bhanu-k8s-proj", "bhanu-k8s-proj", "asia-east1-a", "vm-kube-master-0")
