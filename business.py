import pandas as pd 

def get_data():
    
    df = pd.read_csv('data.csv')

    #print(df['states'].tolist())

    Countries              = df['Countries'].tolist()
    Oxford_AstraZeneca     = df['Oxford AstraZeneca'].tolist()
    Pfizer_BioNTech        = df['Pfizer BioNTech'].tolist()
    Johnson_and_Johnson    = df['Johnson and Johnson'].tolist()
    Moderna                = df['Moderna'].tolist()

    list_of_tuples = [tuple(row) for row in df.values]
  
    # print(list_of_tuples)

    result_dict = {
        'Countries ' : Countries ,
        'data_list'  : [
            {
                "name": 'Oxford AstraZeneca',
                "data": Oxford_AstraZeneca 
            },
            {
                "name": 'Pfizer BioNTech',
                "data": Pfizer_BioNTech
            },
            {
                "name": 'Johnson and Johnson',
                "data": Johnson_and_Johnson 
            },
            {
                "name": 'Moderna',
                "data": Moderna
            }
        ]
    }

    print(result_dict)

    return result_dict

if __name__ == "__main__":
    get_data()
    