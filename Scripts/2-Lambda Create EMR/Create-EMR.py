import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    # Configurar o cliente do Amazon EMR
    emr = boto3.client("emr",'us-east-1')

    
    # Definir as configurações do cluster
    cluster_config = {
        "Name": "Cluster EMR SSP",
        "ReleaseLabel": "emr-6.5.0",
        "Instances": {
            "InstanceGroups": [
                {
                    "Name": "Master nodes",
                    "Market": "SPOT",
                    "InstanceRole": "MASTER",
                    "InstanceType": "m5.xlarge",
                    "InstanceCount": 1,
                },
                {
                    "Name": "Worker nodes",
                    "Market": "SPOT",
                    "InstanceRole": "CORE",
                    "InstanceType": "m5.xlarge",
                    "InstanceCount": 2,
                },
            ],
            "Ec2KeyName": "INSIRA-SUA-CHAVE-AQUI",
            "KeepJobFlowAliveWhenNoSteps": True,
            "TerminationProtected": False,
        },
        "Applications": [{"Name": "Hadoop"}, {"Name": "Spark"},{"Name": "Ganglia"}, {"Name": "Jupyterhub"}],
        "VisibleToAllUsers": True,
        "JobFlowRole": "EMR_EC2_DefaultRole",
        "ServiceRole": "EMR_DefaultRole",
    }
    
    # Criar o cluster EMR
    response = emr.run_job_flow(**cluster_config)
    
    # Imprimir o ID do cluster EMR recém-criado
    print(f"Cluster EMR criado com sucesso. ID do cluster: {response['JobFlowId']}")