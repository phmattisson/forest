from forest.oak.base import run
from forest import constants
import logging

def main():
    logging.getLogger().setLevel(logging.INFO)
    # Determine study folder and output_folder
<<<<<<< Updated upstream
    #study_folder = "/Volumes/One Touch/cnoc/study1_decrypt"
    #output_folder = "/Volumes/One Touch/cnoc/oak_output"
    study_folder = "d:\\acc\\meningioma"
    output_folder = "c:\\Users\\david\\Exjobb\\data\\acc\\meningioma_stats"

    # Determine study timezone and time frames for data analysis
    tz_str = "America/New_York"
    time_start = "2016-01-01 00_00_00"
    time_end = "2024-03-01 00_00_00"

    # Determine window for analysis. Available opts: "Hourly", "Daily", "both".
    frequency = constants.Frequency.DAILY
    users = ['iwuqsovc', 'rwr2byoc']
=======
    study_folder = "c:\\Users\\david\\Exjobb\\data\\pituitary\\accel_decrypted"
    output_folder = "c:\\Users\\david\\Exjobb\\data\\pituitary\\accel_stats"

    # Determine study timezone and time frames for data analysis
    tz_str = "America/New_York"
    time_start = None
    time_end = None

    # Determine window for analysis. Available opts: "Hourly", "Daily", "both".
    frequency = constants.Frequency.DAILY
    users = None
>>>>>>> Stashed changes

    # Call the main function
    run(study_folder, output_folder, tz_str=tz_str, frequency=frequency, time_start=time_start, time_end=time_end, users=users)

if __name__ == '__main__':
    main()



