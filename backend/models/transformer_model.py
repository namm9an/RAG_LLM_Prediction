import torch
import torch.nn as nn

class TransformerModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim, num_heads, num_layers):
        super(TransformerModel, self).__init__()
        self.transformer = nn.Transformer(input_dim, num_heads, num_layers)
        self.fc = nn.Linear(hidden_dim, output_dim)

    def forward(self, x):
        x = self.transformer(x)
        return self.fc(x)

def predict(data):
    model = TransformerModel(input_dim=10, hidden_dim=50, output_dim=1, num_heads=5, num_layers=3)
    prediction = model(data)
    return prediction
