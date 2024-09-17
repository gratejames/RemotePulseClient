# RemotePulse
*Welcome to the RemotePulse project!*  
RemotePulse is designed to be a simple server monitoring webservice built on flask and psutils that can provide detailed information about system stats such as memory, disk, CPU, and network usage.
Currently only general information is displayed in the GUI, though a process-specific tab is in the works.

## Client
The client is a simple webserver running on port 3546.  
It offers password protectiong by editing the Client/main.py file to adjust the 'users' dictionary and uncomment the `@auth.login_required` just before the main function.  
It serves the index.html file with your settings (config.json) injected into it rather lazily. A rework is in order, possibly by just leaving the user preferences hardcoded into the index.html file.  

## Server
The server runs on port 3545 and offers a simple API that make available system stats (from psutils) at a snapshot, as well as over a history.  
It can provide CORS, which accepts requests from all domain by default but can be changed to only accept requests from wherever your client is running.  
Currently the detailed process information is commented out while the frontend is prepared.

## Installation
For my setup, I put the client and server folders into /opt/RemotePulseClient and /opt/RemotePulseServer, and add a conf file into my /etc/apache2/sites-available/ folder that redirects a subdomain to the client subservice. Then I wrote some quick service files to allow them to run as daemons in the background, and allowed ports 3545 and 3546 for the client and server services.

## TODO
 + Write an installation script

## Done
 + Auto-update pages
