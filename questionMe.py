###############################################################################
# Program Name : Question Me
# Version      : 0.1
# Author       : Anoop
# Created On   : Jul 11, 2015
# Last Updated : Jul 11, 2015
#
# Change History
# [Anoop] Jul 11, 2015 : File Created
#
###############################################################################

import sys;
import optparse;
import socket;

def main():
  arguments = sys.argv;
  try:
    task = arguments[1];
    validateTask(task);
  except:
    usage();
    exit(0);
  
  try:
    validateTaskArguments(task);
  except:
    usage();
    exit(0);

  output = executeTask(task);  
  
  print output;

  return;



#################################
# Validate if task is supported
# Throws exception if task is not supported
#################################

def validateTask(task):
  if task in getAllTasks():
    return;
  else:
    raise Exception('Invalid Task');



#################################
# Validate if task has valid options
# Throws exception if task options are not supported
#################################

def validateTaskArguments(task):
  parser = getOption(task);
  try:
    (options, args) = parser.parse_args();
  except:
    usage();
    exit(0);


#################################
# Get the task options
# Return the valid options
#################################

def executeTask(task):
  parser = getOption(task);
  (options, args) = parser.parse_args();
  if task == 'getHostIP':
    output = getHostIP(options, args);
  elif task == 'getHostName':
    output = getHostName(options, args);

  return output;

#################################
# Get the Host IP address 
# Return the IP address
#################################

def getHostIP(options, args):
  return socket.gethostbyname(options.tgtHostName);


#################################
# Get the Host Name 
# Return the Host Name
#################################

def getHostName(options, args):
  return socket.gethostbyaddr(options.tgtHostIP);

#################################
# Get the task oprions
# Return the valid options
#################################

def getOption(task):
  if task == 'getHostIP':
    parser = optparse.OptionParser('usage %prog getHostIP -H <target host(s)>');
    parser.add_option('-H','--host',dest='tgtHostName',type='string', help='Enter Host Name');
  elif task == 'getHostName': 
    parser = optparse.OptionParser('usage %prog getHostName -H <target IP address(es)>');
    parser.add_option('-H','--host',dest='tgtHostIP',type='string', help='Enter Host IP');

  return parser;

#################################
# Print the usage of program
# List down all the tasks supported
#################################

def usage():
  print 'usage questionMe.py <task name> <task options>';
  print printAllTasks();



#################################
# Print all the tasks supported
#################################
def printAllTasks():
  tasks = getAllTasks();
  print '\n---------Supported Tasks --------------';
  for task in tasks:
    print task;


#################################
# Get all the tasks supported
#################################
def getAllTasks():
  tasks = [];
  tasks.append('getHostIP');
  tasks.append('getHostName');
  
  return tasks;


#---------------------------Main Function Call -------------------------------

if __name__ == "__main__":
  main()
