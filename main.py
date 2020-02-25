from matches_played_per_year import compute_and_plot_matches_played_per_year

import csv

def extract_matches():
    data_file=open('matches.csv','r')
    match_file=csv.DictReader(data_file)
    return match_file


def extract_deliveries():
    data_file=open('deliveries.csv','r')
    deliveries_file=csv.DictReader(data_file)
    return deliveries_file


def main():
    compute_and_plot_matches_played_per_year(extract_matches())
    
if __name__ == "__main__":
    main()
