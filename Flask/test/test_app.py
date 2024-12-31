from flask_testing import TestCase
from flask import current_app,url_for
from main import app


class MainTest(TestCase):
    def create_app(self):
        app.config["TESTING"]=True
        app.config["WTF_CSRF_ENABLED"]=False
        return app
    
    def test_app_exists_web(self):
        self.assertIsNotNone(current_app)
        
    def test_app_in_testing_mode(self):
        self.assertTrue(current_app.config["TESTING"])
    
    def test_index_redirects(self):
        response = self.client.get(url_for("index"))
        self.assertRedirects(response,url_for("show_information"))
        
    def test_show_information_get(self):
        response = self.client.get(url_for("show_information"))
        self.assert200(response)
    
    def test_show_information_post(self):        
        response = self.client.post(url_for("show_information"))
        self.assert405(response)
    
    def test_auth_blueprint_exists_module(self):
        self.assertIn("auth",self.app.blueprints)
        
    def test_auth_blueprint_login_get(self):
        response = self.client.get(url_for("auth.login"))
        self.assert200(response)
        
    def test_auth_blueprint_template(self):
        self.client.get(url_for("auth.login"))
        self.assertTemplateUsed("login.html")

    def test_auth_blueprint_login_post(self):
        test_form_fake ={
            "username":"Daniel",
            "password":"1234"
        }
        response = self.client.post(url_for("auth.login"),data=test_form_fake)
        self.assertRedirects(response,url_for("index"))