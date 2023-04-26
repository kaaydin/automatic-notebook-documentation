import re 

string = 'The resulting data is stored in the "training" variable.\ntraining = get_training(TRAINING_PATH, CLASS_LABELS, BANDS)'


nb_encoded = re.sub('\"\w\"', '\\"\w\\"' , string )

print(nb_encoded)