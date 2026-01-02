# how to install
```
git clone https://github.com/y423610m/genesis_rl.git
cd genesis_rl
git submodule --init 
uv sync
```

# train
```
uv run humanoids/g1/g1_train.py --max_iterations 100 --exp_name g1_walking_20250102
```

# monitor
```
uv run tensorboard --logdir logs
firefox http://localhost:6006/
```

# eval
```
uv run humanoids/g1/g1_eval.py --ckpt 100 --exp_name g1_walking_20250102
```
