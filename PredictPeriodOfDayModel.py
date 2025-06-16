import joblib
from config import settings
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn.preprocessing import LabelEncoder

class PredictPeriodOfDayModel:
    """
    This class is used to predict the period of the day based on the given time.
    """

    def __init__(self):
        """
        Initialize the PredictPeriodOfDayModel class.
        """
        self.model = None
        self.label_encoder = LabelEncoder()
        labels = ["Night", "Morning", "Evening"]
        self.label_encoder.fit(labels)  

    def load_model(self):
        """
        Load the pre-trained model from the specified path.
        """
        try:
            self.model = joblib.load(settings.MODEL_PATH)
            print(f"Model loaded successfully from {settings.MODEL_PATH}")
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def train(self, test_size=0.2):
        """
        Train the model with the provided data.

        :param test_size: Proportion of the dataset to include in the test split.
        """

        df = pd.read_csv(settings.DATA_PATH)
        df["Period_Encoded"] = self.label_encoder.fit_transform(df["Period"])
        X = df[["Hour"]]    
        y = df["Period_Encoded"]

        df.head()

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
        self.model = RandomForestClassifier()
        self.model.fit(X_train, y_train)
        

        # Save the model after training
        joblib.dump(self.model, settings.MODEL_PATH)
        print(f"Model trained and saved to {settings.MODEL_PATH}")
        return self.model

        

    def predict(self, data):
        """
        Predict the period of the day based on the given data.

        :param data: The input data for prediction.
        :return: The predicted period of the day.
        """
        if self.model is None:
            print("Model is not loaded. Cannot make predictions.")
            return None

        try:
            hour = pd.DataFrame({"Hour": [data]})
            prediction = self.model.predict(hour)

            returnValue = self.label_encoder.inverse_transform(prediction)[0]
              
            return  returnValue
        
        except Exception as e:
            print(f"Error during prediction: {e}")
            return None
    