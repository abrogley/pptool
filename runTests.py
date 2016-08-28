test_list = [
    'UT_Airport.py',
    'UT_AirportManager.py',    
    ]

for item in test_list:
    test_item = 'test/' + item
    exec(open( test_item ).read())

# This runs ALL the tests in test_list
if __name__ == "__main__":
    unittest.main() # run all tests