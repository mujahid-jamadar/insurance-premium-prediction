
from src.pipeline.training_pipeline import runpipline
from src.logger import logging
def main():
    try:
        pipeline=runpipline()


    except Exception as e:
        logging.error(f"{e}")
        print(e)    
    




if __name__=="__main__":
    main()        