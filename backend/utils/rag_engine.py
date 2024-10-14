import openai
import pandas as pd

openai.api_key = "your-openai-api-key"

def retrieve_relevant_data(data, prediction_date):
    window = pd.Timedelta(days=30)
    relevant_data = data[(data['Date'] >= (prediction_date - window)) & 
                         (data['Date'] <= (prediction_date + window))]
    return relevant_data

def get_llm_augmented_prediction(prediction, data):
    prediction_date = data['Date'].max()
    relevant_data = retrieve_relevant_data(data, prediction_date)
    relevant_text = relevant_data.to_string()

    context = (f"Stock prediction is {prediction}. Provide insights based on "
               f"the following stock data history: \n{relevant_text}")

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "You are a financial analyst."},
        {"role": "user", "content": context}
      ],
      max_tokens=150
    )

    llm_insights = response['choices'][0]['message']['content']

    return {
        "prediction": prediction,
        "relevant_stock_data": relevant_text,
        "llm_insights": llm_insights
    }
