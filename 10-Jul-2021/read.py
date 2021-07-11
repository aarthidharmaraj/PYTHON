from configparser import ConfigParser
config = ConfigParser()
file='sample.ini'
config.read(file)

print(config.sections())
print(list(config['account']))


print("From account section Password - ",config['account']['passwd'])
print("From data section data -",config.get('datas','data'))

print('datas' in config)

print(config.getint('account','id'))

print(config.getboolean('bankdetails','client_number'))
#for updating

config.add_section('bankdetail')
config.set('bankdetail','Name','XYZ')
config.set('bankdetail','Branch','ABC')
config.set('bankdetail','IFSCcode','ABC000123')

with open(file,'w') as f1:
    config.write(f1)