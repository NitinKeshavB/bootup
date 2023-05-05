# Python logging

Now it is your turn! 

## Task:
- Implement logging in your Python file, and validate that your pipeline runs and logs something similar to: 

```
[INFO][2022-05-18 20:13:18,297][trading_price_pipeline.py]: Commencing extraction
[INFO][2022-05-18 20:13:22,972][trading_price_pipeline.py]: Extraction complete
[INFO][2022-05-18 20:13:22,972][trading_price_pipeline.py]: Commencing transformation
[INFO][2022-05-18 20:13:22,981][trading_price_pipeline.py]: Transformation complete
[INFO][2022-05-18 20:13:22,982][trading_price_pipeline.py]: Commencing file load
[INFO][2022-05-18 20:13:23,016][trading_price_pipeline.py]: File load complete
[INFO][2022-05-18 20:13:23,034][trading_price_pipeline.py]: Commencing database load
[INFO][2022-05-18 20:13:23,295][trading_price_pipeline.py]: Database load complete
```

To run your code, make sure you execute the following: 

```
# 1. change directory to the src folder. 
cd your_path_to_src_folder/src

# 2. set the python path. You will only need to do this once. 
. ./set_python_path.sh

# 3. Set the environment variables. You will only need to do this once. 
. ./your_project/config.sh 

# 4. Run your python pipeline 
python your_project/pipeline/your_pipeline.py
```

