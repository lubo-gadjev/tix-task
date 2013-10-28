from time import time
import glob

def print_msg(msg):
    print(msg)

def vehicle_prcess(filename):
    vehicles = [0,0,0]  
    counter = 1
    f = open(filename)
    print_msg('Processing file: %s' % filename+ '...')

    start = time()

    for line in f:
        global total_records
        global record_v1
        global record_v2
        global record_v3
        global overall
        
        total_records += 1
        if line[len(line)-2:len(line)-1] == '1':
           vehicles[0] += 1
           record_v1 +=1
        elif line[len(line)-2:len(line)-1] == '2':
            vehicles[1] += 1
            record_v2 +=1
        else:
            vehicles[2] += 1
            record_v3 +=1

    end = time()
    overall += (end-start)
    print_msg("Processing time: "+str(end-start)+'seconds')

    for vehicle in vehicles:
        print("Vehicle type ", str(counter), " --> ", vehicle, 'counts')
        counter+=1
    print_msg('------------------------------------------------')

all_files = glob.glob('2012-02-*.csv')

total_records = 0
record_v1 = 0
record_v2 = 0
record_v3 = 0
overall = 0

for filename in all_files:
    vehicle_prcess(filename)

print_msg("Processed files: %s" % len(all_files))
print_msg("Processed records: %s" % total_records)
print_msg("Processed vehicles:")
print_msg("Vehicle type 1: %s" % record_v1)
print_msg("Vehicle type 2: %s" % record_v2)
print_msg("Vehicle type 3: %s" % record_v3)
print_msg("Done in: %s" % overall+'sec.')

a = input("Press enter to exit")