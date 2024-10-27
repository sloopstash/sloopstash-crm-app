pipeline {
  agent any
  stages {
    stage('CI: Dowmnload Sources') {
      steps {
        sh '''rm -rf kickstart-docker
rm -rf kickstart-ansible
git clone https://github.com/sloopstash/kickstart-docker.git kickstart-docker
git clone https://github.com/sloopstash/kickstart-ansible.git kickstart-ansible'''
      }
    }

    stage('CI: Build OCI Images') {
      steps {
        sh '''cd kickstart-docker
sudo docker image build -t sloopstash/base:v1.1.1 -f image/base/1.1.1/amazon-linux-2.dockerfile image/base/1.1.1/context
sudo docker image build -t sloopstash/nginx:v1.14.0 -f image/nginx/1.14.0/amazon-linux-2.dockerfile image/nginx/1.14.0/context
sudo docker image build -t sloopstash/python:v2.7 -f image/python/2.7/amazon-linux-2.dockerfile image/python/2.7/context
sudo docker image build -t sloopstash/redis:v4.0.9 -f image/redis/4.0.9/amazon-linux-2.dockerfile image/redis/4.0.9/context

        '''
      }
    }

    stage('CI: Bootsrap testing environment') {
      steps {
        sh '''cd kickstart-docker
sudo docker compose -f compose/crm.yml --env-file compose/QAB.env -p sloopstash-QAB-crm up -d
sudo docker container exec sloopstash-QAB-crm-app-1 pip install pytest'''
      }
    }

    stage('CI: Execute test cases') {
      steps {
        sh 'sudo docker container exec --workdir ${APP_SOURCE} sloopstash-${qa2}-crm-app-1 pytest --junitxml=reports.xml script/test/main.py"'
        input 'App testing has been successful. Do you want to proceed deployment in staging environment?'
      }
    }

    stage('CD: Bootstrap staging environment') {
      steps {
        sh '''cd kickstart-ansible
sudo docker compose -f docker/compose/crm.yml --env-file docker/compose/STG.env -p sloopstash-stg-crm up -d --scale app=3 --scale nginx=2'''
      }
    }

    stage('CD: Execute deployment') {
      steps {
        sh '''cd kickstart-ansible
'''
        ansiblePlaybook(playbook: 'playbook/redis.yml', credentialsId: 'ansible-node-ssh', inventory: 'inventory/stg', tags: 'setup,config,stop,start')
        ansiblePlaybook(playbook: 'playbook/crm/app.yml', credentialsId: 'ansible-node-ssh', inventory: 'inventory/stg', limit: 'sloopstash-stg-crm-app-1', tags: 'setup,update,configure,stop,start')
        ansiblePlaybook(playbook: 'playbook/nginx.yml', credentialsId: 'ansible-node-ssh', inventory: 'inventory/stg', limit: 'sloopstash-stg-crm-nginx-1', tags: 'setup,update,configure,stop,start')
        input 'Deployment has been successful. Do you want to proceed deployment in production environment?'
      }
    }

  }
  environment {
    qa1 = 'qaa'
    qa2 = 'qab'
    APP_SOURCE = '/opt/app/source'
    ANSIBLE_CONFIG = '/opt/kickstart-ansible/ansible.cfg'
  }
}