# main.py – Entry point of the project

import logging
import pandas as pd
import PredictPeriodOfDayModel
import numpy as np

def main():
    logging.info("Starting the application...")

    model = PredictPeriodOfDayModel.PredictPeriodOfDayModel()
    model.train(test_size=0.2)
    logging.info(f"Model trained successfully.")
    logging.info(f"Model: {model}")

    logging.info(f"Processing Result:")

    logging.info(model.predict(18))

    model2 = PredictPeriodOfDayModel.PredictPeriodOfDayModel()
    model2.load_model()
    logging.info(model.predict(20))


if __name__ == "__main__":
    main()
