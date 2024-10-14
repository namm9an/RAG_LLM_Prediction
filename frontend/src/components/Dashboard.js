import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Line } from 'react-chartjs-2';

const Dashboard = () => {
  const [predictionData, setPredictionData] = useState({});
  const [causalData, setCausalData] = useState({});
  const [llmInsights, setLlmInsights] = useState('');

  useEffect(() => {
    axios.get('/predict/lstm')
      .then(response => {
        const data = response.data;
        setPredictionData({
          dates: data.prediction.relevant_stock_data.split('\n').map(row => row.split()[0]),
          values: data.prediction.relevant_stock_data.split('\n').map(row => row.split()[1])
        });
        setCausalData(data.causal_inference);
        setLlmInsights(data.prediction.llm_insights);
      })
      .catch(error => console.error('Error fetching data', error));
  }, []);

  const chartData = {
    labels: predictionData.dates,
    datasets: [{
      label: 'Stock Prices',
      data: predictionData.values,
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 2
    }]
  };

  return (
    <div>
      <h2>Stock Prediction Dashboard</h2>
      <Line data={chartData} />
      <h3>LLM Insights:</h3>
      <p>{llmInsights}</p>
      <h3>Causal Inference:</h3>
      <p>{JSON.stringify(causalData)}</p>
    </div>
  );
};

export default Dashboard;
