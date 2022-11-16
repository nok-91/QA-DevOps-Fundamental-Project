from flask_testing import TestCase
from application import app, db
from application.models import Task, Category
from flask import url_for
import datetime


class TestBase(TestCase):
        def create_app(self):

        # Pass in testing configurations for the app. 
        # Here we use sqlite without a persistent database for our tests.
                app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                        SECRET_KEY='TEST_SECRET_KEY',
                        DEBUG=True,
                        WTF_CSRF_ENABLED=False
                        )
                return app

# Will be called before every test
        def setUp(self):
                # Create table
                db.create_all()
        
                #Create test objects
                category1 = Category(category_id=1, category_title='title')
                task1 = Task(description='desc', date=datetime.date.today(), completed=False, category_id=1)
                #data = db.session.query(Task, Category).join(Category).all()
                # save users to database
                db.session.add(category1)
                db.session.add(task1)
                db.session.commit()

        def tearDown(self):
                #Close the database session and remove all contents of the database
                db.session.remove()
                db.drop_all()


class TestHome(TestBase):
        def test_home(self):
                response = self.client.get(url_for('home'))
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Home', response.data)


class TestGetAddCat(TestBase):
        def test_cat_get(self):
                response = self.client.get(url_for('add_category'))  
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Add Category', response.data)


class TestAddCat(TestBase):
        def test_add_cat(self):
                response = self.client.get(
                        url_for('add_category'),
                        data=dict(category_title='title'),
                        follow_redirects=True
                )   
                self.assertIn(b'Add', response.data)


class TestGetAddTask(TestBase):
        def test_task_get(self):
                response = self.client.get(url_for('add_task'))  
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Add', response.data)


class TestAddTask(TestBase):       
        def test_add_task(self):
                response = self.client.post(
                        url_for('add_task'),
                        data=dict(description='words',date=datetime.date.today(), completed=False, category_id=1),
                        follow_redirects=True
                        )
                self.assertIn(b'Add', response.data)


class TestGetUpdate(TestBase):
        def test_get_update(self):
                response = self.client.get(url_for('update_task', tid=1))  
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Update', response.data)


class TestUpdateTask(TestBase):       
        def test_Update_task(self):
                response = self.client.post(
                        url_for('update_task', tid=1),
                        data=dict(description='words',date=datetime.date.today(), completed=False, category_id=1),
                        follow_redirects=True
                        )
                self.assertIn(b'Update', response.data)


class TestDeleteTask(TestBase):
        def test_delete_task(self):
                response = self.client.get(url_for('delete_task', tid=1), follow_redirects=True)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Delete', response.data)


class TestIscomplete(TestBase):
        def test_IsComplete(self):
                response = self.client.get(url_for('is_complete', tid=1), follow_redirects=True)
                self.assertEqual(response.status_code, 200)
                self.assertIn(b'Complete', response.data)