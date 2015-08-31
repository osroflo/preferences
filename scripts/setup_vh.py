#!/usr/bin/python
# Automate Apache virtual host creation
import sys
import os
import time
import threading

semaphore = threading.Semaphore(4)

def createHost(hostname):
    semaphore.acquire()
    try:
       print '\nCreating Host...'
       hosts = open("/etc/hosts", "a")
       hosts.write("127.0.0.1       " + hostname + '\n')
    finally:
       semaphore.release()

def pingHost(hostname):
    response = os.system("ping -c 1 " + hostname)
    print '\n'

    if response == 0:
       print hostname, 'is up!'
    else:
       print hostname, 'is down!'

    print '\n'


def createVirtualHost(document_root, server_name):
    print 'Creating virtual host...'
    apache_sites_available_path = '/etc/apache2/sites-available/'
    site_conf = str(server_name + '.conf')

    vhost = '<VirtualHost *:80>'
    vhost += '\n\tServerName ' + server_name

    vhost += '\n\n\tServerAdmin webmaster@localhost'
    vhost += '\n\tDocumentRoot ' + document_root
    vhost += '\n\tServerAlias ' + server_name

    vhost += '\n\n\tErrorLog ${APACHE_LOG_DIR}/error.log'
    vhost += '\n\tCustomLog ${APACHE_LOG_DIR}/access.log combined'

    vhost += '\n\n\t<Directory ' + document_root + '>'
    vhost += '  \n\t\tOptions Indexes FollowSymLinks'
    vhost += '  \n\t\tAllowOverride All'
    vhost += '  \n\t\tRequire all granted'
    vhost += '\n\t</Directory>'
    vhost += '\n</VirtualHost>'

    conf_file = open(apache_sites_available_path + site_conf, "w")
    conf_file.write(vhost)
    conf_file.close()

    # enable site
    print '\nEnabling site...';
    os.system("a2ensite " + site_conf)
    os.system("service apache2 reload")


# Main execution
number_of_arguments = len(sys.argv)

if number_of_arguments > 2:
    document_root = sys.argv[1]
    server_name = sys.argv[2]

    threading.Thread(target=createVirtualHost(document_root,server_name), args=("sleep 1", )).start()
    threading.Thread(target=createHost(server_name), args=("sleep 1", )).start()
    threading.Thread(target=pingHost(server_name), args=("sleep 1", )).start()
else:
    print '\nApache virtual host creator\n'
    print 'Usage:'
    print '     sudo setup_vh' + ' [document root] [server name]'
