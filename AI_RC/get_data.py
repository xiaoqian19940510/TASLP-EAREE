from preprocessing.data_processor import read_squad_data

if __name__ == "__main__":
    read_squad_data("AI_RC/data/squad-like_all_train_data.json", "AI_RC/data/",is_training=True)


