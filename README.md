# Currency-Converter
Repository for python GUI application for currency conversion

## API configuration
In order to configure the API for this project you will need to create a ```.env``` file inside the API folder located in the project <b>root directory.</b>

Inside the file you will need to create an enviroment variable called ```API_KEY``` and assign the API access_key value to it. The API access key can be obtained by registering a free account at [https://fixer.io](https://fixer.io). The final contents of the .env file should look similar to this example:

```API_KEY=auhf7wqB35r9u2eg9gr9486ng48dy3tr```

Once this file exists and the API key is valid you are ready to start using the API by importing ```currency_api.py``` module from the API packet.

## Dependencies
The following modules need to be installed before running the project locally:

+ requests
+ json
+ os
+ dotenv
+ urllib3