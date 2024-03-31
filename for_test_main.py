import requests

example = {'Type_parents': 1.0,
           'Birth_1mth_M_inclusion': 1.0,
           'Birth_12mth_M_inclusion': 1.0,
           'Age': 34.0,
           'Marital_status': 2.0,
           'Marital_status_edit': 2.0,
           'Education': 5.0,
           'Gestationnal_age': 37.0,
           'Type_pregnancy': 1.0,
           'sex_baby1': 1.0,
           'CBTS_M_3': 0.0,
           'CBTS_M_4': 0.0,
           'CBTS_M_5': 0.0,
           'CBTS_M_6': 0.0,
           'CBTS_M_7': 0.0,
           'CBTS_M_8': 0.0,
           'CBTS_M_9': 0.0,
           'CBTS_M_10': 1.0,
           'CBTS_M_11': 0.0,
           'CBTS_M_12': 0.0,
           'CBTS_13': 0.0,
           'CBTS_14': 0.0,
           'CBTS_15': 0.0,
           'CBTS_16': 0.0,
           'CBTS_17': 2.0,
           'CBTS_18': 0.0,
           'CBTS_19': 2.0,
           'CBTS_20': 0.0,
           'CBTS_21': 0.0,
           'CBTS_22': 1.0,
           'EPDS_1': 1.0,
           'EPDS_2': 2.0,
           'EPDS_3': 2.0,
           'EPDS_4': 1.0,
           'EPDS_5': 1.0,
           'EPDS_6': 2.0,
           'EPDS_7': 0.0,
           'EPDS_8': 2.0,
           'EPDS_9': 2.0,
           'EPDS_10': 0.0,
           'HADS_1': 2.0,
           'HADS_3': 1.0,
           'HADS_5': 2.0,
           'HADS_7': 2.0,
           'HADS_9': 0.0,
           'HADS_11': 1.0,
           'HADS_13': 1.0,
           'Child_survey_participation': 1.0,
           'Age_bb': 1.0}

if __name__ == '__main__':
    # for test
    url = 'http://localhost:9696/predict'  ## this is the route we made for prediction
    response = requests.post(url, json=example)  ## post the customer information in json format
    result = response.json()  ## get the server response
    print(result)