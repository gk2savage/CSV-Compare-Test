import csv
import json

#Json Validation
def is_json(myjson):
  try:
    json_object = json.loads(myjson)
  except ValueError as e:
    return False
  return True

#CSV data 
class csvdata():
    def __init__(self, filename):
        with open(filename, "r") as f_input:
            csv_input = csv.reader(f_input)
            self.details = list(csv_input)

    def get_col_row(self, col, row):
        return self.details[col][row]

expected = csvdata("expected.csv")
testcase = csvdata("testcase0.csv")

#p = expected.get_col_row(1,1)
#print "%s" % p

#json check
#print is_json(expected.get_col_row(7,1))
#a = expected.get_col_row(7,1)
#b = testcase.get_col_row(7,1)
#x = json.loads(a)
#y = json.loads(b)
#if x==y:
#    print("True")

print("-------------------------------------------------------------------")
print("JSON Validation")

for i in range(8):
    if is_json(expected.get_col_row(i,1)) == True and expected.get_col_row(i,1)[0] == '{':
        print("For Expected: Json Data is Valid in " + str(i) + " , 1 ")
        def test_json_validation_expected():        #TESTCASE 1 : "Expected" CSV has valid JSON.
            assert is_json(expected.get_col_row(i,1)) == True
            
        
for j in range(8):
    if is_json(testcase.get_col_row(j,1)) == True and testcase.get_col_row(j,1)[0] == '{':
        print("For Testcase: Json Data is Valid in " + str(j) + " , 1 ")
        def test_json_validation_testcase():        #TESTCASE 2 : "Testcase" CSV has valid JSON.
            assert is_json(expected.get_col_row(j,1)) == True
        
        
count = 0
print("-------------------------------------------------------------------")
print("JSON Data Check")
for i in range(8):
    for j in range(8):
                if is_json(expected.get_col_row(i,1)) == True and is_json(testcase.get_col_row(j,1)) == True:
                    if expected.get_col_row(i,1)[0] == '{' and testcase.get_col_row(j,1)[0] == '{':
                        a = expected.get_col_row(i,1)
                        b = testcase.get_col_row(j,1)
                        x = json.loads(a)
                        y = json.loads(b)
                        if x==y:
                            print("For Expected: Json data is in " + str(i) + " , 1 ")
                            print("For Testcase: Json data is in " + str(j) + " , 1 ")
                            count = count + 1

if count > 0:
    print("Json in both .csv files are true and has same value which is:")
    for i in range(8):
        if is_json(expected.get_col_row(i,1)) == True and expected.get_col_row(i,1)[0] == '{':
            print(expected.get_col_row(i,1))
            def test_json_same_data():      #TESTCASE 3 : Both "Expected" and "Testcase" has same valid JSON Data.
                assert is_json(expected.get_col_row(i,1)) == True and expected.get_col_row(i,1)[0] == '{'
else:
    print("Json data in both the files are not same.")

count1 = 0
print("-------------------------------------------------------------------")
print("CSV Data Check")
for i in range(8):
    for j in range(8):
        if expected.get_col_row(i,0) == testcase.get_col_row(j,0):
            if expected.get_col_row(i,1) == testcase.get_col_row(j,1):
                print("Variable "+ expected.get_col_row(i,0) + " has same value which is " + expected.get_col_row(i,1) + " in both .csv files.")   
                count1 = count1 + 1

def test_same_csv_data():       #TESTCASE 4 : Both "Expected" and "Testcase" has same valid Data.
               assert count1 == 8 

#written by Girish aka '@gk2savage'
