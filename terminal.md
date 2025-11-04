python3 generate_causal_dataset.py \
  --nodes 3 \
  --seed 33550336 \
  --output "datasets/node03/n3_all_observations.json"

python3 generate_3d_dataset_complete.py \               
  --grid-size 3 \                      
  --max-height 3 \                                   
  --max-blocks 1 \
  --fixed \
  --seed 33550336 \
  --output "datasets/3d_grid3_h3.json"

python3 boolean_dataset.py \                            
  --operators basic \                  
  --max-depth 2 \                                    
  --output 'datasets/boolean_2var.json' \
  --seed 33550336 


python3 run_causal_benchmark.py \
  --dataset "datasets/node03/n3_all_observations.json" \
  --config "config/config_gpt4o.yaml" \
  --n-samples 10 \
  --query-multiplier 1.0 \
  --seed 33550336


python3 run_3d_benchmark.py \
  --dataset "datasets/3d_grid3_h3.json" \
  --config "config/config_gpt4o.yaml" \
  --n-samples 9 \
  --query-multiplier 1.0 \
  --seed 33550336


python3 boolean_benchmark.py \
  --dataset "datasets/boolean_2var.json" \
  --config "config/config_gpt4o.yaml" \
  --n-samples 10 \
  --query-multiplier 1.0 \
  --seed 33550336

