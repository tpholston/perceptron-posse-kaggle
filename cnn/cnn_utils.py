import torch
import math
import pandas as pd
import numpy as np
from tqdm import tqdm
from torch.utils.data import DataLoader, Dataset

class TaxiDataset(Dataset):
    def __init__(self, data, labels=None):
        self.data = data
        self.labels = labels
        
    def __getitem__(self, index):
        x = self.data[index]
        if self.labels is not None:
            y = self.labels[index]
            return x, y
        return x
    
    def __len__(self):
        return len(self.data)

def test_prediction_to_csv(y_pred, outfile_name, test_data):
    
	output_df = pd.DataFrame(test_data["TRIP_ID"])
	output_df["TRAVEL_TIME"] = y_pred
	output_df.head()

	output_df.to_csv(f'../guesses/{outfile_name}', index=False)

def num_parameters(model):
    return sum(p.numel() for p in model.parameters())

def evaluate(network, dataloader_test, device, criterion):
    test_loss = 0.0
    with torch.no_grad():
        for inputs, labels in dataloader_test:
            inputs, labels = inputs.to(device), labels.to(device)

            # Perform forward pass
            outputs = network(inputs)

            # Reshape labels for warning
            labels = labels.view(-1, 1)
            
            # Compute loss
            loss = criterion(outputs, labels)

            test_loss += loss

    return math.sqrt(test_loss.cpu().detach().numpy() / len(dataloader_test))

def predict(network, dataloader_pred, device):
    network.eval()  # Set the model to evaluation mode
    predictions = []

    with torch.no_grad():
        for inputs in dataloader_pred:
            inputs = inputs.to(device)
	
            # Perform forward pass
            outputs = network(inputs)

            outputs = outputs.float()

            # Append predictions to the list
            predictions.append(outputs.cpu().numpy())

            # Convert the list of predictions to a NumPy array
    predictions = np.concatenate(predictions)
    return predictions

def pipeline(network, optimizer, dataloader_train, dataloader_test, dataloader_pred, device, criterion, epochs=10, verbose=False):

    # BEGIN TRAINING
    train_losses = []

    for epoch in tqdm(range(epochs)):

        running_loss = 0.0

        for inputs, labels in dataloader_train:
            inputs, labels = inputs.to(device), labels.to(device)
            
            # Zero the gradients
            optimizer.zero_grad()
            
            # Perform forward pass
            outputs = network(inputs)

            # Reshape labels for warning
            labels = labels.view(-1, 1)
            
            # Compute loss
            loss = criterion(outputs, labels)
            
            # Perform backward pass
            loss.backward()
            
            # Perform optimization
            optimizer.step()

            running_loss += loss.cpu().detach().numpy()
        train_losses.append(math.sqrt(running_loss / len(dataloader_train)))
        
        if verbose:
            print(f"Epoch {epoch+1} - Train Loss = {train_losses[-1]}")

    print('Training process has finished.')
    
    # BEGIN TESTING
    test_loss = evaluate(network, dataloader_test, device, criterion)

    # BEGIN PREDICTION
    predictions = predict(network, dataloader_pred, device)
            
    return train_losses, test_loss, predictions
