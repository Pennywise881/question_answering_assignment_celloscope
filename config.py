# experiment ID
exp = "exp-1"

# data directories
# data_dir = "/Users/gdamien/Data/squad/"
data_dir = "/content/question_answering_assignment_celloscope/Data/squad/"
train_dir = data_dir + "train/"
dev_dir = data_dir + "dev/"

# model paths
# spacy_en = "/Users/gdamien/Data/spacy/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0"
spacy_en = "/content/question_answering_assignment_celloscope/Data/spacy/en_core_web_sm-2.0.0/en_core_web_sm/en_core_web_sm-2.0.0"
glove = "/content/question_answering_assignment_celloscope/glove_6B/" + "glove.6B.{}d.txt"
squad_models = "content/question_answering_assignment_celloscope/output/" + exp


# preprocessing values
max_words = -1
word_embedding_size = 100
char_embedding_size = 8
max_len_context = 400
max_len_question = 50
max_len_word = 25

# training hyper-parameters
num_epochs = 15
batch_size = 64
learning_rate = 0.5
drop_prob = 0.2
hidden_size = 100
char_channel_width = 5
char_channel_size = 100
cuda = True
pretrained = False
