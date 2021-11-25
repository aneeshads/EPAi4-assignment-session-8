# Use the Faker (Links to an external site.)library to get 10000 random profiles. 
# Using namedtuple, calculate the largest blood type, mean-current_location, 
# oldest_person_age, and average age (add proper doc-strings).
from faker import Faker
from collections import namedtuple, Counter
from datetime import date, time
from decimal import Decimal
import statistics
import random

# internal function to calculate age
def calculate_age(birthDate):
    '''This function has been assigned to express the age of a person given the date of birth \
    (represented by the parameter 'birthDate') in the year/month/day format.'''

    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day)) 
    return age


def profile_feature_generator_namedtuple(num_records=10000):
    '''This function fetches 100 fake profiles of imaginary people and their personal \
    information. It then takes into account a few fields – username, blood type, \
    current location and age –  of the people represented in the records. Using the \
    concepts of namedtuple, the data has been stored and such calculations as largest \
    blood type, mean current location, age of the oldest person in the record and the \
    average age has been performed.
    Usage: profile_feature_generator_namedtuple(num_records=n)'''

    if (isinstance(num_records,int)) == False:
        raise TypeError("Please enter an integer only")
    if (num_records < 0):
        raise ValueError("Please enter a positive value")
    fake = Faker()
    Faker.seed(0)
    Profile = namedtuple('Profile', 'username blood_type current_location age')
    profile_list = []
    profile_summary_dict = {}
    for i in range(num_records):
        profile_details = fake.profile(fields = ['username','blood_group','current_location', 'birthdate' ])
        testtuple = Profile(profile_details['username'],profile_details['blood_group'], profile_details['current_location'] , calculate_age(profile_details['birthdate']))
        profile_list.append(testtuple)

    blood_type_list = Counter(p.blood_type for p in profile_list)
    largest_blood_type = blood_type_list.most_common(1)[0][0]
    location_avg_latitude = sum(p.current_location[0] for p in profile_list)/ len(profile_list)
    location_avg_longitude = sum(p.current_location[1] for p in profile_list)/ len(profile_list)
    highest_age = max(p.age for p in profile_list)
    age_avg = sum(p.age for p in profile_list) / len(profile_list)
    profile_summary_dict = {'largest_blood_type':largest_blood_type, 'mean_current_location':(location_avg_latitude, location_avg_longitude), 'oldest_person_age':highest_age, 'average_age':age_avg}

    return profile_summary_dict


# Do the same thing above using a dictionary. Prove that namedtuple is faster.
def profile_feature_generator_dictionary(num_records=10000):
    '''This function fetches 100 fake profiles of imaginary people and their personal \
    information. It then takes into account a few fields – username, blood type, \
    current location and age –  of the people represented in the records. Using the \
    concepts of dictionary, the data has been stored and such calculations as largest \
    blood type, mean current location, age of the oldest person in the record and the \
    average age has been performed.
    Usage: profile_feature_generator_dictionary(num_records=n)'''

    if (isinstance(num_records,int)) == False:
        raise TypeError("Please enter an integer only")
    if (num_records < 0):
        raise ValueError("Please enter a positive value")
    profile_dict = {}
    profile_summary_dict = {}
    fake = Faker()
    Faker.seed(0)
    for i in range(num_records):
        profile_details = fake.profile(fields = ['username','blood_group','current_location', 'birthdate' ])
        profile_details['age'] = calculate_age(profile_details['birthdate'])
        profile_dict[i+1] = profile_details
    blood_type_list = Counter(profile_dict[p]['blood_group'] for p in profile_dict)
    largest_blood_type = blood_type_list.most_common(1)[0][0]
    location_avg_latitude = sum(profile_dict[p]['current_location'][0] for p in profile_dict)/ len(profile_dict)
    location_avg_longitude = sum(profile_dict[p]['current_location'][1] for p in profile_dict)/ len(profile_dict)
    highest_age = max(profile_dict[p]['age'] for p in profile_dict)
    age_avg = sum(profile_dict[p]['age'] for p in profile_dict) / len(profile_dict)
    profile_summary_dict = {'largest_blood_type':largest_blood_type, 'mean_current_location':(location_avg_latitude, location_avg_longitude), 'oldest_person_age':highest_age, 'average_age':age_avg}

    return profile_summary_dict


# Create fake data (you can use Faker for company names) for imaginary stock 
# exchange for top 100 companies (name, symbol, open, high, close). Assign a 
# random weight to all the companies. Calculate and show what value the stock 
# market started at, what was the highest value during the day, and where did it
# end. Make sure your open, high, close are not totally random. You can only use
# namedtuple.
def company_profile_generator(num_records=100):
    ''''This function fetches the names of a number of companies (specified by \
    the parameter num_records) and stores data related to their stock prices \ 
    using the concepts of namedtuple. The data stored in the namedtuple are usually \
    price during the opening, highest price and the price at closing. In addition, each \
    of the companies have been allotted weights, which reflect each of their market cap. \
    Using the aforementioned knowledge, the weighted average of the opening price, the \
    weighted average of  the highest price and the weighted average of the closing price \
    has been calculated for each company. 
    Usage: company_profile_generator(num_records=n)'''

    if (isinstance(num_records,int)) == False:
        raise TypeError("Please enter an integer only")
    if (num_records < 0):
        raise ValueError("Please enter a positive value")
    fake = Faker()
    Faker.seed(0)
    Faker100 = namedtuple('Faker100', 'name symbol open high close weight')
    company_stock = []
    Faker100_stock_summary_dict = {}
    Faker100 = namedtuple('Faker100', 'name symbol open high close weight')
    company_stock = []
    Faker100_stock_summary_dict = {}

    for c in range(num_records):
        name = fake.company() + ' ' + fake.company_suffix()
        symbol = (name[:4].upper() + str(c))
        open = random.randint(1, 1000)
        increaseperc = (random.randint (0,20)/100) * open
        high = random.randint(open, int(open+increaseperc))
        decreaseperc = (random.randint(0,20)/100) * open
        low = random.randint(int(open-decreaseperc), open)
        close = random.randint(low, high)
        weight = random.randint(1, 10)
        companytuple = Faker100(name, symbol, open, high, close, weight)
        company_stock.append(companytuple)

    sum_of_weights = sum(p.weight for p in company_stock)
    weightedopen = round(sum((p.open * p.weight) for p in company_stock)/sum_of_weights, 2)
    weightedhigh = round(sum((p.high * p.weight) for p in company_stock)/sum_of_weights, 2)
    weightedclose = round(sum((p.close * p.weight) for p in company_stock)/sum_of_weights, 2)
    Faker100_stock_summary_dict = {'weighted_open':weightedopen, 'weighted_high':weightedhigh, 'weighted_close':weightedclose}

    return company_stock, Faker100_stock_summary_dict

