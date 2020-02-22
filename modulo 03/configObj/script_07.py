from configobj import ConfigObj


config = ConfigObj('config.conf')

print("status: {}".format(config["accesspoint"]["dhcp"]["Status"]))


config["accesspoint"]["dhcp"]["Status"]= "13meowmoe"


print(config["accesspoint"]["dhcp"]["Range"])

config.write()