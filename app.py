# network and XML libraries
from jnpr.junos import Device
from lxml import etree

# environment libraries
from dotenv import load_dotenv
import os

# timestamp helper
from datetime import datetime

# allow us to pass parameters into the script
import getopt, sys

# help us perform some basic checks to see if a directory exists
from pathlib import Path

def load_variables():
    # load any variables that were passed through the .env file
    load_dotenv()

    username = os.environ.get('USERNAME')
    password = os.environ.get('PASSWORD')

    # return an object that has both username and password values
    return username, password


def write_to_file(network_config_text, hostname):
    # find out the current timestamp
    today = datetime.today()

    # Year / Month / Day / Hour / Minute (ex. 20210822_1923)
    todays_date = today.strftime("%Y%m%d_%H%M")

    # cleanup any hostname that has a decimal in the name (IPv4 address)
    if "." in hostname:
        hostname = hostname.replace(".", "_")

    # check to see if a directory for this host already exists
    hostname_path = Path(f'./backups/{hostname}')
    if hostname_path.is_dir() == False:
        hostname_path.mkdir(parents=True, exist_ok=True)

    # open a file with "append" mode and write the string
    network_config_file = open(f'./backups/{hostname}/{todays_date}.conf',"a")
    network_config_file.write(network_config_text)
    network_config_file.close()

    # check to make sure a file was written
    network_config_file = Path(f'./backups/{hostname}/{todays_date}.conf')
    if network_config_file.is_file() == True:
        print('\n' + '-' * 64)
        print(f'Configuration for {hostname} was written at:\n\tbackups/{hostname}/{todays_date}.conf')
        print('-' * 64 + '\n')
    else:
        print(f'Configuration for {hostname} was NOT written, check debug logs')


def get_hostname(argv):
    # create an empty string object to fill in below
    hostname = ""

    # try to see if there the hostname argument was passed with -h
    try:
        opts, args = getopt.getopt(argv, 'h:', ['hostname='])

    # if anything goes wrong with our argument check, fail the script
    except getopt.GetoptError:
        print('Something went wrong!')
        sys.exit(2)

    # loop over arguments passed, storing the key/value as opt/arg
    for opt, arg in opts:

        # if the -h (hostname) flag was thrown, save the value as 'hostname'
        if opt in ("-h", "--hostname"):
            hostname = arg

    # check to see if the hostname is empty and prompt the user
    if len(hostname) == 0:
        hostname = input("Please enter your device's hostname or IP address:\n")

    return hostname


if __name__ == "__main__":
    # load username and password variables
    username, password = load_variables()

    # find out if any arguments were passed into the script's execution
    hostname = get_hostname(sys.argv[1:])

    # create an object to reflect connection parameters
    network_device = Device(
                        host=f'{hostname}',
                        user=f'{username}',
                        password=f'{password}')

    # create an empty object to hold our configuration
    network_config = ""

    try:
        # open a connection to the device's NETCONF API
        network_device.open()

        # request the configuration back in the format of 'text'
        network_config_xml = network_device.rpc.get_config(
                                                    options={
                                                        'format':'text'
                                                    }
                                                )

        # close our connection to the NETCONF API
        network_device.close()

        # configuration is still an XML object, this will translate it into a string
        network_config_text = etree.tostring(
                                        network_config_xml,
                                        encoding='unicode',
                                        pretty_print=True
                                    )

        # print the configuration to the screen
        # print(network_config_text)

        # save file to local directory
        write_to_file(network_config_text, hostname)

    except ConnectError as err:
        print (f"Cannot connect to device: {network_device['host']}".format(err))

    except Exception as err:
      print (err)