c = get_config()
c.ServerApp.port = 8888
c.ServerApp.open_browser = False
c.NotebookApp.allow_origin = '*'
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.token = ''
c.NotebookApp.notebook_dir = '/root/workspace'
