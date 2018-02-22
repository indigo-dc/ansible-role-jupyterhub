import os

c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'

c.JupyterHub.hub_connect_ip = os.environ['HUB_CONNECT_IP']

c.JupyterHub.allow_named_servers = True
