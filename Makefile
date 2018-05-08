prepare_data_dir:
	mkdir -p data

get_test_data: prepare_data_dir
	curl -o ./data/test.csv https://raw.githubusercontent.com/rebeccabilbro/titanic/master/data/test.csv

get_train_data: prepare_data_dir
	curl -o ./data/train.csv https://raw.githubusercontent.com/rebeccabilbro/titanic/master/data/train.csv

data: get_test_data get_train_data
	python src/csv_to_json.py

train: get_train_data
	python src/train_model.py

clean:
	rm -f pipeline.pkl
	rm -rf data/
