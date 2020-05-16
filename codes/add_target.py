import pandas as pd
from tqdm import tqdm

dataset_path  = '/home/vicky/workspace/projects/plasticc/data'

## Meta data
training_meta = pd.read_csv(f'{dataset_path}/PLAsTiCC-2018/training_set_metadata.csv')
training_meta.head()

## reading sample data
training_set = pd.read_csv(f'{dataset_path}/PLAsTiCC-2018/training_set.csv')
default_target_values = [None for i in range(len(training_set))]
training_set['target'] = default_target_values

## updating
for object_id in tqdm(training_set.object_id.unique()):
    # print(f'object_id = {object_id}')
    target_value = int(training_meta[training_meta['object_id'] == object_id].target)
    num_elements = len(training_set[training_set['object_id'] == object_id])
    target_values = [target_value for i in range(num_elements)]
    training_set.loc[training_set['object_id'] == object_id, 'target'] = target_values

output_csv = '/home/vicky/workspace/projects/plasticc/data/training_set_with_target.csv'
training_set.to_csv(output_csv)