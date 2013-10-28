from time import time
import glob

all_files = glob.glob('2012-02-*.csv')

total_records = 0
record_v1 = 0
record_v2 = 0
record_v3 = 0
overall = 0

def vehicle_prcess(filename):
    vehicles = {"v1":0, "v2":0, "v3":0}  
    counter = 1
    f = open(filename)
    print('Processing file: ', filename, '...')

    start = time()

    for line in f:
        global total_records
        global record_v1
        global record_v2
        global record_v3
        global overall
        
        total_records += 1
        if line[len(line)-2:len(line)-1] == '1':
           vehicles["v1"] += 1
           record_v1 +=1
        elif line[len(line)-2:len(line)-1] == '2':
            vehicles["v2"] += 1
            record_v2 +=1
        else:
            vehicles["v3"] += 1
            record_v3 +=1

    end = time()
    overall += (end-start)
    print("Processing time: ", str(end-start), 'seconds')

    for vehicle in vehicles:
        print("Vehicle type ", str(counter), " --> ", vehicles[vehicle], 'counts')
        counter+=1
    print('------------------------------------------------')

for filename in all_files:
    vehicle_prcess(filename)

print("Processed files: ", len(all_files))
print("Processed records: ", total_records)
print("Processed vehicles:")
print("Vehicle type 1: ", record_v1)
print("Vehicle type 2: ", record_v2)
print("Vehicle type 3: ", record_v3)
print("Done in: ", overall, 'sec.')

a = input("Press enter to exit")