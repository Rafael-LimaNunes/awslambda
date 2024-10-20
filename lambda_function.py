import os
    
def lambda_handler(event, context):

    env = os.environ['MINHA_ENV']
    print("Hello World! Pela Esteira")
    print(env)
