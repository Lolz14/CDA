import os
import pandas as pd
#new
def load_data(data_folder: str = r"C:\Users\Diego\Documents\DTU\Spring2023\CDA\CDA_Projects\Case2\dataset\dataset") -> pd.DataFrame:
    # define the path to the data folder
    # initialize an empty list to hold the dataframes for each file
    dataframes = []
    # loop through the folders and subfolders to read the csv files and create dataframes
    for type_folder in os.listdir(data_folder):
        type_folder_path = os.path.join(data_folder, type_folder)
        for id_folder in os.listdir(type_folder_path):
            id_folder_path = os.path.join(type_folder_path, id_folder)
            for round_folder in os.listdir(id_folder_path):
                round_folder_path = os.path.join(id_folder_path, round_folder)
                for phase_folder in os.listdir(round_folder_path):
                    phase_folder_path = os.path.join(round_folder_path, phase_folder)
                    for filename in os.listdir(phase_folder_path):
                        if filename.endswith(".csv"):
                            file_path = os.path.join(phase_folder_path, filename)
                            data_type = filename[:-4]
                            df = pd.read_csv(file_path)
                            df["Group"] = type_folder
                            df["ID"] = id_folder
                            df["Round"] = round_folder
                            df["Phase"] = phase_folder
                            df["data_type"] = data_type
                            dataframes.append(df)

    # concatenate all the dataframes into a single one
    df = pd.concat(dataframes, axis=0, ignore_index=True).iloc[:,1:]
    return df
