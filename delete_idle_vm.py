import os
import time
import googleapiclient.discovery
from multiprocessing import Process
import multiprocessing as mp

res = []
compute = googleapiclient.discovery.build('compute', 'v1')
project=os.environ.get('project')
zone = os.environ.get('zone')

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

# [START close_host]
def close_host(instance):
    operation = delete_instance(compute, project, zone, instance)
    result = wait_for_operation(compute, project, zone, operation['name'])
    global res
    res.append(result['status'])
    return result['status']
# [END close_host]

# [START run]
def main(wait=True):
    output = ""    
    pool = mp.Pool(mp.cpu_count())
    print(mp.cpu_count())

    instances = list_instances(compute, project, zone)
    
    if instances != None:
        #parallelization
        instances_id = [i["id"] for i in instances]
        res = pool.map(close_host,instances_id)
        
        #parallelization + concurrency
        #for i in instances:
        #    p = Process(target=close_host, args=(i["id"],))
        #   p.start()
        
        print("Completed")
        print(res)
        return "|||".join(res)
        #return      
        # print('Instances in project %s and zone %s:' % (project, zone))
        # output=""
        # for instance in instances:
        #     print(' - ' + instance['name'])
        #     output+=instance['name']+"||"
    else:
        return f"No VM's Present in the Project now!"
