# main.py – Entry point of the project

import logging
import pandas as pd
import PredictPeriodOfDayModel


def main():
    logging.info("Starting the application...")

    perioddf = pd.read_csv("data/periods.csv") 
    logging.info(f"Period DataFrame:\n{perioddf}")

    model = PredictPeriodOfDayModel.PredictPeriodOfDayModel()
    model.train(test_size=0.2)
    logging.info(f"Model trained successfully.")
    logging.info(f"Model: {model}")

    logging.info(f"Processing Result:")

if __name__ == "__main__":
    main()
