pip install faker

from decimal import Decimal
import pytest
import session8
import inspect
import os
import re 
from time import perf_counter


README_CONTENT_CHECK_FOR = [
    'namedtuple',
    'profile_feature_generator_namedtuple',
    'profile_feature_generator_dictionary',
    'company_profile_generator'
]

def test_session8_readme_exists():
    '''Test to check if the README.md file has been created and stored in close vicinity'''
    assert os.path.isfile("README.md"), "Found README.md file!"


def test_session8_readme_500_words():
    '''Test to check if the README.md file has equal to or greater than 500 words'''
    readme_words=[word for line in open('README.md', 'r', encoding="utf-8") for word in line.split()]
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session8_readme_proper_description():
    '''Test to check if description has been provided for each of the functions declared within the code'''
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session8_readme_file_for_more_than_10_hashes():
    '''Test to check if the number of topics and subtopics described within the README.md file is equal to or greater than 10'''
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10, "You have not described all the functions/classes well in your README.md file"


def test_session8_indentations():
    '''Test to check if the indentation in the session6.py file follows the PEP8 guidelines'''
    lines = inspect.getsource(session8)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        print(space)
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session8_function_name_had_cap_letter():
    '''PEP8 gudelines state that function names cannnot have capital letters in them. This test checks if there are any \
    capital lettes within function names and throws error if there are.'''
    functions = inspect.getmembers(session8, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


############################ Validation for Faker namedtuple type records #######################################

def test_session8_number_of_records_namedtuple():
  '''Test to check if the code raises an error when a non-integer value is passed as an argument against \
  num_records.'''

  with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
    session8.profile_feature_generator_namedtuple(num_records="A string")


def test_session8_record_not_negative_namedtuple():
  '''Test to check if the code raises an error when a negative value is passed as an argument against \
  num_records..'''

  with pytest.raises(ValueError, match=r".*Please enter a positive value*"):
    session8.profile_feature_generator_namedtuple(num_records=-10000)


def test_session8_execution_time_namedtuple():
  '''Test to check the time taken for the function to be executed when "namedtuple" library is \
  implemented as a data container.'''

  start = perf_counter()
  result = session8.profile_feature_generator_namedtuple(num_records=10000)
  end = perf_counter()
  execution_time = end - start
  print(execution_time)
  assert (execution_time < 24), "The code is taking too long to be executed"


def test_session8_testtuple_fields_present_namedtuple():
  '''Test to check the time taken for the function to be executed when "dictionary" library is \
  implemented as a data container.'''

  result = session8.profile_feature_generator_namedtuple(num_records=10000)
  assert (result ['largest_blood_type'] != None), "The dictionary should contain the field 'largest_blood_type'"
  assert (result ['mean_current_location'] != None), "The dictionary should contain the field 'mean_current_location'"
  assert (result ['oldest_person_age'] != None), "The dictionary should contain the field 'oldest_person_age'"
  assert (result ['average_age'] != None), "The dictionary should contain the field 'average_age'"


def test_session8_profile_summary_container_type_namedtuple():
  '''Test to check if the processed data is being stored in a dictionary type data container.'''

  result = session8.profile_feature_generator_dictionary(num_records=10000)
  assert isinstance(result, dict) == True, "You should return a dictionary"



############################ Validation for Faker dictionary type records ######################################

def test_session8_number_of_records_dictionary():
  '''Test to check if the code raises an error when a non-integer value is passed.'''

  with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
    session8.profile_feature_generator_dictionary(num_records="A string")


def test_session8_record_not_negative_dictionary():
  '''Test to check if the code raises an error when a negative value is passed.'''

  with pytest.raises(ValueError, match=r".*Please enter a positive value*"):
    session8.profile_feature_generator_dictionary(num_records=-10000)


def test_session8_execution_time_dictionary():
  '''Test to check the time taken for the function to be executed when "dictionary" library is \
  implemented as a data container.'''

  start = perf_counter()
  result = session8.profile_feature_generator_dictionary(num_records=10000)
  end = perf_counter()
  execution_time = end - start
  print(execution_time)
  assert (execution_time < 27), "The code is taking too long to be executed"


def test_session8_testtuple_fields_present_dictionary():
  '''Test check if all the required fields are present within the output dictinary.'''

  result = session8.profile_feature_generator_dictionary(num_records=10000)
  assert (result ['largest_blood_type'] != None), "The dictionary should contain the field 'largest_blood_type'"
  assert (result ['mean_current_location'] != None), "The dictionary should contain the field 'mean_current_location'"
  assert (result ['oldest_person_age'] != None), "The dictionary should contain the field 'oldest_person_age'"
  assert (result ['average_age'] != None), "The dictionary should contain the field 'average_age'"


def test_session8_profile_summary_container_type_dictionary():
  '''Test to check if the results of the code are returned within a dictionary.'''

  result = session8.profile_feature_generator_dictionary(num_records=10000)
  assert isinstance(result, dict) == True, "You should return a dictionary"


############################ Test to prove that namedtuple is faster ######################################

def test_session8_execution_time_compare():
  '''Test to check the compare the execution times of functions rofile_feature_generator_namedtuple and profile_feature_generator_dictionary.'''

  start_namedtuple = perf_counter()
  result_namedtuple = session8.profile_feature_generator_namedtuple(num_records=10000)
  end_namedtuple = perf_counter()
  execution_time_namedtuple = end_namedtuple - start_namedtuple
  start_dict = perf_counter()
  result_dict = session8.profile_feature_generator_dictionary(num_records=10000)
  end_dict = perf_counter()
  execution_time_dict = end_dict - start_dict
  print(execution_time_dict, " ", execution_time_namedtuple)
  assert (execution_time_dict > execution_time_namedtuple), "The named tuple code is taking longer to execute"


############################ Validation for Fake 100 companies' stocks ######################################

def test_session8_company_profile_generator_non_integer():
  '''Test to ensure that the argument passed against num_records is of type integer.'''

  with pytest.raises(TypeError, match=r".*Please enter an integer only*"):
    session8.profile_feature_generator_namedtuple(num_records="A string")


def test_session8_company_profile_generator_record_not_negative():
  '''Test to ensure that the argument passed against num_records is a positive value.'''

  with pytest.raises(ValueError, match=r".*Please enter a positive value*"):
    session8.profile_feature_generator_namedtuple(num_records=-10000)


def test_session8_company_profile_generator_number_of_records():
  '''Test to check if the correct number of records are being generated and passed to the subsequent function.'''

  data_dict, summary_dict = session8.company_profile_generator(num_records=100)
  assert len(data_dict) == 100, "The number of records should be 100"


def test_session8_company_profile_generator_list_check():
  '''Test to ensure that the initial data generated by the Faker library is stored as a collection of tuples within a list.'''

  data_dict, summary_dict = session8.company_profile_generator(num_records=100)
  assert isinstance(data_dict, list) == True, "The data is not being collected in a list."


def test_session8_company_profile_generator_list_non_empty_check():
  '''Test to ensure that the aforementioned list is being populated as per requirement.'''

  data_dict, summary_dict = session8.company_profile_generator(num_records=100)
  assert (data_dict != None), "The list seems to be empty"


def test_session8_company_profile_generator_dictionary_check():
  '''Test to ensure that the processed data is stored within a dictionary.'''

  data_dict, summary_dict = session8.company_profile_generator(num_records=100)
  assert isinstance(summary_dict, dict) == True, "The data is not being collected in a dictionary."


def test_session8_company_profile_generator_dictionary_non_empty_check():
  '''Test to ensure that the dictionary is being populated as per requirement.'''

  data_dict, summary_dict = session8.company_profile_generator(num_records=100)
  assert (summary_dict != None), "The dictionary seems to be empty"


def test_session8_company_profile_generator_stock_high_amount():
  '''Test to ensure that the highest price of the stock is either greater than or equal to its opening price.'''

  data_tuple, summary_dict = session8.company_profile_generator(num_records=100)
  for data in data_tuple:
    assert(data.high >= data.open), "High is less than open"


def test_session8_company_profile_generator_stock_close_amount():
  '''Test to ensure that the price of the stock at closing is lesser than or equal to its highest price.'''

  data_tuple, summary_dict = session8.company_profile_generator(num_records=100)
  for data in data_tuple:
    assert(data.high >= data.close), "High is less than close"


def test_session8_company_profile_generator_dictionary_field_check():
  '''Test to ensure that a dictionary containing the data fields of average weighted open, average weighted \
  high and average wieghted close is being created.'''
  
  data_tuple, summary_dict = session8.company_profile_generator(num_records=100)
  assert (summary_dict ['weighted_open'] != None), "The dictionary should contain the field 'weighted_open'"
  assert (summary_dict ['weighted_high'] != None), "The dictionary should contain the field 'weighted_high'"
  assert (summary_dict ['weighted_close'] != None), "The dictionary should contain the field 'weighted_close'"
