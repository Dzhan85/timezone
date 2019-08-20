# timezone

## Github Deployment



## Docker deployment

1. Creating docker image with application and testing it.

```
docker build -t flaskclock .
```
Run it and expose port:
```
docker run -d -p 80:5000 flaskclock
```
2. Created Docker hub image to further deployment.
https://cloud.docker.com/u/kurbik/repository/docker/kurbik/clock

## Ansible deployment

Before need to generate SSH Pub keys and copy to host machine to - authorized_keys.  

1. Installing Python on hosts and server machines.

```
apt-get install -y python3 python3-dev python3-pip
```

2. Installig Ansible  on the server:

  ```
  sudo apt install ansible
  
  ```
or

Installing Ansible-galaxy:
```


ansible-galaxy install hypebeast.flaskapp
```
```
root@test-Book:/home/test/Desktop/LIALAB/timezone# ansible-galaxy install hypebeast.flaskapp
- downloading role 'flaskapp', owned by hypebeast
- downloading role from https://github.com/hypebeast/ansible-flask-stack/archive/master.tar.gz
- extracting hypebeast.flaskapp to /root/.ansible/roles/hypebeast.flaskapp
- hypebeast.flaskapp (master) was installed successfully

```

2. Configuring location of hosts and its IP addresses:


```
sudo vim /etc/ansible/hosts 
```
2.1 Creating group:
```
[webserver]

host1 ansible_host=34.245.176.15

```

2.2 Testing ping to host:

```
root@test-Book:/home/test/Desktop/LIALAB/timezone# ansible -m ping all
host1 | SUCCESS => {
    "ansible_facts": {
        "discovered_interpreter_python": "/usr/bin/python3"
    }, 
    "changed": false, 
    "ping": "pong"
}

```
ansible -m shell -a 'free -m' host1
```
root@test-Book:/home/test/Desktop/LIALAB/timezone# ansible -m shell -a 'free -m' host1
host1 | CHANGED | rc=0 >>
              total        used        free      shared  buff/cache   available
Mem:           7625         150        5822           0        1651        7179
Swap: 
```


3. Creating Ansible playbook:

3.1 Creating deploy.yml file

```

```

3.2



