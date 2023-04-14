Flask E-Notary Website

Flask E-Notary is a web application for requesting notary services online. The application allows users to register for an account, log in, and submit requests for notary services. It also has a separate registration flow for notaries to register with the application.

Installation

To install Flask E-Notary, follow these steps:

Clone this repository: git clone https://github.com/BlancheC/e-notary_websire.git
Navigate to the project directory: cd ENOTARY
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate
Install the required packages: pip install -r requirements.txt
Usage

To run Flask E-Notary, follow these steps:

Navigate to the project directory: cd flask-enotary
Activate the virtual environment: source venv/bin/activate
Set the Flask application environment variable: export FLASK_APP=enotary
Run the application: flask run
The application should now be running on http://localhost:5000.

Configuration

The application requires the following environment variables to be set:

DATABASE_URL: The URL of the MySQL database where the application's data will be stored.
SECRET_KEY: A secret key used to encrypt session data.
Contributing

Contributions to Flask E-Notary are welcome! If you'd like to contribute, please follow these steps:

Fork this repository.
Create a new branch: git checkout -b my-new-feature
Make your changes and commit them: git commit -am 'Add some feature'
Push your changes to the branch: git push origin my-new-feature
Submit a pull request.
Credits

Flask E-Notary was created by Blanche Chung.

License

Flask E-Notary is licensed under the MIT License.
