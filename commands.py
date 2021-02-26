from app import app

@app.cli.command()
def test():
    print('This is a test message')