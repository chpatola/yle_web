<h1>Election Predictor</h1>
<p>This is the web version of the project found here: https://github.com/chpatola/election_predicter</p>
<p>Try the app here: https://yle-election-predictor.herokuapp.com/</p>

<h2>Instructions for running the project locally</h2>
You can choose to run the project either via Docker or manually.

<h4>Run manually</h4>

1. Install python 3.8: https://www.python.org/downloads/
2. Make sure pip is installed: https://pip.pypa.io/en/stable/installation/
3. Install all packages mentioned in requirements.txt
4. Start the app in your terminal
      
        python app.py

Now you can open localhost:5000 in your browser and use the app there.


<h4>Run via Docker</h4>
You can use the Docker image provided here https://hub.docker.com/repository/docker/chpatola/yle_web.

The Dockerfile is also uploaded in this repository. Execute the following commands in your terminal.

    1. docker image pull chpatola/yle_web
    2. docker run -p 5000:5000 chpatola/yle_web
    
Now you can open localhost:5000 in your browser and use the app there.    
    
    


