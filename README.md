# Bracnet Payment API(Dockerized)
This a basic Django restframework implementation for Bracnet limited. We have implement SSLCommerz and bkash payment api. This api will work as a payment hub for all online transaction of bracnet. 
## Installation
1. Install docker and git
2. Clone this git to local machine
3. Go to the root folder where Dockerfile is located and run `docker build .`
4. then run `docker-compose build`
5. Finally, run `docker-compose up`
#### Note 1: if app container starts before db than just re-run 5th command.
#### Note 2: Change the .env.sample to .env and set the env variables.
#### Note 3: Add the ip/host in settings.py. Example: ALLOWED_HOSTS = ['202.0.0.1','127.0.0.1']
## Contributing
1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D
