import logging

logging.basicConfig(level=logging.INFO)

def handler(event=None, context=None):
    logging.info("App is running through CircleCI IDT demo pipeline.")
    return {"status": "success", "message": "Deployment successful!"}

if __name__ == "__main__":
    print(handler())
