import os
import sys

def reload(project_name)
    os.system('systemctl daemon-reload')
    os.system('systemctl restart nginx')
    os.system('systemctl restart {}.service'.format(project_name))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        project_name = sys.argv[1]
        reload(project_name)
