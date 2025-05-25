import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df["race"].value_counts()

    # What is the average age of men?
    male_ages = df[df['sex'] == 'Male']
    average_age_men = float(male_ages['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    dict_count=((df['education'].value_counts(normalize=True))*100).to_dict()
    percentage_bachelors = dict_count["Bachelors"]

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    advanced_education = ['Bachelors', 'Masters', 'Doctorate']

    # Filter people with advanced education
    adv_edu_data = df[df['education'].isin(advanced_education)]
    
    # Total with advanced education
    total_adv_edu = len(adv_edu_data)
    
    # Those with advanced education earning >50K
    rich_adv_edu = len(adv_edu_data[adv_edu_data['salary'] == '>50K'])
    
    # Calculate percentage
    percentage = (rich_adv_edu / total_adv_edu) * 100
    
    # Optional: round result
    percentage_higher_edu = round(percentage, 2)
    
    # What percentage of people without advanced education make more than 50K?
    # Filter people with no advanced education
    no_adv_edu_data = df[~df['education'].isin(advanced_education)]
    
    # Total with no advanced education
    total_no_adv_edu = len(no_adv_edu_data)
    
    # Those with no advanced education earning >50K
    rich_no_adv_edu = len(no_adv_edu_data[no_adv_edu_data['salary'] == '>50K'])
    
    # Calculate percentage
    perc = (rich_no_adv_edu / total_no_adv_edu) * 100
    
    # Optional: round result
    percentage_lower_edu = round(perc, 2)
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education =  len(df[df['education'].isin(advanced_education)])
    lower_education = len(df[~df['education'].isin(advanced_education)])

    # percentage with salary >50K
    higher_education_rich = percentage_higher_edu 
    lower_education_rich = percentage_lower_edu 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = float(df['hours-per-week'].min())

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    #filter data to min hours workers
    min_hrs_data=df[df['hours-per-week']==min_hrs_week]
    #calculate number of people working min hours
    total_min_hrs_workers=len(min_hrs_data)
    #for those working min hour but earning more than 50k
    rich_min_hrs_workers=len(min_hrs_data[min_hrs_data['salary']=='>50K'])
    #percentage
    per=round((rich_min_hrs_workers / total_min_hrs_workers)*100,2)

    num_min_workers = total_min_hrs_workers

    rich_percentage = per

    # What country has the highest percentage of people that earn >50K?
    # list of unique countries and creation of percentage dict
    countries = list(df["native-country"].unique())
    country_per={}
    for country in countries:
        country_spec_data = df[df["native-country"]==country]
        
        # Total in a country
        total_country = len(country_spec_data)
        
        # Those in a country earning >50K
        rich_country= len(country_spec_data[country_spec_data['salary'] == '>50K'])
        
        # Calculate percentage
        percent = (rich_country / total_country) * 100
        
        # Optional: round result
        percents = round(percent, 2)
    
        country_per[country]=percents
    max_key = max(country_per, key=country_per.get)
    max_value = country_per[max_key]
    highest_earning_country = max_key
    highest_earning_country_percentage = max_value

    # Identify the most popular occupation for those who earn >50K in India.
    #India data
    country_India_data = df[df["native-country"]=="India"]
    #India people earning more than 50K
    India_sup_50k=country_India_data[country_India_data['salary'] == '>50K']
    #Occupations
    my_dict=India_sup_50k["occupation"].value_counts().to_dict()
    first_key = list(my_dict.keys())[0]
    first_value = my_dict[first_key]
    top_IN_occupation = first_key

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
