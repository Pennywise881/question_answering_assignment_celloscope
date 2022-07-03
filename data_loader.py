# external libraries
import torch.utils.data as data
from torch import tensor

class SquadDataset(data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        return {key: tensor(val[idx]) for key, val in self.encodings.items()}

    def __len__(self):
        return len(self.encodings['word_context'])

# class SquadDataset(data.Dataset):
#     """Custom Dataset for SQuAD data compatible with torch.utils.data.DataLoader."""

#     def __init__(self, w_context, c_context, w_question, c_question, labels):
#         """Set the path for context, question and labels."""
#         self.w_context = w_context
#         self.c_context = c_context
#         self.w_question = w_question
#         self.c_question = c_question
#         self.labels = labels

#     def __getitem__(self, index):
#         """Returns one data tuple of the form ( word context, character context, word question,
#          character question, answer)."""
#         return self.w_context[index], self.c_context[index], self.w_question[index], self.c_question[index],\
#                self.labels[index]

#     def __len__(self):
#         return len(self.w_context)
