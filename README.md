Installs the JupyterHub server.
===============================================

Installs the JupyterHub server

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows.

	# Set the Spawner to use. Currently suported: local, kubernetes
	jupyterhub_spawner: local
	# Volumes to mount to the container
	# Do not remove this one.
	volumes: ["/etc/jupyterhub_config.py:/jupyterhub_config.py"]
	# Add users for local spawner
	# password is encrypted as expected in useradd command
	users: 
	  - {"name": "user1", "password": "FxbYqKrYALWHo"}
	  - {"name": "user2", "password": "FxbYqKrYALWHo"}

Example Playbook
----------------

This an example of how to install the application:

```yml
  roles:
    - { role: 'indigo-dc.jupyterhub' }
```

License
-------

Apache Licence v2 [1]

[1] http://www.apache.org/licenses/LICENSE-2.0
